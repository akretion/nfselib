from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class ArrayOfKeyNameItemString:
    KeyNameItem: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfMgmtDataItemString:
    MgmtDataItem: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfSpkisexpItemBase64Binary:
    class Meta:
        name = "ArrayOfSPKISexpItemBase64Binary"

    SPKISexpItem: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
            "format": "base64",
        },
    )


@dataclass
class ArrayOfX509CrlitemBase64Binary:
    class Meta:
        name = "ArrayOfX509CRLItemBase64Binary"

    X509CRLItem: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
            "format": "base64",
        },
    )


@dataclass
class ArrayOfX509CertificateItemBase64Binary:
    X509CertificateItem: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
            "format": "base64",
        },
    )


@dataclass
class ArrayOfX509SkiitemBase64Binary:
    class Meta:
        name = "ArrayOfX509SKIItemBase64Binary"

    X509SKIItem: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
            "format": "base64",
        },
    )


@dataclass
class ArrayOfX509SubjectNameItemString:
    X509SubjectNameItem: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfXpathItemString:
    class Meta:
        name = "ArrayOfXPathItemString"

    XPathItem: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class CanonicalizationMethodType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarNfsePorRpsResult: Optional["ConsultarNfseRpsResposta"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DsakeyValueType:
    class Meta:
        name = "DSAKeyValueType"

    P: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "format": "base64",
        },
    )
    Q: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "format": "base64",
        },
    )
    G: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "format": "base64",
        },
    )
    Y: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "format": "base64",
        },
    )
    J: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "format": "base64",
        },
    )
    Seed: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "format": "base64",
        },
    )
    PgenCounter: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "format": "base64",
        },
    )


@dataclass
class DigestMethodType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DigestValue:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )


@dataclass
class KeyName:
    class Meta:
        nillable = True
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    value: Optional[str] = field(
        default="",
        metadata={
            "nillable": True,
        },
    )


@dataclass
class MgmtData:
    class Meta:
        nillable = True
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    value: Optional[str] = field(
        default="",
        metadata={
            "nillable": True,
        },
    )


@dataclass
class ObjectType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
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


@dataclass
class PgpdataType:
    class Meta:
        name = "PGPDataType"

    PGPKeyID: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "format": "base64",
        },
    )
    PGPKeyPacket: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "max_occurs": 2,
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

    Modulus: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "format": "base64",
        },
    )
    Exponent: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "format": "base64",
        },
    )


@dataclass
class SpkidataType:
    class Meta:
        name = "SPKIDataType"

    SPKISexp: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_occurs": 1,
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
class SignatureMethodType:
    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                },
            ),
        },
    )


@dataclass
class SignatureValueType:
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
class Test:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class TestResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    TestResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TransformType:
    Algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                    "nillable": True,
                },
            ),
        },
    )


@dataclass
class X509IssuerSerialType:
    X509IssuerName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    X509SerialNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 11,
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 80,
        },
    )


@dataclass
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"

    Cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 11,
            "max_length": 11,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 14,
            "max_length": 14,
        },
    )


@dataclass
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"

    CodigoObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
        },
    )
    Art: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
        },
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"

    Endereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 125,
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 10,
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 2,
            "max_length": 2,
        },
    )
    Cep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": 0,
        },
    )
    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 14,
            "max_length": 14,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"

    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 14,
            "max_length": 14,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
        },
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": 0,
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    Tipo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": "-128",
            "max_inclusive": "127",
            "pattern": r"1|2|3",
        },
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"

    NfseSubstituidora: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": 0,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"

    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
        },
    )
    Correcao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 200,
        },
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"

    ValorServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    ValorDeducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    ValorPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    ValorInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    ValorIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    ValorCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    IssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": "-128",
            "max_inclusive": "127",
            "pattern": r"1|2",
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    ValorIssRetido: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    OutrasRetencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    BaseCalculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    ValorLiquidoNfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    DescontoIncondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    DescontoCondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )


@dataclass
class ArrayOfMensagemRetornotcMensagemRetorno:
    MensagemRetorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfObjectTypeObjectType:
    ObjectType: List[ObjectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfPgpdataTypePgpdataType:
    class Meta:
        name = "ArrayOfPGPDataTypePGPDataType"

    PGPDataType: List[PgpdataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfSpkidataTypeSpkidataType:
    class Meta:
        name = "ArrayOfSPKIDataTypeSPKIDataType"

    SPKIDataType: List[SpkidataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfTransformTypeTransformType:
    transformType: List[TransformType] = field(
        default_factory=list,
        metadata={
            "name": "TransformType",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfX509IssuerSerialTypeX509IssuerSerialType:
    X509IssuerSerialType: List[X509IssuerSerialType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class ConsultarNfsePorRpsSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarNfsePorRpsSoapConsultarNfsePorRpsOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseRpsResposta: Optional[ConsultarNfseRpsResposta] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "ConsultarNfsePorRpsSoapConsultarNfsePorRpsOutput.Body.Fault"
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
class ConsultarNfsePorRpsSoapTestInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarNfsePorRpsSoapTestInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        Test: Optional[Test] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class ConsultarNfsePorRpsSoapTestOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarNfsePorRpsSoapTestOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        TestResponse: Optional[TestResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional["ConsultarNfsePorRpsSoapTestOutput.Body.Fault"] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
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
class ConsultarNfseRpsEnvio:
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )


@dataclass
class DsakeyValue(DsakeyValueType):
    class Meta:
        name = "DSAKeyValue"
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class DigestMethod(DigestMethodType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class _Object(ObjectType):
    class Meta:
        name = "Object"
        nillable = True
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class Pgpdata(PgpdataType):
    class Meta:
        name = "PGPData"
        nillable = True
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class RsakeyValue(RsakeyValueType):
    class Meta:
        name = "RSAKeyValue"
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class Spkidata(SpkidataType):
    class Meta:
        name = "SPKIData"
        nillable = True
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class SignatureMethod(SignatureMethodType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class SignatureValue(SignatureValueType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class Transform(TransformType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class X509DataType:
    X509IssuerSerial: List[X509IssuerSerialType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )
    X509SKI: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
            "format": "base64",
        },
    )
    X509SubjectName: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )
    X509Certificate: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
            "format": "base64",
        },
    )
    X509CRL: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
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
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"

    IdentificacaoPrestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 115,
        },
    )
    NomeFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 60,
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"

    Valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    ItemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    CodigoCnae: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )
    CodigoTributacaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 20,
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": -2147483648,
            "max_inclusive": 2147483647,
        },
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"

    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 115,
        },
    )
    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
        },
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"

    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
        },
    )


@dataclass
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"

    IdentificacaoNfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    CodigoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class ArrayOfX509DataTypeX509DataType:
    X509DataType: List[X509DataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarNfseRpsEnvio: Optional[ConsultarNfseRpsEnvio] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class ConsultarNfsePorRpsSoapTest:
    style = "document"
    location = (
        "http://www.tinus.com.br/csp/ipojuca/WSNFSE.ConsultarNfsePorRps.cls"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.abrasf.org.br/nfse.xsd/WSNFSE.ConsultarNfsePorRps.Test"
    )
    input = ConsultarNfsePorRpsSoapTestInput
    output = ConsultarNfsePorRpsSoapTestOutput


@dataclass
class KeyValueType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "DSAKeyValue",
                    "type": DsakeyValue,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                },
                {
                    "name": "RSAKeyValue",
                    "type": RsakeyValue,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                },
            ),
        },
    )


@dataclass
class ListaMensagemRetorno(ArrayOfMensagemRetornotcMensagemRetorno):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class TransformsType:
    transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class X509Data(X509DataType):
    class Meta:
        nillable = True
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    IdentificacaoTomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 115,
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )


@dataclass
class ArrayOfKeyValueTypeKeyValueType:
    KeyValueType: List[KeyValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNfsePorRpsSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarNfsePorRpsSoapConsultarNfsePorRpsInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfsePorRps: Optional[ConsultarNfsePorRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class KeyValue(KeyValueType):
    class Meta:
        nillable = True
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class Transforms(TransformsType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": 0,
        },
    )
    CodigoVerificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 9,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    DataEmissaoRps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    NaturezaOperacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": "-128",
            "max_inclusive": "127",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    RegimeEspecialTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": "-128",
            "max_inclusive": "127",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": "-128",
            "max_inclusive": "127",
            "pattern": r"1|2",
        },
    )
    IncentivadorCultural: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_inclusive": "-128",
            "max_inclusive": "127",
            "pattern": r"1|2",
        },
    )
    Competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    NfseSubstituida: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": 0,
        },
    )
    OutrasInformacoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 255,
        },
    )
    Servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    ValorCredito: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    PrestadorServico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    TomadorServico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
    )
    OrgaoGerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    ContrucaoCivil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


class ConsultarNfsePorRpsSoapConsultarNfsePorRps:
    style = "document"
    location = (
        "http://www.tinus.com.br/csp/ipojuca/WSNFSE.ConsultarNfsePorRps.cls"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/WSNFSE.ConsultarNfsePorRps.ConsultarNfsePorRps"
    input = ConsultarNfsePorRpsSoapConsultarNfsePorRpsInput
    output = ConsultarNfsePorRpsSoapConsultarNfsePorRpsOutput


@dataclass
class ReferenceType:
    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    digestMethod: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    digestValue: Optional[DigestValue] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
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
    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
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
class ArrayOfReferenceTypeReferenceType:
    ReferenceType: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRetrievalMethodTypeRetrievalMethodType:
    RetrievalMethodType: List[RetrievalMethodType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class Reference(ReferenceType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class RetrievalMethod(RetrievalMethodType):
    class Meta:
        nillable = True
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class KeyInfoType:
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
                    "name": "KeyName",
                    "type": KeyName,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                    "nillable": True,
                },
                {
                    "name": "KeyValue",
                    "type": KeyValue,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                    "nillable": True,
                },
                {
                    "name": "RetrievalMethod",
                    "type": RetrievalMethod,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                    "nillable": True,
                },
                {
                    "name": "X509Data",
                    "type": X509Data,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                    "nillable": True,
                },
                {
                    "name": "PGPData",
                    "type": Pgpdata,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                    "nillable": True,
                },
                {
                    "name": "SPKIData",
                    "type": Spkidata,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                    "nillable": True,
                },
                {
                    "name": "MgmtData",
                    "type": MgmtData,
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                    "nillable": True,
                },
            ),
        },
    )


@dataclass
class SignedInfoType:
    canonicalizationMethod: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    signatureMethod: Optional[SignatureMethod] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_occurs": 1,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class KeyInfo(KeyInfoType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class SignedInfo(SignedInfoType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class SignatureType:
    signedInfo: Optional[SignedInfo] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    signatureValue: Optional[SignatureValue] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    keyInfo: Optional[KeyInfo] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    Object: List[_Object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ArrayOfSignatureTypeSignatureType:
    SignatureType: List[SignatureType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class Signature(SignatureType):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"

    InfNfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_occurs": 1,
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"

    InfPedidoCancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )


@dataclass
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"

    SubstituicaoNfse: Optional[TcInfSubstituicaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    DataHoraCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcNfseCancelamentoNfse:
    class Meta:
        name = "tcNfseCancelamentoNfse"

    Confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    nfseCancelamento: Optional[TcNfseCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
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
        },
    )
    nfseCancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    nfseSubstituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )


@dataclass
class ConsultarNfseRpsResposta1:
    class Meta:
        name = "ConsultarNfseRpsResposta"

    compNfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )
