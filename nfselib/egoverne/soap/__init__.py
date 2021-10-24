from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
class RecepcionarXml:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    metodo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RecepcionarXmlResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    recepcionar_xml_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecepcionarXmlResult",
            "type": "Element",
        }
    )


@dataclass
class ValidarXml:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"
        target_namespace = "http://www.e-governeapps2.com.br/"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"
        target_namespace = "http://www.e-governeapps2.com.br/"

    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"
        target_namespace = "http://www.e-governeapps2.com.br/"

    codigo_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoObra",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    art: Optional[str] = field(
        default=None,
        metadata={
            "name": "Art",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"
        target_namespace = "http://www.e-governeapps2.com.br/"

    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"
        target_namespace = "http://www.e-governeapps2.com.br/"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"
        target_namespace = "http://www.e-governeapps2.com.br/"

    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"
        target_namespace = "http://www.e-governeapps2.com.br/"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"
        target_namespace = "http://www.e-governeapps2.com.br/"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    tipo: Optional[int] = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"
        target_namespace = "http://www.e-governeapps2.com.br/"

    nfse_substituidora: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituidora",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )


@dataclass
class TcLoteCancelamentoRps:
    class Meta:
        name = "tcLoteCancelamentoRps"
        target_namespace = "http://www.e-governeapps2.com.br/"

    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"
        target_namespace = "http://www.e-governeapps2.com.br/"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcPeriodoEmissao:
    class Meta:
        name = "tcPeriodoEmissao"
        target_namespace = "http://www.e-governeapps2.com.br/"

    data_inicial: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataInicial",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    data_final: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataFinal",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"
        target_namespace = "http://www.e-governeapps2.com.br/"

    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    numero_deducao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroDeducao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_deducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    iss_retido: Optional[int] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_iss_retido: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIssRetido",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    outras_retencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    base_calculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    desconto_incondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    desconto_condicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )


@dataclass
class CanonicalizationMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class DsakeyValueType:
    class Meta:
        name = "DSAKeyValueType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    p: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    q: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Q",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    g: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "G",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    y: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    j: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "J",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    seed: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Seed",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    pgen_counter: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PgenCounter",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )


@dataclass
class DigestMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class ObjectType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Attribute",
        }
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class PgpdataType:
    class Meta:
        name = "PGPDataType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    pgpkey_packet: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "PGPKeyPacket",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    pgpkey_id: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "PGPKeyID",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "sequential": True,
        }
    )


@dataclass
class RsakeyValueType:
    class Meta:
        name = "RSAKeyValueType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    modulus: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Modulus",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    exponent: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Exponent",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )


@dataclass
class SpkidataType:
    class Meta:
        name = "SPKIDataType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    spkisexp: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SPKISexp",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class SignatureMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "HMACOutputLength",
                    "type": int,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class SignatureValueType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TransformType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "XPath",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class X509IssuerSerialType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    x509_issuer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509IssuerName",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    x509_serial_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "X509SerialNumber",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class ArrayOfTcMensagemRetorno:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    tc_mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "tcMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class MensagemRetorno(TcMensagemRetorno):
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"


@dataclass
class WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_xml: Optional[RecepcionarXml] = field(
            default=None,
            metadata={
                "name": "RecepcionarXml",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_xml_response: Optional[RecepcionarXmlResponse] = field(
            default=None,
            metadata={
                "name": "RecepcionarXmlResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapValidarXmlInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapValidarXmlInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        validar_xml: Optional[ValidarXml] = field(
            default=None,
            metadata={
                "name": "ValidarXml",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"
        target_namespace = "http://www.e-governeapps2.com.br/"

    identificacao_prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    nome_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"
        target_namespace = "http://www.e-governeapps2.com.br/"

    valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    codigo_cnae: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"
        target_namespace = "http://www.e-governeapps2.com.br/"

    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"
        target_namespace = "http://www.e-governeapps2.com.br/"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"
        target_namespace = "http://www.e-governeapps2.com.br/"

    identificacao_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ArrayOfTransformType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transform: List[TransformType] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class KeyValueType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "DSAKeyValue",
                    "type": DsakeyValueType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RSAKeyValue",
                    "type": RsakeyValueType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class X509DataType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    x509_crl: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509CRL",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    x509_certificate: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    x509_issuer_serial: List[X509IssuerSerialType] = field(
        default_factory=list,
        metadata={
            "name": "X509IssuerSerial",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
        }
    )
    x509_ski: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509SKI",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    x509_subject_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "X509SubjectName",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "sequential": True,
        }
    )


@dataclass
class ArrayOfMensagemRetorno:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    mensagem_retorno: List[MensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    consultar_lote_rps_envio: Optional[ConsultarLoteRpsEnvio] = field(
        default=None,
        metadata={
            "name": "ConsultarLoteRpsEnvio",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfseEnvio:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    periodo_emissao: Optional[TcPeriodoEmissao] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    consultar_nfse_rps_envio: Optional[ConsultarNfseRpsEnvio] = field(
        default=None,
        metadata={
            "name": "ConsultarNfseRpsEnvio",
            "type": "Element",
        }
    )


@dataclass
class ConsultarSituacaoLoteRps:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    consultar_situacao_lote_rps_envio: Optional[ConsultarSituacaoLoteRpsEnvio] = field(
        default=None,
        metadata={
            "name": "ConsultarSituacaoLoteRpsEnvio",
            "type": "Element",
        }
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    mensagem_retorno: Optional[ArrayOfTcMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


class WsX0020X0020NfsEX0020V1001SoapRecepcionarXml:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/RecepcionarXml"
    input = WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlInput
    output = WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlOutput


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"
        target_namespace = "http://www.e-governeapps2.com.br/"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ReferenceType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transforms: Optional[ArrayOfTransformType] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    digest_method: Optional[DigestMethodType] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    digest_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class RetrievalMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transforms: Optional[ArrayOfTransformType] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class CancelarLoteNfseResposta:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    lista_mensagem_retorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class CancelarLoteRpsResposta:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    lista_mensagem_retorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ConsultarNfse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    consultar_nfse_envio: Optional[ConsultarNfseEnvio] = field(
        default=None,
        metadata={
            "name": "ConsultarNfseEnvio",
            "type": "Element",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    situacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    lista_mensagem_retorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    lista_mensagem_retorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ValidarXmlResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    validar_xml_result: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ValidarXmlResult",
            "type": "Element",
        }
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps: Optional[ConsultarLoteRps] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRps",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rps: Optional[ConsultarNfsePorRps] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorRps",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRps",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"
        target_namespace = "http://www.e-governeapps2.com.br/"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    data_emissao_rps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    regime_especial_tributacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    optante_simples_nacional: Optional[int] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    incentivador_cultural: Optional[int] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    nfse_substituida: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    valor_credito: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcInfRps:
    class Meta:
        name = "tcInfRps"
        target_namespace = "http://www.e-governeapps2.com.br/"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    regime_especial_tributacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )
    optante_simples_nacional: Optional[int] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    incentivador_cultural: Optional[int] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class KeyInfoType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "SPKIData",
                    "type": SpkidataType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "PGPData",
                    "type": PgpdataType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyName",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyValue",
                    "type": KeyValueType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "MgmtData",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RetrievalMethod",
                    "type": RetrievalMethodType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "X509Data",
                    "type": X509DataType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class SignedInfoType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    canonicalization_method: Optional[CanonicalizationMethodType] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    signature_method: Optional[SignatureMethodType] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class CancelarLoteNfseResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    cancelar_lote_nfse_result: Optional[CancelarLoteNfseResposta] = field(
        default=None,
        metadata={
            "name": "CancelarLoteNfseResult",
            "type": "Element",
        }
    )


@dataclass
class CancelarLoteRpsResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    cancelar_lote_rps_result: Optional[CancelarLoteRpsResposta] = field(
        default=None,
        metadata={
            "name": "CancelarLoteRpsResult",
            "type": "Element",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    consultar_situacao_lote_rps_result: Optional[ConsultarSituacaoLoteRpsResposta] = field(
        default=None,
        metadata={
            "name": "ConsultarSituacaoLoteRpsResult",
            "type": "Element",
        }
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    recepcionar_lote_rps_result: Optional[EnviarLoteRpsResposta] = field(
        default=None,
        metadata={
            "name": "RecepcionarLoteRpsResult",
            "type": "Element",
        }
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse: Optional[ConsultarNfse] = field(
            default=None,
            metadata={
                "name": "ConsultarNfse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapValidarXmlOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapValidarXmlOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        validar_xml_response: Optional[ValidarXmlResponse] = field(
            default=None,
            metadata={
                "name": "ValidarXmlResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapValidarXmlOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class SignatureType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    signed_info: Optional[SignedInfoType] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    signature_value: Optional[SignatureValueType] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    key_info: Optional[KeyInfoType] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    object_value: List[ObjectType] = field(
        default_factory=list,
        metadata={
            "name": "Object",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class CancelarLoteRpsEnvio:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    lote_rps: Optional[TcLoteCancelamentoRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_lote_nfse_response: Optional[CancelarLoteNfseResponse] = field(
            default=None,
            metadata={
                "name": "CancelarLoteNfseResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_lote_rps_response: Optional[CancelarLoteRpsResponse] = field(
            default=None,
            metadata={
                "name": "CancelarLoteRpsResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps_response: Optional[ConsultarSituacaoLoteRpsResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRpsResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps_response: Optional[RecepcionarLoteRpsResponse] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


class WsX0020X0020NfsEX0020V1001SoapValidarXml:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/ValidarXml"
    input = WsX0020X0020NfsEX0020V1001SoapValidarXmlInput
    output = WsX0020X0020NfsEX0020V1001SoapValidarXmlOutput


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"
        target_namespace = "http://www.e-governeapps2.com.br/"

    inf_nfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"
        target_namespace = "http://www.e-governeapps2.com.br/"

    inf_pedido_cancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcRps:
    class Meta:
        name = "tcRps"
        target_namespace = "http://www.e-governeapps2.com.br/"

    inf_rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "name": "InfRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"
        target_namespace = "http://www.e-governeapps2.com.br/"

    substituicao_nfse: Optional[TcInfSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class CancelarLoteRps:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    cancelar_lote_rps_envio: Optional[CancelarLoteRpsEnvio] = field(
        default=None,
        metadata={
            "name": "CancelarLoteRpsEnvio",
            "type": "Element",
        }
    )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class PedidoCancelamento(TcPedidoCancelamento):
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"


@dataclass
class Rps(TcRps):
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"


class WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRps:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/ConsultarSituacaoLoteRps"
    input = WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsOutput


@dataclass
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"
        target_namespace = "http://www.e-governeapps2.com.br/"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    data_hora_cancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHoraCancelamento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )


@dataclass
class ArrayOfPedidoCancelamento:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    pedido_cancelamento: List[PedidoCancelamento] = field(
        default_factory=list,
        metadata={
            "name": "PedidoCancelamento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )


@dataclass
class ArrayOfRps:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    rps: List[Rps] = field(
        default_factory=list,
        metadata={
            "name": "Rps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    cancelar_nfse_envio: Optional[CancelarNfseEnvio] = field(
        default=None,
        metadata={
            "name": "CancelarNfseEnvio",
            "type": "Element",
        }
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_lote_rps: Optional[CancelarLoteRps] = field(
            default=None,
            metadata={
                "name": "CancelarLoteRps",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"
        target_namespace = "http://www.e-governeapps2.com.br/"

    confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "Cancelamento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    lista_mensagem_retorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class LoteCancelamento:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    pedidos_cancelamento: Optional[ArrayOfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "PedidosCancelamento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


class WsX0020X0020NfsEX0020V1001SoapCancelarLoteRps:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/CancelarLoteRps"
    input = WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsOutput


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse: Optional[CancelarNfse] = field(
            default=None,
            metadata={
                "name": "CancelarNfse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"
        target_namespace = "http://www.e-governeapps2.com.br/"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    nfse_substituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"
        target_namespace = "http://www.e-governeapps2.com.br/"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    quantidade_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "required": True,
        }
    )
    lista_rps: Optional[ArrayOfRps] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ArrayOfTcCompNfse:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    tc_comp_nfse: List[TcCompNfse] = field(
        default_factory=list,
        metadata={
            "name": "tcCompNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
            "nillable": True,
        }
    )


@dataclass
class CancelarLoteNfseEnvio:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    lote_cancelamento: Optional[LoteCancelamento] = field(
        default=None,
        metadata={
            "name": "LoteCancelamento",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    cancelar_nfse_result: Optional[CancelarNfseResposta] = field(
        default=None,
        metadata={
            "name": "CancelarNfseResult",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    comp_nfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    lista_mensagem_retorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class CancelarLoteNfse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    cancelar_lote_nfse_envio: Optional[CancelarLoteNfseEnvio] = field(
        default=None,
        metadata={
            "name": "CancelarLoteNfseEnvio",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    consultar_nfse_por_rps_result: Optional[ConsultarNfseRpsResposta] = field(
        default=None,
        metadata={
            "name": "ConsultarNfsePorRpsResult",
            "type": "Element",
        }
    )


@dataclass
class ListaNfse:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    comp_nfse: Optional[ArrayOfTcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    enviar_lote_rps_envio: Optional[EnviarLoteRpsEnvio] = field(
        default=None,
        metadata={
            "name": "EnviarLoteRpsEnvio",
            "type": "Element",
        }
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse_response: Optional[CancelarNfseResponse] = field(
            default=None,
            metadata={
                "name": "CancelarNfseResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarNfseOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    lista_nfse: Optional[ListaNfse] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    lista_mensagem_retorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class ConsultarNfseResposta:
    class Meta:
        target_namespace = "http://www.e-governeapps2.com.br/"

    lista_nfse: Optional[ListaNfse] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )
    lista_mensagem_retorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.e-governeapps2.com.br/",
        }
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_lote_nfse: Optional[CancelarLoteNfse] = field(
            default=None,
            metadata={
                "name": "CancelarLoteNfse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


class WsX0020X0020NfsEX0020V1001SoapCancelarNfse:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/CancelarNfse"
    input = WsX0020X0020NfsEX0020V1001SoapCancelarNfseInput
    output = WsX0020X0020NfsEX0020V1001SoapCancelarNfseOutput


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rps_response: Optional[ConsultarNfsePorRpsResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorRpsResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps: Optional[RecepcionarLoteRps] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRps",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    consultar_lote_rps_result: Optional[ConsultarLoteRpsResposta] = field(
        default=None,
        metadata={
            "name": "ConsultarLoteRpsResult",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://www.e-governeapps2.com.br/"

    consultar_nfse_result: Optional[ConsultarNfseResposta] = field(
        default=None,
        metadata={
            "name": "ConsultarNfseResult",
            "type": "Element",
        }
    )


class WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfse:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/CancelarLoteNfse"
    input = WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseInput
    output = WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseOutput


class WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRps:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/ConsultarNfsePorRps"
    input = WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsOutput


class WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRps:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/RecepcionarLoteRps"
    input = WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsOutput


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps_response: Optional[ConsultarLoteRpsResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRpsResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.e-governeapps2.com.br/"

    body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_response: Optional[ConsultarNfseResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseResponse",
                "type": "Element",
                "namespace": "http://www.e-governeapps2.com.br/",
            }
        )
        fault: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarNfseOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


class WsX0020X0020NfsEX0020V1001SoapConsultarLoteRps:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/ConsultarLoteRps"
    input = WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsOutput


class WsX0020X0020NfsEX0020V1001SoapConsultarNfse:
    style = "document"
    location = "https://isscuritiba.curitiba.pr.gov.br:8085/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.e-governeapps2.com.br/ConsultarNfse"
    input = WsX0020X0020NfsEX0020V1001SoapConsultarNfseInput
    output = WsX0020X0020NfsEX0020V1001SoapConsultarNfseOutput
