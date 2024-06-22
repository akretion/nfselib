import xml.etree.ElementTree as ET
import os
import subprocess
import csv
from collections import OrderedDict


city_data = {}
padrao_population = {}


def load_population_data(csv_file):
    population_data = {}
    with open(csv_file, mode="r", encoding="latin1") as file:
        reader = csv.reader(file, delimiter=";")
        for index, row in enumerate(reader):
            if index == 0 or not row[6].isdigit():
                continue
            population_data[str(row[2])] = int(row[6])
    return population_data


def order_cities_by_population(cities, population_data):
    """
    Use IBGE population to use the wsdl of the largest cities (likely be safest)
    """
    sorted_cities = OrderedDict(
        sorted(
            cities.items(),
            key=lambda item: population_data.get(item[0], 1000000000),
            reverse=True,
        )
    )
    return sorted_cities


def parse_wsdl_production(
    xml_file, city_data, population_data, padrao_population
):
    # Load and parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialize an empty dictionary
    wsdl_dict = {}

    # Iterate through each Estado element
    for item in root.findall("Estado"):
        padrao = item.get("Padrao")
        city = item.get("Nome").split("-")[0].strip()
        ibge_code = item.get("ID")
        city_data[ibge_code] = (
            city,
            ibge_code,
            item.get("UF"),
            population_data.get(ibge_code, 0),
        )
        if padrao not in padrao_population:
            padrao_population[padrao] = 0
        padrao_population[padrao] += (
            population_data.get(ibge_code, 0) if ibge_code.isdigit() else 0
        )
        if padrao not in wsdl_dict:
            wsdl_dict[padrao] = {}
        wsdl_dict[padrao][ibge_code] = {}

        # Get the production WSDL file paths
        local_producao = item.find("LocalProducao")
        if local_producao is not None:
            wsdl_files = {}
            for action in local_producao:
                if action.text:
                    wsdl_files[action.text.split("\\")[-1]] = action.tag
            wsdl_dict[padrao][ibge_code] = wsdl_files

    return wsdl_dict


def format_cities_to_markdown(
    padrao,
    cities,
    schema_status,
    soap_status,
    city_data,
):
    schema_emoji = "✅" if schema_status else "❌"
    soap_emoji = "✅" if soap_status else "❌"

    header = f"## {padrao}\n**Schema:** {schema_emoji} - **SOAP:** {soap_emoji}\n\n"
    table_header = "| Cidade | IBGE | UF | Population |\n|------|----|---|----------|\n"
    table_rows = [
        f"| {city_data[ibge_code][0]} | {city_data[ibge_code][1]} | {city_data[ibge_code][2]} | {city_data[ibge_code][3]} |"
        for ibge_code in cities.keys()
        if city_data[ibge_code][1] and city_data[ibge_code][2] != "AN"
    ]
    table = table_header + "\n".join(table_rows) + "\n"
    return header + table


def create_markdown_report(
    sorted_wsdl_dict,
    city_data,
    schema_errors,
    soap_errors,
):
    report = "# NFSe Web Services\n\n"

    for padrao, cities in sorted_wsdl_dict.items():
        if not len(cities.keys()):
            continue
        cities = order_cities_by_population(cities, population_data)
        schema_status = padrao not in schema_errors
        soap_status = padrao not in soap_errors

        markdown_section = format_cities_to_markdown(
            padrao,
            cities,
            schema_status,
            soap_status,
            city_data,
        )
        report += markdown_section + "\n"

    return report


xml_file = "WSDL/Webservice.xml"
# csv comes from http://blog.mds.gov.br/redesuas/wp-content/uploads/2018/06/Lista_Munic%C3%ADpios_com_IBGE_Brasil_Versao_CSV.csv
population_data = load_population_data("cities_ibge_data.csv")
wsdl_dict = parse_wsdl_production(
    xml_file, city_data, population_data, padrao_population
)
sorted_wsdl_dict = OrderedDict(
    sorted(wsdl_dict.items(), key=lambda item: padrao_population[item[0]], reverse=True)
)


schema_errors = set()
soap_errors = set()

for padrao, cities in sorted_wsdl_dict.items():
    if not len(cities.keys()):
        continue
    cities = order_cities_by_population(cities, population_data)
    population = padrao_population[padrao]

    padrao_dir = os.path.join("nfselib", padrao.lower())
    os.makedirs(padrao_dir, exist_ok=True)
    schema_result = subprocess.run(
        [
            "xsdata",
            "generate",
            f"schemas/NFSe/{padrao}",
            "--package",
            f"nfselib.{padrao.lower()}.bindings",
        ]
    )
    if schema_result.returncode != 0:
        schema_errors.add(padrao)

    soap_errors.add(padrao)
    for city_code, wsdl_files in cities.items():
        all_wsdl_files_ok = len(wsdl_files.keys()) > 0
        city = city_data[city_code]
        for wsdl_file in wsdl_files.keys():
            print(f"\t{city}, wsdl file: {wsdl_file}")
            wsdl_result = subprocess.run(
                [
                    "xsdata",
                    "generate",
                    f"WSDL/Producao/{wsdl_file}",
                    "--package",
                    f"nfselib.{padrao.lower()}.soap",
                ]
            )
            if wsdl_result.returncode != 0:  # wsdl is KO
                all_wsdl_files_ok = False
                break
        if all_wsdl_files_ok:
            soap_errors.remove(padrao)
            break

print("schema_errors", schema_errors)
print("soap_errors", soap_errors)


markdown_report = create_markdown_report(
    sorted_wsdl_dict, city_data, schema_errors, soap_errors
)

# Write the markdown_report to CITIES.md file
with open("CITIES.md", "w", encoding="utf-8") as file:
    file.write(markdown_report)
