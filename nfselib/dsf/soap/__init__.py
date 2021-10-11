from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class CancelarNfseV3:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    arg1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CancelarNfseV3Response:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarLoteRpsV3:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    arg1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarLoteRpsV3Response:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarNfsePorRpsV3:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    arg1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarNfsePorRpsV3Response:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarNfseV3:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    arg1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarNfseV3Response:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsV3:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    arg1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsV3Response:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RecepcionarLoteRpsV3:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    arg0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    arg1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RecepcionarLoteRpsV3Response:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
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
            "required": True,
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
            "required": True,
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
            "required": True,
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
class DigestValue:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class KeyName:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class MgmtData:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
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
            "required": True,
            "format": "base64",
        }
    )
    exponent: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Exponent",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
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
            "sequential": True,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequential": True,
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
            "required": True,
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
class SignaturePropertyType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Attribute",
            "required": True,
        }
    )
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
            "required": True,
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
            "required": True,
        }
    )
    x509_serial_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "X509SerialNumber",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    versao_dados: Optional[str] = field(
        default=None,
        metadata={
            "name": "versaoDados",
            "type": "Element",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    codigo_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoObra",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    art: Optional[str] = field(
        default=None,
        metadata={
            "name": "Art",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    tipo: Optional[int] = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )


@dataclass
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    nfse_substituidora: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituidora",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
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
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    valor_deducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    valor_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    valor_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    valor_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    valor_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    valor_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    iss_retido: Optional[int] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    valor_iss_retido: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIssRetido",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    outras_retencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    base_calculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    desconto_incondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    desconto_condicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consultar_lote_rps_envio: Optional["ConsultarLoteRps.ConsultarLoteRpsEnvio"] = field(
        default=None,
        metadata={
            "name": "ConsultarLoteRpsEnvio",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ConsultarLoteRpsEnvio:
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
            }
        )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consultar_nfse_rps_envio: Optional["ConsultarNfsePorRps.ConsultarNfseRpsEnvio"] = field(
        default=None,
        metadata={
            "name": "ConsultarNfseRpsEnvio",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ConsultarNfseRpsEnvio:
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
class ConsultarSituacaoLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consultar_situacao_lote_rps_envio: Optional["ConsultarSituacaoLoteRps.ConsultarSituacaoLoteRpsEnvio"] = field(
        default=None,
        metadata={
            "name": "ConsultarSituacaoLoteRpsEnvio",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ConsultarSituacaoLoteRpsEnvio:
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
            }
        )


@dataclass
class NotaFiscalSoapCancelarNfseV3Input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapCancelarNfseV3Input.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse_v3: Optional[CancelarNfseV3] = field(
            default=None,
            metadata={
                "name": "CancelarNfseV3",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class NotaFiscalSoapCancelarNfseV3Output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapCancelarNfseV3Output.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse_v3_response: Optional[CancelarNfseV3Response] = field(
            default=None,
            metadata={
                "name": "CancelarNfseV3Response",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapCancelarNfseV3Output.Body.Fault"] = field(
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
class NotaFiscalSoapConsultarLoteRpsV3Input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarLoteRpsV3Input.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps_v3: Optional[ConsultarLoteRpsV3] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRpsV3",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class NotaFiscalSoapConsultarLoteRpsV3Output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarLoteRpsV3Output.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps_v3_response: Optional[ConsultarLoteRpsV3Response] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRpsV3Response",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapConsultarLoteRpsV3Output.Body.Fault"] = field(
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
class NotaFiscalSoapConsultarNfsePorRpsV3Input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarNfsePorRpsV3Input.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rps_v3: Optional[ConsultarNfsePorRpsV3] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorRpsV3",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class NotaFiscalSoapConsultarNfsePorRpsV3Output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarNfsePorRpsV3Output.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rps_v3_response: Optional[ConsultarNfsePorRpsV3Response] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorRpsV3Response",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapConsultarNfsePorRpsV3Output.Body.Fault"] = field(
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
class NotaFiscalSoapConsultarNfseV3Input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarNfseV3Input.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_v3: Optional[ConsultarNfseV3] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseV3",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class NotaFiscalSoapConsultarNfseV3Output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarNfseV3Output.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_v3_response: Optional[ConsultarNfseV3Response] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseV3Response",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapConsultarNfseV3Output.Body.Fault"] = field(
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
class NotaFiscalSoapConsultarSituacaoLoteRpsV3Input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarSituacaoLoteRpsV3Input.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps_v3: Optional[ConsultarSituacaoLoteRpsV3] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRpsV3",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class NotaFiscalSoapConsultarSituacaoLoteRpsV3Output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarSituacaoLoteRpsV3Output.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps_v3_response: Optional[ConsultarSituacaoLoteRpsV3Response] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRpsV3Response",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapConsultarSituacaoLoteRpsV3Output.Body.Fault"] = field(
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
class NotaFiscalSoapRecepcionarLoteRpsV3Input:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapRecepcionarLoteRpsV3Input.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps_v3: Optional[RecepcionarLoteRpsV3] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsV3",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class NotaFiscalSoapRecepcionarLoteRpsV3Output:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapRecepcionarLoteRpsV3Output.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps_v3_response: Optional[RecepcionarLoteRpsV3Response] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsV3Response",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapRecepcionarLoteRpsV3Output.Body.Fault"] = field(
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
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DsakeyValue(DsakeyValueType):
    class Meta:
        name = "DSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DigestMethod(DigestMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Object(ObjectType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Pgpdata(PgpdataType):
    class Meta:
        name = "PGPData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class RsakeyValue(RsakeyValueType):
    class Meta:
        name = "RSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Spkidata(SpkidataType):
    class Meta:
        name = "SPKIData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureMethod(SignatureMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignaturePropertiesType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    signature_property: List[SignaturePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "SignatureProperty",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
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
class SignatureProperty(SignaturePropertyType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureValue(SignatureValueType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Transform(TransformType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class TransformsType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transform: List[TransformType] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )


@dataclass
class X509DataType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

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
    x509_issuer_serial: List[X509IssuerSerialType] = field(
        default_factory=list,
        metadata={
            "name": "X509IssuerSerial",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
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
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequential": True,
        }
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

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
        }
    )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

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
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

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
        }
    )


@dataclass
class ListaMensagemRetorno:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    identificacao_prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoPrestador",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    nome_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    codigo_cnae: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    identificacao_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
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
class TcMensagemRetornoLote:
    class Meta:
        name = "tcMensagemRetornoLote"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )


@dataclass
class ConsultarNfse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consultar_nfse_envio: Optional["ConsultarNfse.ConsultarNfseEnvio"] = field(
        default=None,
        metadata={
            "name": "ConsultarNfseEnvio",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ConsultarNfseEnvio:
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
            }
        )
        periodo_emissao: Optional["ConsultarNfse.ConsultarNfseEnvio.PeriodoEmissao"] = field(
            default=None,
            metadata={
                "name": "PeriodoEmissao",
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
        intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
            default=None,
            metadata={
                "name": "IntermediarioServico",
                "type": "Element",
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
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consultar_situacao_lote_rps_resposta: Optional["ConsultarSituacaoLoteRpsResponse.ConsultarSituacaoLoteRpsResposta"] = field(
        default=None,
        metadata={
            "name": "ConsultarSituacaoLoteRpsResposta",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ConsultarSituacaoLoteRpsResposta:
        numero_lote: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroLote",
                "type": "Element",
            }
        )
        situacao: Optional[int] = field(
            default=None,
            metadata={
                "name": "Situacao",
                "type": "Element",
            }
        )
        lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
            default=None,
            metadata={
                "name": "ListaMensagemRetorno",
                "type": "Element",
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            }
        )


class NotaFiscalSoapCancelarNfseV3:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapCancelarNfseV3Input
    output = NotaFiscalSoapCancelarNfseV3Output


class NotaFiscalSoapConsultarLoteRpsV3:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapConsultarLoteRpsV3Input
    output = NotaFiscalSoapConsultarLoteRpsV3Output


@dataclass
class NotaFiscalSoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


class NotaFiscalSoapConsultarNfsePorRpsV3:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapConsultarNfsePorRpsV3Input
    output = NotaFiscalSoapConsultarNfsePorRpsV3Output


@dataclass
class NotaFiscalSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarNfsePorRpsInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


class NotaFiscalSoapConsultarNfseV3:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapConsultarNfseV3Input
    output = NotaFiscalSoapConsultarNfseV3Output


class NotaFiscalSoapConsultarSituacaoLoteRpsV3:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapConsultarSituacaoLoteRpsV3Input
    output = NotaFiscalSoapConsultarSituacaoLoteRpsV3Output


@dataclass
class NotaFiscalSoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarSituacaoLoteRpsInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


class NotaFiscalSoapRecepcionarLoteRpsV3:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapRecepcionarLoteRpsV3Input
    output = NotaFiscalSoapRecepcionarLoteRpsV3Output


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    enviar_lote_rps_resposta: Optional["RecepcionarLoteRpsResponse.EnviarLoteRpsResposta"] = field(
        default=None,
        metadata={
            "name": "EnviarLoteRpsResposta",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class EnviarLoteRpsResposta:
        numero_lote: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroLote",
                "type": "Element",
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
            }
        )
        lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
            default=None,
            metadata={
                "name": "ListaMensagemRetorno",
                "type": "Element",
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
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
                    "name": "RSAKeyValue",
                    "type": RsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "DSAKeyValue",
                    "type": DsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class ReferenceType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transforms: Optional[TransformsType] = field(
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
            "required": True,
        }
    )
    digest_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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

    transforms: Optional[TransformsType] = field(
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
class SignatureProperties(SignaturePropertiesType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Transforms(TransformsType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class X509Data(X509DataType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class ConsultarNfseEnvio:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

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
        }
    )
    periodo_emissao: Optional["ConsultarNfseEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
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
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
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
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
        }
    )
    situacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "Situacao",
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
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
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
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    mensagem_retorno: List[TcMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class NotaFiscalSoapConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarNfseInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class NotaFiscalSoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarSituacaoLoteRpsOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapConsultarSituacaoLoteRpsOutput.Body.Fault"] = field(
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
class NotaFiscalSoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapRecepcionarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapRecepcionarLoteRpsOutput.Body.Fault"] = field(
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
class KeyValue(KeyValueType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class ManifestType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
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
class Reference(ReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class RetrievalMethod(RetrievalMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


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
            "required": True,
        }
    )
    signature_method: Optional[SignatureMethodType] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
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
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    data_emissao_rps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRps",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    regime_especial_tributacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    optante_simples_nacional: Optional[int] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    incentivador_cultural: Optional[int] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    competencia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    nfse_substituida: Optional[int] = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    outras_informacoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    valor_credito: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    prestador_servico: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    tomador_servico: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    orgao_gerador: Optional[TcIdentificacaoOrgaoGerador] = field(
        default=None,
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
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
class TcInfRps:
    class Meta:
        name = "tcInfRps"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    regime_especial_tributacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    optante_simples_nacional: Optional[int] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    incentivador_cultural: Optional[int] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    contrucao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ContrucaoCivil",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


class NotaFiscalSoapConsultarSituacaoLoteRps:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapConsultarSituacaoLoteRpsInput
    output = NotaFiscalSoapConsultarSituacaoLoteRpsOutput


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
                    "name": "X509Data",
                    "type": X509Data,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "PGPData",
                    "type": Pgpdata,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyName",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyValue",
                    "type": KeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "MgmtData",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RetrievalMethod",
                    "type": RetrievalMethod,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "SPKIData",
                    "type": Spkidata,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class Manifest(ManifestType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignedInfo(SignedInfoType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class KeyInfo(KeyInfoType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


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
            "required": True,
        }
    )
    signature_value: Optional[SignatureValueType] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
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
class Signature(SignatureType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class TcNfse:
    class Meta:
        name = "tcNfse"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    inf_nfse: Optional[TcInfNfse] = field(
        default=None,
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    inf_pedido_cancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
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
class TcRps:
    class Meta:
        name = "tcRps"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    inf_rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "name": "InfRps",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
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
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    substituicao_nfse: Optional[TcInfSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    cancelar_nfse_envio: Optional["CancelarNfse.CancelarNfseEnvio"] = field(
        default=None,
        metadata={
            "name": "CancelarNfseEnvio",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class CancelarNfseEnvio:
        pedido: Optional[TcPedidoCancelamento] = field(
            default=None,
            metadata={
                "name": "Pedido",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

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
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    data_hora_cancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHoraCancelamento",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
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
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    quantidade_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    lista_rps: Optional["TcLoteRps.ListaRps"] = field(
        default=None,
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class ListaRps:
        rps: List[TcRps] = field(
            default_factory=list,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
                "min_occurs": 1,
            }
        )


@dataclass
class NotaFiscalSoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapCancelarNfseInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    enviar_lote_rps_envio: Optional["RecepcionarLoteRps.EnviarLoteRpsEnvio"] = field(
        default=None,
        metadata={
            "name": "EnviarLoteRpsEnvio",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class EnviarLoteRpsEnvio:
        lote_rps: Optional[TcLoteRps] = field(
            default=None,
            metadata={
                "name": "LoteRps",
                "type": "Element",
                "required": True,
            }
        )
        signature: Optional[SignatureType] = field(
            default=None,
            metadata={
                "name": "Signature",
                "type": "Element",
            }
        )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "required": True,
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
        }
    )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class NotaFiscalSoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class RetCancelamento:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    nfse_cancelamento: List[TcCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TcCompNfse:
    class Meta:
        name = "tcCompNfse"
        target_namespace = "http:/www.abrasf.org.br/nfse.xsd"

    nfse: Optional[TcNfse] = field(
        default=None,
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            "required": True,
        }
    )
    nfse_cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )
    nfse_substituicao: Optional[TcSubstituicaoNfse] = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http:/www.abrasf.org.br/nfse.xsd",
        }
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    cancelar_nfse_resposta: Optional["CancelarNfseResponse.CancelarNfseResposta"] = field(
        default=None,
        metadata={
            "name": "CancelarNfseResposta",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class CancelarNfseResposta:
        ret_cancelamento: Optional[RetCancelamento] = field(
            default=None,
            metadata={
                "name": "RetCancelamento",
                "type": "Element",
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            }
        )
        lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
            default=None,
            metadata={
                "name": "ListaMensagemRetorno",
                "type": "Element",
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consultar_lote_rps_resposta: Optional["ConsultarLoteRpsResponse.ConsultarLoteRpsResposta"] = field(
        default=None,
        metadata={
            "name": "ConsultarLoteRpsResposta",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ConsultarLoteRpsResposta:
        lista_nfse: Optional["ConsultarLoteRpsResponse.ConsultarLoteRpsResposta.ListaNfse"] = field(
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
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            }
        )
        lista_mensagem_retorno_lote: Optional[ListaMensagemRetornoLote] = field(
            default=None,
            metadata={
                "name": "ListaMensagemRetornoLote",
                "type": "Element",
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            }
        )

        @dataclass
        class ListaNfse:
            comp_nfse: List[TcCompNfse] = field(
                default_factory=list,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consultar_nfse_rps_resposta: Optional["ConsultarNfsePorRpsResponse.ConsultarNfseRpsResposta"] = field(
        default=None,
        metadata={
            "name": "ConsultarNfseRpsResposta",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ConsultarNfseRpsResposta:
        comp_nfse: Optional[TcCompNfse] = field(
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
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            }
        )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    consultar_nfse_resposta: Optional["ConsultarNfseResponse.ConsultarNfseResposta"] = field(
        default=None,
        metadata={
            "name": "ConsultarNfseResposta",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ConsultarNfseResposta:
        lista_nfse: Optional["ConsultarNfseResponse.ConsultarNfseResposta.ListaNfse"] = field(
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
                "namespace": "http:/www.abrasf.org.br/nfse.xsd",
            }
        )

        @dataclass
        class ListaNfse:
            comp_nfse: Optional[TcCompNfse] = field(
                default=None,
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "required": True,
                }
            )


class NotaFiscalSoapRecepcionarLoteRps:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapRecepcionarLoteRpsInput
    output = NotaFiscalSoapRecepcionarLoteRpsOutput


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    ret_cancelamento: Optional[RetCancelamento] = field(
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
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

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
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            }
        )


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    lista_nfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
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
        comp_nfse: Optional[TcCompNfse] = field(
            default=None,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http:/www.abrasf.org.br/nfse.xsd"

    comp_nfse: Optional[TcCompNfse] = field(
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
class NotaFiscalSoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapCancelarNfseOutput.Body.Fault"] = field(
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
class NotaFiscalSoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NotaFiscalSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarNfsePorRpsOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapConsultarNfsePorRpsOutput.Body.Fault"] = field(
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
class NotaFiscalSoapConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.abrasf.org.br/nfse.xsd"

    body: Optional["NotaFiscalSoapConsultarNfseOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            }
        )
        fault: Optional["NotaFiscalSoapConsultarNfseOutput.Body.Fault"] = field(
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


class NotaFiscalSoapCancelarNfse:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapCancelarNfseInput
    output = NotaFiscalSoapCancelarNfseOutput


class NotaFiscalSoapConsultarLoteRps:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapConsultarLoteRpsInput
    output = NotaFiscalSoapConsultarLoteRpsOutput


class NotaFiscalSoapConsultarNfse:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapConsultarNfseInput
    output = NotaFiscalSoapConsultarNfseOutput


class NotaFiscalSoapConsultarNfsePorRps:
    style = "document"
    location = "https://notajoseense.sjc.sp.gov.br/notafiscal-ws/NotaFiscalSoap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NotaFiscalSoapConsultarNfsePorRpsInput
    output = NotaFiscalSoapConsultarNfsePorRpsOutput
