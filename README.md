[![Build Status](https://github.com/akretion/nfselib/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/akretion/nfselib/actions/workflows/tests.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/akretion/nfselib/graph/badge.svg?token=Xg2OpCNM5N)](https://codecov.io/gh/akretion/nfselib)
[![PyPI](https://img.shields.io/pypi/v/nfselib-legacy)](https://pypi.org/project/nfselib-legacy)

# nfselib: a lib Python que suporta a NFS-e de mais de 450 cidades do Brasil

A nfselib usa os schemas do famoso projeto open source
[UNINFE](https://unimake.com.br/uninfe/) junto com o poder do
[xsdata](https://xsdata.readthedocs.io/en/latest/) para tornar facil a importação e
geração dos arquivos XML das NFS-e de mais de 450 cidades do Brasil no ambiente Python.

Existe também agora a NFS-e com o padrão da Receita Federal, esse esta suportado pela
[nfelib](https://github.com/akretion/nfelib), uma lib mais générica sem ligação com o
UNINFE e que suporta todos padrões de notas fiscais nacionais.

## Installation

Devido a 'name squatting', o pacote foi renomeado nfselib-legacy no PyPI. O sufixo
'legacy' indica que esse pacote lida com os padrões anteriores à NFS-e nacional.

`pip install nfselib-legacy`

# NFSe Web Services

## GINFES

**Schema:** ✅ - **SOAP:** ❌

| Cidade                | IBGE    | UF  | Population |
| --------------------- | ------- | --- | ---------- |
| Fortaleza             | 2304400 | CE  | 2452185    |
| Guarulhos             | 3518800 | SP  | 1221979    |
| Maceió                | 2704302 | AL  | 932748     |
| São Bernardo do Campo | 3548708 | SP  | 765463     |
| Santo André           | 3547809 | SP  | 676407     |
| Contagem              | 3118601 | MG  | 603442     |
| Ananindeua            | 1500800 | PA  | 471980     |
| Campos dos Goytacazes | 3301009 | RJ  | 463731     |
| Santos                | 3548500 | SP  | 419400     |
| Mauá                  | 3529401 | SP  | 417064     |
| São José do Rio Preto | 3549805 | SP  | 408258     |
| Diadema               | 3513801 | SP  | 386089     |
| Betim                 | 3106705 | MG  | 378089     |
| Jundiaí               | 3525904 | SP  | 370126     |
| Itaquaquecetuba       | 3523107 | SP  | 321770     |
| Franca                | 3516200 | SP  | 318640     |
| Caruaru               | 2604106 | PE  | 314912     |
| São José dos Pinhais  | 4125506 | PR  | 264210     |
| Araraquara            | 3503208 | SP  | 208662     |
| Hortolândia           | 3519071 | SP  | 192692     |
| Rio Claro             | 3543907 | SP  | 186253     |
| Itu                   | 3523909 | SP  | 154147     |
| São Caetano do Sul    | 3548807 | SP  | 149263     |
| Salto                 | 3545209 | SP  | 105516     |
| Muriaé                | 3143906 | MG  | 100765     |
| Umuarama              | 4128104 | PR  | 100676     |
| Paulínia              | 3536505 | SP  | 82146      |
| Matão                 | 3529302 | SP  | 76786      |
| Jaboticabal           | 3524303 | SP  | 71662      |
| Registro              | 3542602 | SP  | 54261      |
| Mineiros              | 5213103 | GO  | 52935      |
| Olímpia               | 3533908 | SP  | 50024      |
| Capivari              | 3510401 | SP  | 48576      |
| Bertioga              | 3506359 | SP  | 47645      |
| Marechal Deodoro      | 2704708 | AL  | 45977      |

## PAULISTANA

**Schema:** ✅ - **SOAP:** ❌

| Cidade    | IBGE    | UF  | Population |
| --------- | ------- | --- | ---------- |
| São Paulo | 3550308 | SP  | 11253503   |

## DSF

**Schema:** ✅ - **SOAP:** ✅

| Cidade              | IBGE    | UF  | Population |
| ------------------- | ------- | --- | ---------- |
| Belém               | 1501402 | PA  | 1393399    |
| Campinas            | 3509502 | SP  | 1080113    |
| São Luis            | 2111300 | MA  | 1014837    |
| Teresina            | 2211001 | PI  | 814230     |
| Nova Iguaçu         | 3303500 | RJ  | 796257     |
| Campo Grande        | 5002704 | MS  | 786797     |
| São José dos Campos | 3549904 | SP  | 629921     |
| Uberlândia          | 3170206 | MG  | 604013     |
| Sorocaba            | 3552205 | SP  | 586625     |

## CARIOCA

**Schema:** ✅ - **SOAP:** ✅

| Cidade         | IBGE    | UF  | Population |
| -------------- | ------- | --- | ---------- |
| Rio de Janeiro | 3304557 | RJ  | 6320446    |

## ISSNET

**Schema:** ✅ - **SOAP:** ✅

| Cidade            | IBGE    | UF  | Population |
| ----------------- | ------- | --- | ---------- |
| Brasília          | 5300108 | DF  | 2570160    |
| Duque de Caxias   | 3301702 | RJ  | 855048     |
| Ribeirão Preto    | 3543402 | SP  | 604682     |
| Cuiabá            | 5103403 | MT  | 551098     |
| Aparecida Goiania | 5201405 | GO  | 455657     |
| Anapolis          | 5201108 | GO  | 334613     |
| Santa Maria       | 4316907 | RS  | 261031     |
| Jacareí           | 3524402 | SP  | 211214     |
| Cruz Alta         | 4306106 | RS  | 62821      |

## IPM

**Schema:** ✅ - **SOAP:** ✅

| Cidade                  | IBGE    | UF  | Population |
| ----------------------- | ------- | --- | ---------- |
| Cascavel                | 4104808 | PR  | 286205     |
| Gravataí                | 4309209 | RS  | 255660     |
| Novo Hamburgo           | 4313409 | RS  | 238940     |
| Colombo                 | 4105805 | PR  | 212967     |
| São José                | 4216602 | SC  | 209804     |
| Alvorada                | 4300604 | RS  | 195673     |
| Guarapuava              | 4109401 | PR  | 167328     |
| Paranaguá               | 4118204 | PR  | 140469     |
| Palhoça                 | 4211900 | SC  | 137334     |
| Apucarana               | 4101408 | PR  | 120919     |
| Cachoeirinha            | 4303103 | RS  | 118278     |
| Pinhas                  | 4119152 | PR  | 117008     |
| Campo Largo             | 4104204 | PR  | 112377     |
| Bento Gonçalves         | 4302105 | RS  | 107278     |
| Brusque                 | 4202909 | SC  | 105503     |
| Guaíba                  | 4309308 | RS  | 95204      |
| Campo Mourão            | 4104303 | PR  | 87194      |
| Paranavaí               | 4118402 | PR  | 81590      |
| Sapiranga               | 4319901 | RS  | 74985      |
| São Bento do Sul        | 4215802 | SC  | 74801      |
| Concórdia               | 4204301 | SC  | 68621      |
| Santa Rosa              | 4317202 | RS  | 68587      |
| Castro                  | 4104907 | PR  | 67084      |
| Camboriú                | 4203204 | SC  | 62361      |
| Rio do Sul              | 4214805 | SC  | 61198      |
| Carazinho               | 4304705 | RS  | 59317      |
| Biguaçu                 | 4202305 | SC  | 58206      |
| Indaial                 | 4207502 | SC  | 54854      |
| Canoinhas               | 4203808 | SC  | 52765      |
| Marechal Cândido Rondon | 4114609 | PR  | 46819      |
| Osório                  | 4313508 | RS  | 40906      |
| Rio Negrinho            | 4215000 | SC  | 39846      |
| Timbó                   | 4218202 | SC  | 36774      |
| Guaramirim              | 4206504 | SC  | 35172      |
| Guaíra                  | 4108809 | PR  | 30704      |
| Estrela                 | 4307807 | RS  | 30619      |
| Pomerode                | 4213203 | SC  | 27759      |
| Penha                   | 4212502 | SC  | 25141      |
| Araquari                | 4201307 | SC  | 24810      |
| Vera Cruz               | 4322707 | RS  | 23983      |
| Rolante                 | 4316006 | RS  | 19485      |
| Taió                    | 4217808 | SC  | 17260      |
| Balneário Piçarras      | 4212809 | SC  | 17078      |
| Porto Belo              | 4213500 | SC  | 16083      |
| Terra Boa               | 4127205 | PR  | 15776      |
| Corupá                  | 4204509 | SC  | 13852      |
| Paraíso do Norte        | 4118006 | PR  | 11772      |
| Rio dos Cedros          | 4214706 | SC  | 10284      |
| Lontras                 | 4209904 | SC  | 10244      |
| Ouro                    | 4211801 | SC  | 7372       |

## BHISS

**Schema:** ✅ - **SOAP:** ❌

| Cidade         | IBGE    | UF  | Population |
| -------------- | ------- | --- | ---------- |
| Belo Horizonte | 3106200 | MG  | 2375151    |
| Porto Alegre   | 4314902 | RS  | 1409351    |

## SIGCORP_SIGISS

**Schema:** ✅ - **SOAP:** ❌

| Cidade               | IBGE    | UF  | Population |
| -------------------- | ------- | --- | ---------- |
| Londrina             | 4113700 | PR  | 506701     |
| São João de Meriti   | 3305109 | RJ  | 458673     |
| Taubaté              | 3554102 | SP  | 278686     |
| Governador Valadares | 3127701 | MG  | 263689     |
| Ipatinga             | 3131307 | MG  | 239468     |
| Marília              | 3529005 | SP  | 216745     |
| Rio Grande           | 4315602 | RS  | 197228     |
| Cabo Frio            | 3300704 | RJ  | 186227     |
| Chapecó              | 4204202 | SC  | 183530     |
| Nilópolis            | 3303203 | RJ  | 157425     |
| Mogi Guaçu           | 3530706 | SP  | 137245     |
| Barretos             | 3505500 | SP  | 112101     |
| Mogi Mirim           | 3530805 | SP  | 86505      |
| Avaré                | 3504503 | SP  | 82934      |
| Sarandi              | 4126256 | PR  | 82847      |
| Nova Serrana         | 3145208 | MG  | 73699      |
| Cianorte             | 4105508 | PR  | 69958      |
| Tremembé             | 3554805 | SP  | 40984      |

## BETHA

**Schema:** ✅ - **SOAP:** ❌

| Cidade                    | IBGE    | UF  | Population |
| ------------------------- | ------- | --- | ---------- |
| Divinópolis               | 3122306 | MG  | 213016     |
| Criciúma                  | 4204608 | SC  | 192308     |
| Rio Vede                  | 5218805 | GO  | 176424     |
| Lages                     | 4209300 | SC  | 156727     |
| Jaragua do Sul            | 4208906 | SC  | 143123     |
| Varginha                  | 3170701 | MG  | 123081     |
| Resende                   | 3304201 | RJ  | 119769     |
| Araruama                  | 3300209 | RJ  | 112008     |
| Almirante Tamandaré       | 4100400 | PR  | 103204     |
| Fazenda Rio Grande        | 4107652 | PR  | 81675      |
| Timóteo                   | 3168705 | MG  | 81243      |
| Alfenas                   | 3101607 | MG  | 73774      |
| Valença                   | 3306107 | RJ  | 71843      |
| Navegantes                | 4211306 | SC  | 60556      |
| Biguaçu                   | 4202305 | SC  | 58206      |
| Nova Andradina            | 5006200 | MS  | 45585      |
| Lucas do Rio Verde        | 5105259 | MT  | 45556      |
| Imbituba                  | 4207304 | SC  | 40170      |
| Curitibanos               | 4204806 | SC  | 37748      |
| Maracaju                  | 5005400 | MS  | 37405      |
| Torres                    | 4321501 | RS  | 34656      |
| Jaguariaíva               | 4112009 | PR  | 32606      |
| Gramado                   | 4309100 | RS  | 32273      |
| Bandeirantes              | 4102406 | PR  | 32184      |
| Aguaí                     | 3500303 | SP  | 32148      |
| TIJUCAS                   | 4218004 | SC  | 30960      |
| Rio Brilhante             | 5007208 | MS  | 30663      |
| Braço do Norte            | 4202800 | SC  | 29018      |
| Mantena                   | 3139607 | MG  | 27111      |
| Joaçaba                   | 4209003 | SC  | 27020      |
| Sombrio                   | 4217709 | SC  | 26613      |
| Cláudio                   | 3116605 | MG  | 25771      |
| Caarapó                   | 5002407 | MS  | 25767      |
| Xaxim                     | 4219705 | SC  | 25713      |
| Pinheiral                 | 3303955 | RJ  | 22719      |
| Forquilhinha              | 4205456 | SC  | 22548      |
| São Lourenço do Oeste     | 4216909 | SC  | 21792      |
| Orleans                   | 4211702 | SC  | 21393      |
| Vila Rica                 | 5108600 | MT  | 21382      |
| Herval D'Oeste            | 4206702 | SC  | 21239      |
| Capinzal                  | 4203907 | SC  | 20769      |
| Urussanga                 | 4219002 | SC  | 20223      |
| Quatro Barras             | 4120804 | PR  | 19851      |
| Mandaguaçú                | 4114104 | PR  | 19781      |
| Fátima do Sul             | 5003801 | MS  | 19035      |
| Rio Verde de Mato Grosso  | 5007406 | MS  | 18890      |
| Itaquiraí                 | 5004601 | MS  | 18614      |
| Papanduva                 | 4212205 | SC  | 17928      |
| Mundo Novo                | 5005681 | MS  | 17043      |
| Morro da Fumaça           | 4211207 | SC  | 16126      |
| Santa Cecília             | 4215505 | SC  | 15757      |
| Porto Murtinho            | 5006903 | MS  | 15372      |
| Schroeder                 | 4217402 | SC  | 15316      |
| Cocal do Sul              | 4204251 | SC  | 15159      |
| Bombinhas                 | 4202453 | SC  | 14293      |
| Santo Augusto             | 4317806 | RS  | 13968      |
| Tenente Portela           | 4321402 | RS  | 13719      |
| Alterosa                  | 3102001 | MG  | 13717      |
| Nova Veneza               | 4211603 | SC  | 13309      |
| Siderópolis               | 4217600 | SC  | 12998      |
| Nova Trento               | 4211504 | SC  | 12190      |
| Deodápolis                | 5003454 | MS  | 12139      |
| São Ludgero               | 4217006 | SC  | 10993      |
| Urubici                   | 4218905 | SC  | 10699      |
| Santa Tereza do Oeste     | 4124020 | PR  | 10332      |
| Catanduvas                | 4204004 | SC  | 9555       |
| Igaratinga                | 3130200 | MG  | 9264       |
| Armazém                   | 4201505 | SC  | 7753       |
| Boqueirão do Leão         | 4302451 | RS  | 7673       |
| Santana da Vargem         | 3158300 | MG  | 7231       |
| Passo de Torres           | 4212254 | SC  | 6627       |
| Vitorino                  | 4128708 | PR  | 6513       |
| Maracajá                  | 4210407 | SC  | 6404       |
| Grão                      | 4206108 | SC  | 6223       |
| Luzerna                   | 4210035 | SC  | 5600       |
| Novo Horizonte do Sul     | 5006259 | MS  | 4940       |
| Presidente Castelo Branco | 4120408 | PR  | 4784       |
| Erval Velho               | 4205209 | SC  | 4352       |
| Pedras Grandes            | 4212403 | SC  | 4107       |
| Jaborá                    | 4208609 | SC  | 4041       |
| Cordilheira Alta          | 4204350 | SC  | 3767       |
| Taquarussu                | 5007976 | MS  | 3518       |

## SALVADOR_BA

**Schema:** ✅ - **SOAP:** ✅

| Cidade   | IBGE    | UF  | Population |
| -------- | ------- | --- | ---------- |
| Salvador | 2927408 | BA  | 2675656    |

## SMARAPD

**Schema:** ✅ - **SOAP:** ❌

| Cidade          | IBGE    | UF  | Population |
| --------------- | ------- | --- | ---------- |
| Vila Velha      | 3205200 | ES  | 414586     |
| Serra           | 3205002 | ES  | 409267     |
| Mogi das Cruzes | 3530607 | SP  | 387779     |
| Cariacica       | 3201308 | ES  | 348738     |
| Bauru           | 3506003 | SP  | 343937     |
| Sertãozinho     | 3551702 | SP  | 110074     |
| Birigui         | 3506508 | SP  | 108728     |
| Guarapari       | 3202405 | ES  | 105286     |
| Arujá           | 3503901 | SP  | 74905      |

## PRONIN

**Schema:** ✅ - **SOAP:** ✅

| Cidade                    | IBGE    | UF  | Population |
| ------------------------- | ------- | --- | ---------- |
| Montes Claros             | 3143302 | MG  | 361915     |
| Viamão                    | 4323002 | RS  | 239384     |
| Castanhal                 | 1502400 | PA  | 173149     |
| Uruguaiana                | 4322400 | RS  | 125435     |
| Itabira                   | 3131703 | MG  | 109783     |
| Itaperuna                 | 3302205 | RJ  | 95841      |
| Caratinga                 | 3113404 | MG  | 85239      |
| Cachoeira do Sul          | 4303004 | RS  | 83827      |
| Ijuí                      | 4310207 | RS  | 78915      |
| Alegrete                  | 4300406 | RS  | 77653      |
| Pato Branco               | 4118501 | PR  | 72370      |
| Vacaria                   | 4322509 | RS  | 61342      |
| São Gabriel               | 4318309 | RS  | 60425      |
| Cosmópolis                | 3512803 | SP  | 58827      |
| Rolandia                  | 4122404 | PR  | 57862      |
| Mirassol                  | 3530300 | SP  | 53792      |
| Canguçu                   | 4304507 | RS  | 53259      |
| Boituva                   | 3507001 | SP  | 48314      |
| Naviraí                   | 5005707 | MS  | 46424      |
| Medianeira                | 4115804 | PR  | 41817      |
| Caçapava do Sul           | 4302808 | RS  | 33690      |
| São Pedro                 | 3550407 | SP  | 31662      |
| Tres Coroas               | 4321709 | RS  | 23848      |
| Álvares Machado           | 3501301 | SP  | 23513      |
| Teodoro Sampaio           | 3554300 | SP  | 21386      |
| Santa Terezinha de Itaipu | 4124053 | PR  | 20841      |
| Bastos                    | 3505807 | SP  | 20445      |
| Regente Feijó             | 3542404 | SP  | 18494      |
| Horizontina               | 4309605 | RS  | 18348      |
| Paranapanema              | 3535804 | SP  | 17808      |
| Agudo                     | 4300109 | RS  | 16722      |
| Getúlio Vargas            | 4308904 | RS  | 16154      |
| São Sebastião da Grama    | 3550803 | SP  | 12099      |
| Tapera                    | 4321006 | RS  | 10448      |
| Pântano Grande            | 4313953 | RS  | 9895       |
| Entre                     | 4306932 | RS  | 8938       |
| Arroio do Sal             | 4301057 | RS  | 7740       |
| Picada Café               | 4314423 | RS  | 5182       |

## WEBISS

**Schema:** ✅ - **SOAP:** ✅

| Cidade                 | IBGE    | UF  | Population |
| ---------------------- | ------- | --- | ---------- |
| Feira de Santana       | 2910800 | BA  | 556642     |
| Uberaba                | 3170107 | MG  | 295988     |
| Itabuna                | 2914802 | BA  | 204667     |
| Araguaína              | 1702109 | TO  | 150484     |
| Porto Seguro           | 2925303 | BA  | 126929     |
| Barbacena              | 3105608 | MG  | 126284     |
| Passos                 | 3147907 | MG  | 106290     |
| Santo Antônio de Jesus | 2928703 | BA  | 90985      |
| Itabaiana              | 2802908 | SE  | 86967      |
| Candeias               | 2906501 | BA  | 83158      |
| Senhor do Bonfim       | 2930105 | BA  | 74419      |
| Formiga                | 3126109 | MG  | 65128      |
| Brumado                | 2904605 | BA  | 64602      |
| Içara                  | 4207007 | SC  | 58833      |
| Bom Despacho           | 3107406 | MG  | 45624      |
| Arcos                  | 3104205 | MG  | 36597      |
| São José do Rio Claro  | 5107305 | MT  | 17124      |
| Prudente Morais        | 3153608 | MG  | 9573       |

## TINUS

**Schema:** ✅ - **SOAP:** ✅

| Cidade                  | IBGE    | UF  | Population |
| ----------------------- | ------- | --- | ---------- |
| Jaboatão dos Guararapes | 2607901 | PE  | 644620     |
| Olinda                  | 2609600 | PE  | 377779     |
| Paulista                | 2610707 | PE  | 300466     |
| Mossoró                 | 2408003 | RN  | 259815     |
| Cabo de Santo Agostinho | 2602902 | PE  | 185025     |
| Garanhuns               | 2606002 | PE  | 129408     |
| São Gonçalo do Amarante | 2412005 | RN  | 87668      |
| Ipojuca                 | 2607208 | PE  | 80637      |
| Goiana                  | 2606200 | PE  | 75644      |
| Cabedelo                | 2503209 | PB  | 57944      |

## EL

**Schema:** ✅ - **SOAP:** ✅

| Cidade                  | IBGE    | UF  | Population |
| ----------------------- | ------- | --- | ---------- |
| Porto Velho             | 1100205 | RO  | 428527     |
| Vitória da Conquista    | 2933307 | BA  | 306866     |
| Cachoeiro de Itapemirim | 3201209 | ES  | 189889     |
| Nova Friburgo           | 3303401 | RJ  | 182082     |
| Linhares                | 3203205 | ES  | 141306     |
| Teixeira de Freitas     | 2931350 | BA  | 138341     |
| Barreiras               | 2903201 | BA  | 137427     |
| Simões Filho            | 2930709 | BA  | 118047     |
| Colatina                | 3201506 | ES  | 111788     |
| João Monlevade          | 3136207 | MG  | 73610      |
| Manhuaçu                | 3205101 | MG  | 65001      |
| Barra de São Francisco  | 3200904 | ES  | 40649      |
| Taiobeiras              | 3168002 | MG  | 30917      |
| São João do Paraíso     | 3162708 | MG  | 22319      |
| Piuma                   | 3204203 | ES  | 18123      |
| Iconha                  | 3202603 | ES  | 12523      |

## MANAUS_AM

**Schema:** ✅ - **SOAP:** ✅

| Cidade | IBGE    | UF  | Population |
| ------ | ------- | --- | ---------- |
| Manaus | 1302603 | AM  | 1802014    |

## SIMPLISS

**Schema:** ✅ - **SOAP:** ❌

| Cidade                | IBGE    | UF  | Population |
| --------------------- | ------- | --- | ---------- |
| Piracicaba            | 3538709 | SP  | 364571     |
| Blumenau              | 4202404 | SC  | 309011     |
| Volta Redonda         | 3306305 | RJ  | 257803     |
| Embu das Artes        | 3515004 | SP  | 240230     |
| Presidente Prudente   | 3541406 | SP  | 207610     |
| Araras                | 3503307 | SP  | 118843     |
| São João da Boa Vista | 3549102 | SP  | 83639      |
| Patrocínio            | 3148103 | MG  | 82471      |
| Paraguaçu Paulista    | 3535507 | SP  | 42278      |
| Vargem Grande do Sul  | 3556404 | SP  | 39266      |
| Astorga               | 4102109 | PR  | 24698      |
| Macaraí               | 3528809 | SP  | 13332      |

## TIPLAN

**Schema:** ✅ - **SOAP:** ✅

| Cidade | IBGE    | UF  | Population |
| ------ | ------- | --- | ---------- |
| Recife | 2611606 | PE  | 1537704    |
| Macaé  | 3302403 | RJ  | 206728     |
| Piraí  | 3304003 | RJ  | 26314      |

## EGOVERNE

**Schema:** ✅ - **SOAP:** ✅

| Cidade   | IBGE    | UF  | Population |
| -------- | ------- | --- | ---------- |
| Curitiba | 4106902 | PR  | 1751907    |

## WEBISS_202

**Schema:** ✅ - **SOAP:** ✅

| Cidade              | IBGE    | UF  | Population |
| ------------------- | ------- | --- | ---------- |
| Aracaju             | 2800308 | SE  | 571149     |
| Campina Grande      | 2504009 | PB  | 385213     |
| Palmas              | 1721000 | TO  | 228332     |
| Alagoinhas          | 2900702 | BA  | 141949     |
| Bagé                | 4301602 | RS  | 116794     |
| Barra do Piraí      | 3300308 | RJ  | 94778      |
| Vilhena             | 1100304 | RO  | 76202      |
| São Gonçalo do Pará | 3161809 | MG  | 10398      |
| Itanhangá           | 5104542 | MT  | 5276       |

## FIORILLI

**Schema:** ✅ - **SOAP:** ❌

| Cidade             | IBGE    | UF  | Population |
| ------------------ | ------- | --- | ---------- |
| Botucatu           | 3507506 | SP  | 127328     |
| Ji                 | 1100122 | RO  | 116610     |
| Catanduva          | 3511102 | SP  | 112820     |
| Corumbá            | 5003207 | MS  | 103703     |
| Três Lagoas        | 5008305 | MS  | 101791     |
| Itaituba           | 1503606 | PA  | 97493      |
| Assis              | 3504008 | SP  | 95144      |
| Senador Canedo     | 5220454 | GO  | 84443      |
| Fernandópolis      | 3515509 | SP  | 64696      |
| Monte Alto         | 3531308 | SP  | 46642      |
| Garça              | 3516705 | SP  | 43115      |
| Amambai            | 5000609 | MS  | 34730      |
| Bariri             | 3505203 | SP  | 31593      |
| Ouro Fino          | 3146008 | MG  | 31568      |
| Rio das Pedras     | 3544004 | SP  | 29501      |
| Canaã dos Carajás  | 1502152 | PA  | 26716      |
| Veranópolis        | 4322806 | RS  | 22810      |
| Taquarituba        | 3553807 | SP  | 22291      |
| Ribas do Rio Pardo | 5007109 | MS  | 20946      |
| Águas de Lindóia   | 3500501 | SP  | 17266      |
| Potirendaba        | 3540804 | SP  | 15449      |
| Itaporanga         | 3522802 | SP  | 14549      |
| Serafina Corrêa    | 4320404 | RS  | 14253      |
| Xangri             | 4323804 | RS  | 12434      |
| Duartina           | 3514502 | SP  | 12251      |
| Piratininga        | 3539400 | SP  | 12072      |
| Três Cachoeiras    | 4321667 | RS  | 10217      |
| Cosmorama          | 3512902 | SP  | 7214       |
| Jaci               | 3524501 | SP  | 5657       |
| Mirassolândia      | 3530409 | SP  | 4295       |

## PROPRIOGOIANIA

**Schema:** ✅ - **SOAP:** ❌

| Cidade  | IBGE    | UF  | Population |
| ------- | ------- | --- | ---------- |
| Goiânia | 5208707 | GO  | 1302001    |

## GIF

**Schema:** ✅ - **SOAP:** ❌

| Cidade          | IBGE    | UF  | Population |
| --------------- | ------- | --- | ---------- |
| Caxias do Sul   | 4305108 | RS  | 435564     |
| Canoas          | 4304606 | RS  | 323827     |
| Sapucaia do Sul | 4320008 | RS  | 130957     |
| Farroupilha     | 4307906 | RS  | 63635      |
| São Borja       | 4318002 | RS  | 61671      |
| Campo Bom       | 4303905 | RS  | 60074      |
| Garibaldi       | 4308607 | RS  | 30689      |

## CONAM

**Schema:** ✅ - **SOAP:** ✅

| Cidade               | IBGE    | UF  | Population |
| -------------------- | ------- | --- | ---------- |
| Geral                | CONAN   | XX  | 0          |
| Taboão da Serra      | 3552809 | SP  | 244528     |
| Itapecerica da Serra | 3522208 | SP  | 152614     |
| Bragança Paulista    | 3507605 | SP  | 146744     |
| Jaú                  | 3525300 | SP  | 131040     |
| Poá                  | 3539806 | SP  | 106013     |
| Caieiras             | 3509007 | SP  | 86529      |
| Mairipora            | 3528502 | SP  | 80956      |
| Bebedouro            | 3506102 | SP  | 75035      |

## THEMA

**Schema:** ✅ - **SOAP:** ❌

| Cidade                    | IBGE    | UF  | Population |
| ------------------------- | ------- | --- | ---------- |
| São Leopoldo              | 4318705 | RS  | 214087     |
| Passo Fundo               | 4314100 | RS  | 184826     |
| Santa Cruz do Sul         | 4316808 | RS  | 118374     |
| Esteio                    | 4307708 | RS  | 80755      |
| Lajeado                   | 4311403 | RS  | 71445      |
| Venancio Aires            | 4322608 | RS  | 65946      |
| Montenegro                | 4312401 | RS  | 59415      |
| Gaspar                    | 4205902 | SC  | 57981      |
| Taquara                   | 4321204 | RS  | 54643      |
| Santo Antônio da Patrulha | 4317608 | RS  | 39685      |
| Imbe                      | 4310330 | RS  | 17670      |

## FINTEL

**Schema:** ✅ - **SOAP:** ✅

| Cidade       | IBGE    | UF  | Population |
| ------------ | ------- | --- | ---------- |
| Juiz de Fora | 3136702 | MG  | 516247     |
| Maringá      | 4115200 | PR  | 357077     |
| Paracambi    | 3303609 | RJ  | 47124      |

## TIPLAN_203

**Schema:** ✅ - **SOAP:** ✅

| Cidade         | IBGE    | UF  | Population |
| -------------- | ------- | --- | ---------- |
| Niterói        | 3303302 | RJ  | 487562     |
| Americana      | 3501608 | SP  | 210638     |
| Angra dos Reis | 3300100 | RJ  | 169511     |

## NATALENSE

**Schema:** ✅ - **SOAP:** ✅

| Cidade | IBGE    | UF  | Population |
| ------ | ------- | --- | ---------- |
| Natal  | 2408102 | RN  | 803739     |

## GIAP

**Schema:** ✅ - **SOAP:** ❌

| Cidade      | IBGE    | UF  | Population |
| ----------- | ------- | --- | ---------- |
| Carapicuíba | 3510609 | SP  | 369584     |
| São Carlos  | 3548906 | SP  | 221950     |
| Cotia       | 3513009 | SP  | 201150     |

## SISPMJP

**Schema:** ✅ - **SOAP:** ✅

| Cidade      | IBGE    | UF  | Population |
| ----------- | ------- | --- | ---------- |
| João Pessoa | 2507507 | PB  | 723515     |

## GOVDIGITAL

**Schema:** ✅ - **SOAP:** ✅

| Cidade                 | IBGE    | UF  | Population |
| ---------------------- | ------- | --- | ---------- |
| Poços de Caldas        | 3151800 | MG  | 152435     |
| Lavras                 | 3138203 | MG  | 92200      |
| Paracatu               | 3147006 | MG  | 84718      |
| São Roque              | 3550605 | SP  | 78821      |
| Pedro Leopoldo         | 3149309 | MG  | 58740      |
| Guaxupé                | 3128709 | MG  | 49430      |
| Vargem Grande Paulista | 3556453 | SP  | 42997      |
| Andradas               | 3102605 | MG  | 37270      |
| Igarapé                | 3130101 | MG  | 34851      |
| Prata                  | 3152808 | MG  | 25802      |
| São Joaquim de Bicas   | 3162922 | MG  | 25537      |
| São José da Lapa       | 3162955 | MG  | 19799      |

## BAUHAUS

**Schema:** ✅ - **SOAP:** ❌

| Cidade              | IBGE    | UF  | Population |
| ------------------- | ------- | --- | ---------- |
| Petrópolis          | 3303906 | RJ  | 295917     |
| São José do Ribamar | 2111201 | MA  | 163045     |
| Tubarão             | 4218707 | SC  | 97235      |
| Redenção            | 1506138 | PA  | 75556      |
| Itapema             | 4208302 | SC  | 45797      |

## EGOVERNEISS

**Schema:** ✅ - **SOAP:** ✅

| Cidade | IBGE    | UF  | Population |
| ------ | ------- | --- | ---------- |
| Osasco | 3534401 | SP  | 666740     |

## ISSONLINE_ASSESSORPUBLICO

**Schema:** ✅ - **SOAP:** ✅

| Cidade             | IBGE    | UF  | Population |
| ------------------ | ------- | --- | ---------- |
| Araçatuba          | 3502804 | SP  | 181579     |
| Votorantim         | 3557006 | SP  | 108809     |
| Lins               | 3527108 | SP  | 71432      |
| Pirassununga       | 3539301 | SP  | 70081      |
| Taquaritinga       | 3553708 | SP  | 53988      |
| Primavera do Leste | 5107040 | MT  | 52066      |
| Dracena            | 3514403 | SP  | 43258      |

## PORTALFACIL_ACTCON_202

**Schema:** ✅ - **SOAP:** ✅

| Cidade       | IBGE    | UF  | Population |
| ------------ | ------- | --- | ---------- |
| Imperatriz   | 2105302 | MA  | 247505     |
| Sete Lagoas  | 3167202 | MG  | 214152     |
| Ubá          | 3169901 | MG  | 101519     |
| Além Paraíba | 3101508 | MG  | 34349      |

## ELOTECH

**Schema:** ✅ - **SOAP:** ✅

| Cidade       | IBGE    | UF  | Population |
| ------------ | ------- | --- | ---------- |
| Ponta Grossa | 4119905 | PR  | 311611     |
| Piraquara    | 4119509 | PR  | 93207      |
| Irati        | 4110706 | PR  | 56207      |
| Palmeira     | 4117701 | PR  | 32123      |
| Marialva     | 4114807 | PR  | 31959      |
| Loanda       | 4113502 | PR  | 21201      |
| Marilena     | 4115002 | PR  | 6858       |

## EQUIPLANO

**Schema:** ✅ - **SOAP:** ❌

| Cidade                    | IBGE    | UF  | Population |
| ------------------------- | ------- | --- | ---------- |
| Toledo                    | 4127700 | PR  | 119313     |
| Francisco Beltrão         | 4108403 | PR  | 78943      |
| Prudentópolis             | 4120606 | PR  | 48792      |
| Dois Vizinhos             | 4107207 | PR  | 36179      |
| Laranjeiras do Sul        | 4113304 | PR  | 30777      |
| Ibaiti                    | 4109708 | PR  | 28751      |
| Imbituva                  | 4110102 | PR  | 28455      |
| Arapoti                   | 4101606 | PR  | 25855      |
| Santo Antonio do Sudoeste | 4124400 | PR  | 18893      |
| Capanema                  | 4104501 | PR  | 18526      |
| Sengés                    | 4126306 | PR  | 18414      |
| Candói                    | 4104428 | PR  | 14983      |
| Palmital                  | 4117800 | PR  | 14865      |
| Cafelândia                | 4103453 | PR  | 14662      |
| Rio Azul                  | 4122008 | PR  | 14093      |
| Balsa Nova                | 4102307 | PR  | 11300      |
| Missal                    | 4116059 | PR  | 10474      |
| Laranjal                  | 4113254 | PR  | 6360       |
| Pranchita                 | 4120358 | PR  | 5628       |

## COPLAN

**Schema:** ✅ - **SOAP:** ❌

| Cidade                | IBGE    | UF  | Population |
| --------------------- | ------- | --- | ---------- |
| Barra Mansa           | 3300407 | RJ  | 177813     |
| Sinop                 | 5107909 | MT  | 113099     |
| Barra do Garças       | 5101803 | MT  | 56560      |
| Guarantã do Norte     | 5104104 | MT  | 32216      |
| Nova Mutum            | 5106224 | MT  | 31649      |
| Peixoto de Azevedo    | 5106422 | MT  | 30812      |
| Campo Novo do Parecis | 5102637 | MT  | 27577      |
| Água Boa              | 5100201 | MT  | 20856      |
| Matupá                | 5105606 | MT  | 14174      |
| Juscimeira            | 5105200 | MT  | 11430      |

## PROPRIOJOINVILLESC

**Schema:** ✅ - **SOAP:** ❌

| Cidade    | IBGE    | UF  | Population |
| --------- | ------- | --- | ---------- |
| Joinville | 4209102 | SC  | 515288     |

## INTERSOL

**Schema:** ✅ - **SOAP:** ✅

| Cidade    | IBGE    | UF  | Population |
| --------- | ------- | --- | ---------- |
| Maracanaú | 2307650 | CE  | 209057     |
| Sobral    | 2312908 | CE  | 188233     |
| Eusébio   | 2304285 | CE  | 46033      |

## SONNER

**Schema:** ✅ - **SOAP:** ❌

| Cidade             | IBGE    | UF  | Population |
| ------------------ | ------- | --- | ---------- |
| Teófilo Otoni      | 3168606 | MG  | 134745     |
| Araguari           | 3103504 | MG  | 109801     |
| Coronel Fabriciano | 3119401 | MG  | 103694     |
| Itajubá            | 3132404 | MG  | 90658      |

## SOFTPLAN

**Schema:** ✅ - **SOAP:** ❌

| Cidade        | IBGE    | UF  | Population |
| ------------- | ------- | --- | ---------- |
| Florianópolis | 4205407 | SC  | 421240     |

## PUBLICA

**Schema:** ✅ - **SOAP:** ✅

| Cidade             | IBGE    | UF  | Population |
| ------------------ | ------- | --- | ---------- |
| Itajaí             | 4208203 | SC  | 183373     |
| Balneário Camboriú | 4202008 | SC  | 108089     |
| Caçador            | 4203006 | SC  | 70762      |
| Mafra              | 4210100 | SC  | 52912      |

## ADM_SISTEMAS

**Schema:** ✅ - **SOAP:** ❌

| Cidade                 | IBGE    | UF  | Population |
| ---------------------- | ------- | --- | ---------- |
| Boa Vista              | 1400100 | RR  | 284313     |
| Luis Eduardo Magalhães | 2919553 | BA  | 60105      |
| Amargosa               | 2901007 | BA  | 34351      |

## METROPOLIS

**Schema:** ✅ - **SOAP:** ❌

| Cidade           | IBGE    | UF  | Population |
| ---------------- | ------- | --- | ---------- |
| Ilhéus           | 2913606 | BA  | 184236     |
| Lauro de Freitas | 2919207 | BA  | 163449     |

## AVMB_ASTEN

**Schema:** ✅ - **SOAP:** ❌

| Cidade  | IBGE    | UF  | Population |
| ------- | ------- | --- | ---------- |
| Pelotas | 4314407 | RS  | 328275     |

## VVISS

**Schema:** ✅ - **SOAP:** ✅

| Cidade  | IBGE    | UF  | Population |
| ------- | ------- | --- | ---------- |
| Vitória | 3205309 | ES  | 327801     |

## VITORIA_ES

**Schema:** ✅ - **SOAP:** ✅

| Cidade  | IBGE    | UF  | Population |
| ------- | ------- | --- | ---------- |
| Vitória | 3205309 | ES  | 327801     |

## BSITBR

**Schema:** ✅ - **SOAP:** ✅

| Cidade     | IBGE    | UF  | Population |
| ---------- | ------- | --- | ---------- |
| Botucatu   | 3507506 | SP  | 127328     |
| Jataí      | 5211909 | GO  | 88006      |
| Cristalina | 5206206 | GO  | 46580      |
| Jaragua    | 5211800 | GO  | 41870      |
| Orizona    | 5215306 | GO  | 14300      |

## MODERNIZACAO_PUBLICA

**Schema:** ✅ - **SOAP:** ✅

| Cidade              | IBGE    | UF  | Population |
| ------------------- | ------- | --- | ---------- |
| Magé                | 3302502 | RJ  | 227322     |
| São pedro da aldeia | 3305208 | RJ  | 87875      |

## IIBRASIL

**Schema:** ✅ - **SOAP:** ❌

| Cidade  | IBGE    | UF  | Population |
| ------- | ------- | --- | ---------- |
| Limeira | 3526902 | SP  | 276022     |

## AGILI

**Schema:** ✅ - **SOAP:** ❌

| Cidade       | IBGE    | UF  | Population |
| ------------ | ------- | --- | ---------- |
| Rondonópolis | 5107602 | MT  | 195476     |
| Sorriso      | 5107925 | MT  | 66521      |

## TECNOSISTEMAS

**Schema:** ✅ - **SOAP:** ✅

| Cidade               | IBGE    | UF  | Population |
| -------------------- | ------- | --- | ---------- |
| Estância Velha       | 4307609 | RS  | 42574      |
| Portão               | 4314803 | RS  | 30920      |
| Dois Irmãos          | 4306403 | RS  | 27572      |
| Nova Prata           | 4313300 | RS  | 22830      |
| São Sebastião do Caí | 4319505 | RS  | 21932      |
| São Marcos           | 4319000 | RS  | 20103      |
| Ivoti                | 4310801 | RS  | 19874      |
| Tapejara             | 4320909 | RS  | 19250      |
| Cruzeiro do Sul      | 4306205 | RS  | 12320      |
| Terra de Areia       | 4321436 | RS  | 9878       |
| Paverama             | 4314159 | RS  | 8044       |
| Salvador do Sul      | 4316501 | RS  | 6747       |
| Harmonia             | 4309555 | RS  | 4254       |
| Pareci Novo          | 4314035 | RS  | 3511       |
| Maratá               | 4311791 | RS  | 2527       |
| Presidente Lucena    | 4315149 | RS  | 2484       |
| São José do Sul      | 4318614 | RS  | 2082       |

## LEXSOM

**Schema:** ✅ - **SOAP:** ✅

| Cidade        | IBGE    | UF  | Population |
| ------------- | ------- | --- | ---------- |
| Foz do Iguaçu | 4108304 | PR  | 256088     |

## ABACO

**Schema:** ✅ - **SOAP:** ✅

| Cidade        | IBGE    | UF  | Population |
| ------------- | ------- | --- | ---------- |
| Várzea Grande | 5108402 | MT  | 252596     |

## PRODATA

**Schema:** ✅ - **SOAP:** ❌

| Cidade    | IBGE    | UF  | Population |
| --------- | ------- | --- | ---------- |
| Cubatão   | 3513504 | SP  | 118720     |
| Catalão   | 5205109 | GO  | 86647      |
| Morrinhos | 5213806 | GO  | 41460      |

## CENTI

**Schema:** ✅ - **SOAP:** ❌

| Cidade    | IBGE    | UF  | Population |
| --------- | ------- | --- | ---------- |
| Formosa   | 5208004 | GO  | 100085     |
| Itumbiara | 5211503 | GO  | 92883      |
| Porangatu | 5218003 | GO  | 42355      |
| Edéia     | 5207402 | GO  | 11266      |

## PRODEB

**Schema:** ✅ - **SOAP:** ✅

| Cidade   | IBGE    | UF  | Population |
| -------- | ------- | --- | ---------- |
| Camaçari | 2905701 | BA  | 242970     |

## PROPRIOBARUERISP

**Schema:** ✅ - **SOAP:** ❌

| Cidade  | IBGE    | UF  | Population |
| ------- | ------- | --- | ---------- |
| Barueri | 3505708 | SP  | 240749     |

## ABASE

**Schema:** ✅ - **SOAP:** ❌

| Cidade                    | IBGE    | UF  | Population |
| ------------------------- | ------- | --- | ---------- |
| Santo Ângelo              | 4317509 | RS  | 76275      |
| São Luiz Gonzaga          | 4318903 | RS  | 34556      |
| Três de Maio              | 4321808 | RS  | 23726      |
| Giruá                     | 4309001 | RS  | 17075      |
| Santo Cristo              | 4317905 | RS  | 14378      |
| Cerro Largo               | 4305207 | RS  | 13289      |
| Santo Antônio das Missões | 4317707 | RS  | 11210      |
| Porto Xavier              | 4315107 | RS  | 10558      |
| Mauricio Cardoso          | 4306734 | RS  | 5313       |
| Caibaté                   | 4303301 | RS  | 4954       |

## ISSONLINE4R

**Schema:** ✅ - **SOAP:** ✅

| Cidade       | IBGE    | UF  | Population |
| ------------ | ------- | --- | ---------- |
| Itapetininga | 3522307 | SP  | 144377     |
| Andradina    | 3502101 | SP  | 55334      |
| Taquarivaí   | 3553856 | SP  | 5151       |

## MEMORY

**Schema:** ✅ - **SOAP:** ❌

| Cidade     | IBGE    | UF  | Population |
| ---------- | ------- | --- | ---------- |
| Curvelo    | 3120904 | MG  | 74219      |
| Ponte Nova | 3152105 | MG  | 57390      |
| Salinas    | 3157005 | MG  | 39178      |
| Matozinhos | 3141108 | MG  | 33955      |

## INDAIATUBA_SP

**Schema:** ✅ - **SOAP:** ✅

| Cidade     | IBGE    | UF  | Population |
| ---------- | ------- | --- | ---------- |
| Indaiatuba | 3520509 | SP  | 201619     |

## EMBRAS

**Schema:** ✅ - **SOAP:** ❌

| Cidade        | IBGE    | UF  | Population |
| ------------- | ------- | --- | ---------- |
| Guaratinguetá | 3518404 | SP  | 112072     |
| Lorena        | 3527207 | SP  | 82537      |
| Pouso Alto    | 3152600 | MG  | 6213       |

## RLZ_INFORMATICA_02

**Schema:** ✅ - **SOAP:** ✅

| Cidade           | IBGE    | UF  | Population |
| ---------------- | ------- | --- | ---------- |
| Cáceres          | 5102504 | MT  | 87942      |
| Tangará da Serra | 5107958 | MT  | 83431      |

## RLZ_INFORMATICA

**Schema:** ✅ - **SOAP:** ✅

| Cidade          | IBGE    | UF  | Population |
| --------------- | ------- | --- | ---------- |
| Votuporanga     | 3557105 | SP  | 84692      |
| Jales           | 3524808 | SP  | 47012      |
| Santa Fé do Sul | 3546603 | SP  | 29239      |

## SYSTEMPRO

**Schema:** ✅ - **SOAP:** ✅

| Cidade            | IBGE    | UF  | Population |
| ----------------- | ------- | --- | ---------- |
| Erechim           | 4307005 | RS  | 96087      |
| Canela            | 4304408 | RS  | 39229      |
| Barão de Cotegipe | 4301701 | RS  | 6529       |
| Estação           | 4307559 | RS  | 6011       |
| Campinas do Sul   | 4303806 | RS  | 5506       |
| Paulo Bento       | 4314134 | RS  | 2196       |

## SH3

**Schema:** ✅ - **SOAP:** ✅

| Cidade                 | IBGE    | UF  | Population |
| ---------------------- | ------- | --- | ---------- |
| São João del           | 3162500 | MG  | 84469      |
| Visconde do Rio Branco | 3172004 | MG  | 37942      |
| Barroso                | 3105905 | MG  | 19599      |

## CONSIST

**Schema:** ✅ - **SOAP:** ❌

| Cidade         | IBGE    | UF  | Population |
| -------------- | ------- | --- | ---------- |
| Patos de Minas | 3148004 | MG  | 138710     |

## TRIBUTUS

**Schema:** ✅ - **SOAP:** ❌

| Cidade   | IBGE    | UF  | Population |
| -------- | ------- | --- | ---------- |
| Gravatá  | 2606408 | PE  | 76458      |
| Palmares | 2610004 | PE  | 59526      |

## SUPERNOVA

**Schema:** ✅ - **SOAP:** ✅

| Cidade | IBGE    | UF  | Population |
| ------ | ------- | --- | ---------- |
| Sabará | 3156700 | MG  | 126269     |

## DBSELLER

**Schema:** ✅ - **SOAP:** ✅

| Cidade                | IBGE    | UF  | Population |
| --------------------- | ------- | --- | ---------- |
| Santana do Livramento | 4317103 | RS  | 82464      |
| Tramandaí             | 4321600 | RS  | 41585      |

## QUASAR

**Schema:** ✅ - **SOAP:** ❌

| Cidade        | IBGE    | UF  | Population |
| ------------- | ------- | --- | ---------- |
| Pará de Minas | 3147105 | MG  | 84215      |
| Igarapé       | 3130101 | MG  | 34851      |

## E_RECEITA

**Schema:** ✅ - **SOAP:** ✅

| Cidade                   | IBGE    | UF  | Population |
| ------------------------ | ------- | --- | ---------- |
| São Sebastião do Paraíso | 3164704 | MG  | 64980      |
| Monte Carmelo            | 3143104 | MG  | 45772      |

## CECAM

**Schema:** ❌ - **SOAP:** ✅

| Cidade   | IBGE    | UF  | Population |
| -------- | ------- | --- | ---------- |
| Ibiúna   | 3519709 | SP  | 71217      |
| Juquiá   | 3526100 | SP  | 19246      |
| Itatinga | 3523503 | SP  | 18052      |

## DESENVOLVECIDADE

**Schema:** ✅ - **SOAP:** ✅

| Cidade      | IBGE    | UF  | Population |
| ----------- | ------- | --- | ---------- |
| Paragominas | 1505502 | PA  | 97819      |

## SIGISSWEB

**Schema:** ✅ - **SOAP:** ❌

| Cidade | IBGE    | UF  | Population |
| ------ | ------- | --- | ---------- |
| Leme   | 3526704 | SP  | 91756      |

## ABACO_204

**Schema:** ✅ - **SOAP:** ✅

| Cidade    | IBGE    | UF  | Population |
| --------- | ------- | --- | ---------- |
| Nova Lima | 3144805 | MG  | 80998      |

## VERSATEC

**Schema:** ✅ - **SOAP:** ❌

| Cidade     | IBGE    | UF  | Population |
| ---------- | ------- | --- | ---------- |
| Cataguases | 3115300 | SP  | 69757      |

## WEBFISCO_TECNOLOGIA

**Schema:** ✅ - **SOAP:** ❌

| Cidade           | IBGE    | UF  | Population |
| ---------------- | ------- | --- | ---------- |
| Barra Bonita     | 3505302 | SP  | 35246      |
| Igaraçu do Tietê | 3520004 | SP  | 23362      |

## MGM

**Schema:** ✅ - **SOAP:** ✅

| Cidade    | IBGE    | UF  | Population |
| --------- | ------- | --- | ---------- |
| Penápolis | 3537305 | SP  | 58510      |

## MEGASOFT

**Schema:** ✅ - **SOAP:** ✅

| Cidade          | IBGE    | UF  | Population |
| --------------- | ------- | --- | ---------- |
| Padre Bernardo  | 5215603 | GO  | 27671      |
| Pontalina       | 5217708 | GO  | 17121      |
| Cromínia        | 5206503 | GO  | 3555       |
| Professor Jamil | 5218391 | GO  | 3239       |
| Mairipotaba     | 5212600 | GO  | 2374       |

## DUETO

**Schema:** ✅ - **SOAP:** ✅

| Cidade          | IBGE    | UF  | Population |
| --------------- | ------- | --- | ---------- |
| Triunfo         | 4322004 | RS  | 25793      |
| Nova Santa Rita | 4313375 | RS  | 22716      |

## NOBESISTEMAS

**Schema:** ✅ - **SOAP:** ❌

| Cidade  | IBGE    | UF  | Population |
| ------- | ------- | --- | ---------- |
| Guariba | 3518602 | SP  | 35486      |

## NOTAINTELIGENTE

**Schema:** ✅ - **SOAP:** ❌

| Cidade     | IBGE    | UF  | Population |
| ---------- | ------- | --- | ---------- |
| Itambacuri | 3132701 | MG  | 22809      |

## DIGIFRED

**Schema:** ✅ - **SOAP:** ❌

| Cidade    | IBGE    | UF  | Population |
| --------- | ------- | --- | ---------- |
| Ibirubá   | 4310009 | RS  | 19310      |
| Ernestina | 4307054 | RS  | 3088       |

## PUBLIC_SOFT

**Schema:** ✅ - **SOAP:** ✅

| Cidade | IBGE        | UF  | Population |
| ------ | ----------- | --- | ---------- |
| Geral  | PUBLIC_SOFT | XX  | 0          |

## NACIONAL

**Schema:** ✅ - **SOAP:** ❌

| Cidade | IBGE | UF  | Population |
| ------ | ---- | --- | ---------- |

## WEBFISCO

**Schema:** ✅ - **SOAP:** ❌

| Cidade | IBGE | UF  | Population |
| ------ | ---- | --- | ---------- |
