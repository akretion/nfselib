from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nfselib.desenvolvecidade.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    versao_dados: Optional[str] = field(
        default=None,
        metadata={
            "name": "versaoDados",
            "type": "Element",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 80,
            "white_space": "collapse",
        }
    )


@dataclass
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"

    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "length": 11,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "length": 14,
            "white_space": "collapse",
        }
    )


@dataclass
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"

    codigo_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoObra",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        }
    )
    art: Optional[str] = field(
        default=None,
        metadata={
            "name": "Art",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    tipo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "pattern": r"1|2|3",
        }
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"

    nfse_substituidora: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituidora",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )
    correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class TcValoresDeclaracaoServico:
    class Meta:
        name = "tcValoresDeclaracaoServico"

    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_deducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    outras_retencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    val_tot_tributos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValTotTributos",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    desconto_incondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    desconto_condicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class TcValoresNfse:
    class Meta:
        name = "tcValoresNfse"

    base_calculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


class TsItemListaServico(Enum):
    """
    Tipo Codigo da Lista de Servicos LC 116/2003.
    """
    VALUE_01_01 = "01.01"
    VALUE_01_02 = "01.02"
    VALUE_01_03 = "01.03"
    VALUE_01_04 = "01.04"
    VALUE_01_05 = "01.05"
    VALUE_01_06 = "01.06"
    VALUE_01_07 = "01.07"
    VALUE_01_08 = "01.08"
    VALUE_02_01 = "02.01"
    VALUE_03_02 = "03.02"
    VALUE_03_03 = "03.03"
    VALUE_03_04 = "03.04"
    VALUE_03_05 = "03.05"
    VALUE_04_01 = "04.01"
    VALUE_04_02 = "04.02"
    VALUE_04_03 = "04.03"
    VALUE_04_04 = "04.04"
    VALUE_04_05 = "04.05"
    VALUE_04_06 = "04.06"
    VALUE_04_07 = "04.07"
    VALUE_04_08 = "04.08"
    VALUE_04_09 = "04.09"
    VALUE_04_10 = "04.10"
    VALUE_04_11 = "04.11"
    VALUE_04_12 = "04.12"
    VALUE_04_13 = "04.13"
    VALUE_04_14 = "04.14"
    VALUE_04_15 = "04.15"
    VALUE_04_16 = "04.16"
    VALUE_04_17 = "04.17"
    VALUE_04_18 = "04.18"
    VALUE_04_19 = "04.19"
    VALUE_04_20 = "04.20"
    VALUE_04_21 = "04.21"
    VALUE_04_22 = "04.22"
    VALUE_04_23 = "04.23"
    VALUE_05_01 = "05.01"
    VALUE_05_02 = "05.02"
    VALUE_05_03 = "05.03"
    VALUE_05_04 = "05.04"
    VALUE_05_05 = "05.05"
    VALUE_05_06 = "05.06"
    VALUE_05_07 = "05.07"
    VALUE_05_08 = "05.08"
    VALUE_05_09 = "05.09"
    VALUE_06_01 = "06.01"
    VALUE_06_02 = "06.02"
    VALUE_06_03 = "06.03"
    VALUE_06_04 = "06.04"
    VALUE_06_05 = "06.05"
    VALUE_07_01 = "07.01"
    VALUE_07_02 = "07.02"
    VALUE_07_03 = "07.03"
    VALUE_07_04 = "07.04"
    VALUE_07_05 = "07.05"
    VALUE_07_06 = "07.06"
    VALUE_07_07 = "07.07"
    VALUE_07_08 = "07.08"
    VALUE_07_09 = "07.09"
    VALUE_07_10 = "07.10"
    VALUE_07_11 = "07.11"
    VALUE_07_12 = "07.12"
    VALUE_07_13 = "07.13"
    VALUE_07_16 = "07.16"
    VALUE_07_17 = "07.17"
    VALUE_07_18 = "07.18"
    VALUE_07_19 = "07.19"
    VALUE_07_20 = "07.20"
    VALUE_07_21 = "07.21"
    VALUE_07_22 = "07.22"
    VALUE_08_01 = "08.01"
    VALUE_08_02 = "08.02"
    VALUE_09_01 = "09.01"
    VALUE_09_02 = "09.02"
    VALUE_09_03 = "09.03"
    VALUE_10_01 = "10.01"
    VALUE_10_02 = "10.02"
    VALUE_10_03 = "10.03"
    VALUE_10_04 = "10.04"
    VALUE_10_05 = "10.05"
    VALUE_10_06 = "10.06"
    VALUE_10_07 = "10.07"
    VALUE_10_08 = "10.08"
    VALUE_10_09 = "10.09"
    VALUE_10_10 = "10.10"
    VALUE_11_01 = "11.01"
    VALUE_11_02 = "11.02"
    VALUE_11_03 = "11.03"
    VALUE_11_04 = "11.04"
    VALUE_12_01 = "12.01"
    VALUE_12_02 = "12.02"
    VALUE_12_03 = "12.03"
    VALUE_12_04 = "12.04"
    VALUE_12_05 = "12.05"
    VALUE_12_06 = "12.06"
    VALUE_12_07 = "12.07"
    VALUE_12_08 = "12.08"
    VALUE_12_09 = "12.09"
    VALUE_12_10 = "12.10"
    VALUE_12_11 = "12.11"
    VALUE_12_12 = "12.12"
    VALUE_12_13 = "12.13"
    VALUE_12_14 = "12.14"
    VALUE_12_15 = "12.15"
    VALUE_12_16 = "12.16"
    VALUE_12_17 = "12.17"
    VALUE_13_02 = "13.02"
    VALUE_13_03 = "13.03"
    VALUE_13_04 = "13.04"
    VALUE_13_05 = "13.05"
    VALUE_14_01 = "14.01"
    VALUE_14_02 = "14.02"
    VALUE_14_03 = "14.03"
    VALUE_14_04 = "14.04"
    VALUE_14_05 = "14.05"
    VALUE_14_06 = "14.06"
    VALUE_14_07 = "14.07"
    VALUE_14_08 = "14.08"
    VALUE_14_09 = "14.09"
    VALUE_14_10 = "14.10"
    VALUE_14_11 = "14.11"
    VALUE_14_12 = "14.12"
    VALUE_14_13 = "14.13"
    VALUE_15_01 = "15.01"
    VALUE_15_02 = "15.02"
    VALUE_15_03 = "15.03"
    VALUE_15_04 = "15.04"
    VALUE_15_05 = "15.05"
    VALUE_15_06 = "15.06"
    VALUE_15_07 = "15.07"
    VALUE_15_08 = "15.08"
    VALUE_15_09 = "15.09"
    VALUE_15_10 = "15.10"
    VALUE_15_11 = "15.11"
    VALUE_15_12 = "15.12"
    VALUE_15_13 = "15.13"
    VALUE_15_14 = "15.14"
    VALUE_15_15 = "15.15"
    VALUE_15_16 = "15.16"
    VALUE_15_17 = "15.17"
    VALUE_15_18 = "15.18"
    VALUE_16_01 = "16.01"
    VALUE_17_01 = "17.01"
    VALUE_17_02 = "17.02"
    VALUE_17_03 = "17.03"
    VALUE_17_04 = "17.04"
    VALUE_17_05 = "17.05"
    VALUE_17_06 = "17.06"
    VALUE_17_08 = "17.08"
    VALUE_17_09 = "17.09"
    VALUE_17_10 = "17.10"
    VALUE_17_11 = "17.11"
    VALUE_17_12 = "17.12"
    VALUE_17_13 = "17.13"
    VALUE_17_14 = "17.14"
    VALUE_17_15 = "17.15"
    VALUE_17_16 = "17.16"
    VALUE_17_17 = "17.17"
    VALUE_17_18 = "17.18"
    VALUE_17_19 = "17.19"
    VALUE_17_20 = "17.20"
    VALUE_17_21 = "17.21"
    VALUE_17_22 = "17.22"
    VALUE_17_23 = "17.23"
    VALUE_17_24 = "17.24"
    VALUE_18_01 = "18.01"
    VALUE_19_01 = "19.01"
    VALUE_20_01 = "20.01"
    VALUE_20_02 = "20.02"
    VALUE_20_03 = "20.03"
    VALUE_21_01 = "21.01"
    VALUE_22_01 = "22.01"
    VALUE_23_01 = "23.01"
    VALUE_24_01 = "24.01"
    VALUE_25_01 = "25.01"
    VALUE_25_02 = "25.02"
    VALUE_25_03 = "25.03"
    VALUE_25_04 = "25.04"
    VALUE_26_01 = "26.01"
    VALUE_27_01 = "27.01"
    VALUE_28_01 = "28.01"
    VALUE_29_01 = "29.01"
    VALUE_30_01 = "30.01"
    VALUE_31_01 = "31.01"
    VALUE_32_01 = "32.01"
    VALUE_33_01 = "33.01"
    VALUE_34_01 = "34.01"
    VALUE_35_01 = "35.01"
    VALUE_36_01 = "36.01"
    VALUE_37_01 = "37.01"
    VALUE_38_01 = "38.01"
    VALUE_39_01 = "39.01"
    VALUE_40_01 = "40.01"


class TsUf(Enum):
    """UF (

    AC - Acre;
    AL - Alagoas;
    AM - Amazonas;
    AP - Amapa;
    BA - Bahia;
    CE - Ceara;
    DF - Distrito Federal;
    ES - Espirito Santo;
    GO - Goias;
    MA - Maranhao;
    MG - Minas Gerais;
    MS - Mato Grosso do Sul;
    MT - Mato Grosso;
    PA - Para;
    PB - Paraiba;
    PE - Pernambuco;
    PI - Piaui;
    PR - Parana;
    RJ - Rio de Janeiro;
    RN - Rio Grande do Norte;
    RO - Rondonia;
    RR - Roraima;
    RS - Rio Grande do Sul;
    SC - Santa Catarina;
    SE - Sergipe;
    SP - Sao Paulo;
    TO - Tocantins)
    """
    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"


@dataclass
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"

    valores: Optional[TcValoresDeclaracaoServico] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    responsavel_retencao: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponsavelRetencao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "pattern": r"1|2",
        }
    )
    item_lista_servico: Optional[TsItemListaServico] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    codigo_cnae: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "total_digits": 7,
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    codigo_nbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoNbs",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    codigo_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "length": 4,
            "white_space": "collapse",
        }
    )
    exigibilidade_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExigibilidadeISS",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5|6|7",
        }
    )
    municipio_incidencia: Optional[int] = field(
        default=None,
        metadata={
            "name": "MunicipioIncidencia",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "total_digits": 7,
        }
    )
    numero_processo: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroProcesso",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        }
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"

    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 125,
            "white_space": "collapse",
        }
    )
    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "total_digits": 7,
        }
    )
    uf: Optional[TsUf] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    codigo_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "length": 4,
            "white_space": "collapse",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "length": 8,
        }
    )


@dataclass
class TcIdentificacaoConsulente:
    class Meta:
        name = "tcIdentificacaoConsulente"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoIntermediario:
    class Meta:
        name = "tcIdentificacaoIntermediario"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 7,
        }
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"

    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[TsUf] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )


@dataclass
class TcInfRps:
    class Meta:
        name = "tcInfRps"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcMensagemRetornoLote:
    class Meta:
        name = "tcMensagemRetornoLote"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"

    substituicao_nfse: Optional[TcInfSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 2,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "required": True,
            "max_length": 50,
        }
    )


@dataclass
class ConsultarNfseFaixaEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    faixa: Optional["ConsultarNfseFaixaEnvio.Faixa"] = field(
        default=None,
        metadata={
            "name": "Faixa",
            "type": "Element",
            "required": True,
        }
    )
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )

    @dataclass
    class Faixa:
        numero_nfse_inicial: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroNfseInicial",
                "type": "Element",
                "required": True,
                "total_digits": 15,
            }
        )
        numero_nfse_final: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroNfseFinal",
                "type": "Element",
                "total_digits": 15,
            }
        )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ConsultarNfseServicoPrestadoEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "total_digits": 15,
        }
    )
    periodo_emissao: Optional["ConsultarNfseServicoPrestadoEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
        }
    )
    periodo_competencia: Optional["ConsultarNfseServicoPrestadoEnvio.PeriodoCompetencia"] = field(
        default=None,
        metadata={
            "name": "PeriodoCompetencia",
            "type": "Element",
        }
    )
    tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
        }
    )
    intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
        }
    )
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )

    @dataclass
    class PeriodoEmissao:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class PeriodoCompetencia:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class ConsultarNfseServicoTomadoEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consulente: Optional[TcIdentificacaoConsulente] = field(
        default=None,
        metadata={
            "name": "Consulente",
            "type": "Element",
            "required": True,
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "total_digits": 15,
        }
    )
    periodo_emissao: Optional["ConsultarNfseServicoTomadoEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
        }
    )
    periodo_competencia: Optional["ConsultarNfseServicoTomadoEnvio.PeriodoCompetencia"] = field(
        default=None,
        metadata={
            "name": "PeriodoCompetencia",
            "type": "Element",
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
        }
    )
    tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
        }
    )
    intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
        }
    )
    pagina: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pagina",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999999,
        }
    )

    @dataclass
    class PeriodoEmissao:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class PeriodoCompetencia:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        }
    )
    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagem_retorno: List[TcMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcDadosIntermediario:
    class Meta:
        name = "tcDadosIntermediario"

    identificacao_intermediario: Optional[TcIdentificacaoIntermediario] = field(
        default=None,
        metadata={
            "name": "IdentificacaoIntermediario",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 7,
        }
    )


@dataclass
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"

    identificacao_prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    nome_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    nif_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "NifTomador",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 0,
            "max_length": 40,
            "white_space": "collapse",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"

    identificacao_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "pattern": r"1|2|3|4|5",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcInfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcInfDeclaracaoPrestacaoServico"

    rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "name": "Rps",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    intermediario: Optional[TcDadosIntermediario] = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    construcao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    regime_especial_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "pattern": r"1|2|3|4|5|6",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    incentivo_fiscal: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncentivoFiscal",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"

    inf_pedido_cancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcDeclaracaoPrestacaoServico"

    inf_declaracao_prestacao_servico: Optional[TcInfDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "InfDeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    rps: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "Rps",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SubstituirNfseEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    substituicao_nfse: Optional["SubstituirNfseEnvio.SubstituicaoNfse"] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )

    @dataclass
    class SubstituicaoNfse:
        pedido: Optional[TcPedidoCancelamento] = field(
            default=None,
            metadata={
                "name": "Pedido",
                "type": "Element",
                "required": True,
            }
        )
        rps: Optional[TcDeclaracaoPrestacaoServico] = field(
            default=None,
            metadata={
                "name": "Rps",
                "type": "Element",
                "required": True,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "max_length": 255,
            }
        )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
            "pattern": r"[a-zA-Z0-9]{1,9}",
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    nfse_substituida: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "total_digits": 15,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    valores_nfse: Optional[TcValoresNfse] = field(
        default=None,
        metadata={
            "name": "ValoresNfse",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    valor_credito: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    declaracao_prestacao_servico: Optional[TcDeclaracaoPrestacaoServico] = field(
        default=None,
        metadata={
            "name": "DeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        }
    )
    quantidade_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )

    @dataclass
    class ListaRps:
        rps: List[TcDeclaracaoPrestacaoServico] = field(
            default_factory=list,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
                "min_occurs": 1,
            }
        )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class EnviarLoteRpsSincronoEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"

    inf_nfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass
class TcRetCancelamento:
    class Meta:
        name = "tcRetCancelamento"

    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ret_cancelamento: Optional[TcRetCancelamento] = field(
        default=None,
        metadata={
            "name": "RetCancelamento",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )
    nfse_substituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    situacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
            "required": True,
            "pattern": r"1|2|3|4",
        }
    )
    lista_nfse: Optional["ConsultarLoteRpsResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )
    lista_mensagem_retorno_lote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        lista_mensagem_alerta_retorno: Optional[ListaMensagemAlertaRetorno] = field(
            default=None,
            metadata={
                "name": "ListaMensagemAlertaRetorno",
                "type": "Element",
            }
        )


@dataclass
class ConsultarNfseFaixaResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    lista_nfse: Optional["ConsultarNfseFaixaResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    comp_nfse: Optional[CompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfseServicoPrestadoResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    lista_nfse: Optional["ConsultarNfseServicoPrestadoResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class ConsultarNfseServicoTomadoResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    lista_nfse: Optional["ConsultarNfseServicoTomadoResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )
        proxima_pagina: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProximaPagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )


@dataclass
class EnviarLoteRpsSincronoResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        }
    )
    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
        }
    )
    lista_nfse: Optional["EnviarLoteRpsSincronoResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )
    lista_mensagem_retorno_lote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            }
        )
        lista_mensagem_alerta_retorno: Optional[ListaMensagemAlertaRetorno] = field(
            default=None,
            metadata={
                "name": "ListaMensagemAlertaRetorno",
                "type": "Element",
            }
        )


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    lista_nfse: Optional["GerarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: Optional[CompNfse] = field(
            default=None,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "required": True,
            }
        )
        lista_mensagem_alerta_retorno: Optional[ListaMensagemAlertaRetorno] = field(
            default=None,
            metadata={
                "name": "ListaMensagemAlertaRetorno",
                "type": "Element",
            }
        )


@dataclass
class SubstituirNfseResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ret_substituicao: Optional["SubstituirNfseResposta.RetSubstituicao"] = field(
        default=None,
        metadata={
            "name": "RetSubstituicao",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class RetSubstituicao:
        nfse_substituida: Optional["SubstituirNfseResposta.RetSubstituicao.NfseSubstituida"] = field(
            default=None,
            metadata={
                "name": "NfseSubstituida",
                "type": "Element",
                "required": True,
            }
        )
        nfse_substituidora: Optional["SubstituirNfseResposta.RetSubstituicao.NfseSubstituidora"] = field(
            default=None,
            metadata={
                "name": "NfseSubstituidora",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class NfseSubstituida:
            comp_nfse: Optional[CompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                }
            )
            lista_mensagem_alerta_retorno: Optional[ListaMensagemAlertaRetorno] = field(
                default=None,
                metadata={
                    "name": "ListaMensagemAlertaRetorno",
                    "type": "Element",
                }
            )

        @dataclass
        class NfseSubstituidora:
            comp_nfse: Optional[CompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                }
            )
