from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
        }
    )
    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcInfConfirmacaoCancelamento:
    class Meta:
        name = "tcInfConfirmacaoCancelamento"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    sucesso: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sucesso",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    data_hora: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcTransform:
    class Meta:
        name = "tcTransform"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DigestValue:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class TcCanonicalizationMethod:
    class Meta:
        name = "tcCanonicalizationMethod"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcDigestMethod:
    class Meta:
        name = "tcDigestMethod"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcSignatureMethod:
    class Meta:
        name = "tcSignatureMethod"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcX509Data:
    class Meta:
        name = "tcX509Data"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    x509_certificate: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    identificacao_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    codigo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TcListaMensagemRetorno:
    class Meta:
        name = "tcListaMensagemRetorno"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class CanonicalizationMethod(TcCanonicalizationMethod):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DigestMethod(TcDigestMethod):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureMethod(TcSignatureMethod):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Transform(TcTransform):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class X509Data(TcX509Data):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class TcKeyInfo:
    class Meta:
        name = "tcKeyInfo"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    x509_data: Optional[X509Data] = field(
        default=None,
        metadata={
            "name": "X509Data",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcTransforms:
    class Meta:
        name = "tcTransforms"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )


@dataclass
class Transforms(TcTransforms):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class TcReference:
    class Meta:
        name = "tcReference"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Reference(TcReference):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class TcSigInfo:
    class Meta:
        name = "tcSigInfo"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_method: Optional[SignatureMethod] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class Signature:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    signed_info: Optional[TcSigInfo] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "required": True,
        }
    )
    signature_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "required": True,
        }
    )
    key_info: Optional[TcKeyInfo] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    inf_pedido_cancelamento: Optional[TcInfPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "",
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


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    inf_confirmacao_cancelamento: Optional[TcInfConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "InfConfirmacaoCancelamento",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CancelarNev01CancelarNfseEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    body: Optional["CancelarNev01CancelarNfseEnvioInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse_envio: Optional[CancelarNfseEnvio] = field(
            default=None,
            metadata={
                "name": "CancelarNfseEnvio",
                "type": "Element",
                "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            }
        )


@dataclass
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    confirmacao: Optional[TcConfirmacaoCancelamento] = field(
        default=None,
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class CancelarNfseResposta:
    class Meta:
        name = "cancelarNfseResposta"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    cancelamento: List[TcCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "name": "Cancelamento",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    lista_mensagem_retorno: List[TcListaMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )


@dataclass
class CancelarNfseEnvioResponse:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    cancelar_nfse_reposta: Optional[CancelarNfseResposta] = field(
        default=None,
        metadata={
            "name": "CancelarNfseReposta",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CancelarNev01CancelarNfseEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    body: Optional["CancelarNev01CancelarNfseEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse_envio_response: Optional[CancelarNfseEnvioResponse] = field(
            default=None,
            metadata={
                "name": "CancelarNfseEnvioResponse",
                "type": "Element",
                "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            }
        )
        fault: Optional["CancelarNev01CancelarNfseEnvioOutput.Body.Fault"] = field(
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


class CancelarNev01CancelarNfseEnvio:
    style = "document"
    location = "http://e-gov.betha.com.br/e-nota-contribuinte-ws/cancelarNfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = CancelarNev01CancelarNfseEnvioInput
    output = CancelarNev01CancelarNfseEnvioOutput
