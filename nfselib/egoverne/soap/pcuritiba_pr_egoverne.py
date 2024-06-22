from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef, List, Optional

from xsdata.models.datatype import XmlDateTime


@dataclass
class CanonicalizationMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DsakeyValueType:
    class Meta:
        name = "DSAKeyValueType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    P: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    Q: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    G: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    Y: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    J: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    Seed: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    PgenCounter: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )


@dataclass
class DigestMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class ObjectType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    MimeType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Encoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class PgpdataType:
    class Meta:
        name = "PGPDataType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    PGPKeyPacket: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    PGPKeyID: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class RsakeyValueType:
    class Meta:
        name = "RSAKeyValueType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    Modulus: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    Exponent: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )


@dataclass
class SpkidataType:
    class Meta:
        name = "SPKIDataType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    SPKISexp: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SignatureMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
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
        },
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
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TransformType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
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
        },
    )


@dataclass
class X509IssuerSerialType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    X509IssuerName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    X509SerialNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class RecepcionarXml:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    metodo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarXmlResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    RecepcionarXmlResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ValidarXml:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"
        target_namespace = "https://www.e-governeapps2.com.br/"

    CodigoObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Art: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Endereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Cep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"
        target_namespace = "https://www.e-governeapps2.com.br/"

    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Tipo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"
        target_namespace = "https://www.e-governeapps2.com.br/"

    NfseSubstituidora: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )


@dataclass
class TcLoteCancelamentoRps:
    class Meta:
        name = "tcLoteCancelamentoRps"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Correcao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcPeriodoEmissao:
    class Meta:
        name = "tcPeriodoEmissao"
        target_namespace = "https://www.e-governeapps2.com.br/"

    DataInicial: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    DataFinal: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"
        target_namespace = "https://www.e-governeapps2.com.br/"

    ValorServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    NumeroDeducao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorDeducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    IssRetido: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorIssRetido: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    OutrasRetencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    BaseCalculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ValorLiquidoNfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    DescontoIncondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    DescontoCondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
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
        },
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
        },
    )


@dataclass
class X509DataType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    X509Certificate: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    X509IssuerSerial: List[X509IssuerSerialType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    X509SKI: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    X509SubjectName: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    X509CRL: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ArrayOfTcMensagemRetorno:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    tcMensagemRetorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class MensagemRetorno(TcMensagemRetorno):
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"


@dataclass
class WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarXml: Optional[RecepcionarXml] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarXmlResponse: Optional[RecepcionarXmlResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapValidarXmlInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional["WsX0020X0020NfsEX0020V1001SoapValidarXmlInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ValidarXml: Optional[ValidarXml] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"
        target_namespace = "https://www.e-governeapps2.com.br/"

    IdentificacaoPrestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    NomeFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    ItemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    CodigoCnae: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    CodigoTributacaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"
        target_namespace = "https://www.e-governeapps2.com.br/"

    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"
        target_namespace = "https://www.e-governeapps2.com.br/"

    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"
        target_namespace = "https://www.e-governeapps2.com.br/"

    IdentificacaoNfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    CodigoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
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
        },
    )
    digestMethod: Optional[DigestMethodType] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    digestValue: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
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
        },
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class ArrayOfMensagemRetorno:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    MensagemRetorno: List[MensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ConsultarLoteRpsEnvio: Optional[ConsultarLoteRpsEnvio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseEnvio:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    NumeroNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    PeriodoEmissao: Optional[TcPeriodoEmissao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ConsultarNfseRpsEnvio: Optional[ConsultarNfseRpsEnvio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRps:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ConsultarSituacaoLoteRpsEnvio: Optional[ConsultarSituacaoLoteRpsEnvio] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    MensagemRetorno: Optional[ArrayOfTcMensagemRetorno] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


class WsX0020X0020NfsEX0020V1001SoapRecepcionarXml:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/RecepcionarXml"
    input = WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlInput
    output = WsX0020X0020NfsEX0020V1001SoapRecepcionarXmlOutput


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"
        target_namespace = "https://www.e-governeapps2.com.br/"

    IdentificacaoTomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class KeyInfoType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "PGPData",
                    "type": PgpdataType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyName",
                    "type": ForwardRef("KeyInfoType.KeyName"),
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyValue",
                    "type": KeyValueType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "MgmtData",
                    "type": ForwardRef("KeyInfoType.MgmtData"),
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RetrievalMethod",
                    "type": RetrievalMethodType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "SPKIData",
                    "type": SpkidataType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "X509Data",
                    "type": X509DataType,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        },
    )

    @dataclass
    class KeyName:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class MgmtData:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class SignedInfoType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    canonicalizationMethod: Optional[CanonicalizationMethodType] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    signatureMethod: Optional[SignatureMethodType] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CancelarLoteNfseResposta:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    DataRecebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    listaMensagemRetorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class CancelarLoteRpsResposta:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    DataRecebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    listaMensagemRetorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class ConsultarNfse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ConsultarNfseEnvio: Optional[ConsultarNfseEnvio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    Situacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    listaMensagemRetorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    DataRecebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    listaMensagemRetorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class ValidarXmlResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ValidarXmlResult: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRps: Optional[ConsultarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRps: Optional[ConsultarNfsePorRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRps: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    DataEmissaoRps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    NaturezaOperacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    RegimeEspecialTributacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    OptanteSimplesNacional: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    IncentivadorCultural: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    Competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    NfseSubstituida: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    ValorCredito: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    ContrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcInfRps:
    class Meta:
        name = "tcInfRps"
        target_namespace = "https://www.e-governeapps2.com.br/"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    NaturezaOperacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    RegimeEspecialTributacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )
    OptanteSimplesNacional: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    IncentivadorCultural: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    Status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    RpsSubstituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    Tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
    )
    ContrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class SignatureType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    signedInfo: Optional[SignedInfoType] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    signatureValue: Optional[SignatureValueType] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    keyInfo: Optional[KeyInfoType] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    Object: List[ObjectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CancelarLoteNfseResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    CancelarLoteNfseResult: Optional[CancelarLoteNfseResposta] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarLoteRpsResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    CancelarLoteRpsResult: Optional[CancelarLoteRpsResposta] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ConsultarSituacaoLoteRpsResult: Optional[
        ConsultarSituacaoLoteRpsResposta
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    RecepcionarLoteRpsResult: Optional[EnviarLoteRpsResposta] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional["WsX0020X0020NfsEX0020V1001SoapConsultarNfseInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfse: Optional[ConsultarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapValidarXmlOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional["WsX0020X0020NfsEX0020V1001SoapValidarXmlOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ValidarXmlResponse: Optional[ValidarXmlResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapValidarXmlOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class CancelarLoteRpsEnvio:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    LoteRps: Optional[TcLoteCancelamentoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarLoteNfseResponse: Optional[CancelarLoteNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarLoteRpsResponse: Optional[CancelarLoteRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsResponse: Optional[
            ConsultarSituacaoLoteRpsResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsResponse: Optional[RecepcionarLoteRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "https://www.e-governeapps2.com.br/",
                },
            )
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


class WsX0020X0020NfsEX0020V1001SoapValidarXml:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/ValidarXml"
    input = WsX0020X0020NfsEX0020V1001SoapValidarXmlInput
    output = WsX0020X0020NfsEX0020V1001SoapValidarXmlOutput


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"
        target_namespace = "https://www.e-governeapps2.com.br/"

    InfNfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"
        target_namespace = "https://www.e-governeapps2.com.br/"

    InfPedidoCancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcRps:
    class Meta:
        name = "tcRps"
        target_namespace = "https://www.e-governeapps2.com.br/"

    InfRps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"
        target_namespace = "https://www.e-governeapps2.com.br/"

    SubstituicaoNfse: Optional[TcInfSubstituicaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class CancelarLoteRps:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    CancelarLoteRpsEnvio: Optional[CancelarLoteRpsEnvio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class PedidoCancelamento(TcPedidoCancelamento):
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"


@dataclass
class Rps(TcRps):
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"


class WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRps:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/ConsultarSituacaoLoteRps"
    input = WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapConsultarSituacaoLoteRpsOutput


@dataclass
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    DataHoraCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )


@dataclass
class ArrayOfPedidoCancelamento:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    PedidoCancelamento: List[PedidoCancelamento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRps:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    Rps: List[Rps] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    CancelarNfseEnvio: Optional[CancelarNfseEnvio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarLoteRps: Optional[CancelarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    Cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    listaMensagemRetorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class LoteCancelamento:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    PedidosCancelamento: Optional[ArrayOfPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


class WsX0020X0020NfsEX0020V1001SoapCancelarLoteRps:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/CancelarLoteRps"
    input = WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapCancelarLoteRpsOutput


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarNfseInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        CancelarNfse: Optional[CancelarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"
        target_namespace = "https://www.e-governeapps2.com.br/"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    nfseCancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    nfseSubstituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"
        target_namespace = "https://www.e-governeapps2.com.br/"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    QuantidadeRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "required": True,
        },
    )
    ListaRps: Optional[ArrayOfRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class ArrayOfTcCompNfse:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    tcCompNfse: List[TcCompNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
            "nillable": True,
        },
    )


@dataclass
class CancelarLoteNfseEnvio:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    LoteCancelamento: Optional[LoteCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    CancelarNfseResult: Optional[CancelarNfseResposta] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    compNfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    listaMensagemRetorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    LoteRps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class CancelarLoteNfse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    CancelarLoteNfseEnvio: Optional[CancelarLoteNfseEnvio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ConsultarNfsePorRpsResult: Optional[ConsultarNfseRpsResposta] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ListaNfse:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    compNfse: Optional[ArrayOfTcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    EnviarLoteRpsEnvio: Optional[EnviarLoteRpsEnvio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional["WsX0020X0020NfsEX0020V1001SoapCancelarNfseOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        CancelarNfseResponse: Optional[CancelarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapCancelarNfseOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    ListaNfse: Optional[ListaNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    listaMensagemRetorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class ConsultarNfseResposta:
    class Meta:
        target_namespace = "https://www.e-governeapps2.com.br/"

    ListaNfse: Optional[ListaNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )
    listaMensagemRetorno: Optional[ArrayOfMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "https://www.e-governeapps2.com.br/",
        },
    )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarLoteNfse: Optional[CancelarLoteNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


class WsX0020X0020NfsEX0020V1001SoapCancelarNfse:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/CancelarNfse"
    input = WsX0020X0020NfsEX0020V1001SoapCancelarNfseInput
    output = WsX0020X0020NfsEX0020V1001SoapCancelarNfseOutput


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsResponse: Optional[ConsultarNfsePorRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "https://www.e-governeapps2.com.br/",
                },
            )
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRps: Optional[RecepcionarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ConsultarLoteRpsResult: Optional[ConsultarLoteRpsResposta] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "https://www.e-governeapps2.com.br/"

    ConsultarNfseResult: Optional[ConsultarNfseResposta] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfse:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/CancelarLoteNfse"
    input = WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseInput
    output = WsX0020X0020NfsEX0020V1001SoapCancelarLoteNfseOutput


class WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRps:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/ConsultarNfsePorRps"
    input = WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapConsultarNfsePorRpsOutput


class WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRps:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/RecepcionarLoteRps"
    input = WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapRecepcionarLoteRpsOutput


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsResponse: Optional[ConsultarLoteRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsX0020X0020NfsEX0020V1001SoapConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "https://www.e-governeapps2.com.br/"

    Body: Optional[
        "WsX0020X0020NfsEX0020V1001SoapConsultarNfseOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseResponse: Optional[ConsultarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://www.e-governeapps2.com.br/",
            },
        )
        Fault: Optional[
            "WsX0020X0020NfsEX0020V1001SoapConsultarNfseOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


class WsX0020X0020NfsEX0020V1001SoapConsultarLoteRps:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/ConsultarLoteRps"
    input = WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsInput
    output = WsX0020X0020NfsEX0020V1001SoapConsultarLoteRpsOutput


class WsX0020X0020NfsEX0020V1001SoapConsultarNfse:
    style = "document"
    location = "https://srv2-isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.e-governeapps2.com.br/ConsultarNfse"
    input = WsX0020X0020NfsEX0020V1001SoapConsultarNfseInput
    output = WsX0020X0020NfsEX0020V1001SoapConsultarNfseOutput
