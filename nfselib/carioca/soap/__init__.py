from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://notacarioca.rio.gov.br/"


@dataclass
class CancelarNfseRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    input_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputXML",
            "type": "Element",
        }
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    output_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultarLoteRpsRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    input_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    output_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfsePorRpsRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    input_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    output_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfseRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    input_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    output_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    input_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    output_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputXML",
            "type": "Element",
        }
    )


@dataclass
class GerarNfseRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    input_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputXML",
            "type": "Element",
        }
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    output_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputXML",
            "type": "Element",
        }
    )


@dataclass
class RecepcionarLoteRpsRequest:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    input_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputXML",
            "type": "Element",
        }
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://notacarioca.rio.gov.br/"

    output_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputXML",
            "type": "Element",
        }
    )


@dataclass
class NfseSoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse_request: Optional[CancelarNfseRequest] = field(
            default=None,
            metadata={
                "name": "CancelarNfseRequest",
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )


@dataclass
class NfseSoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )
        fault: Optional["NfseSoapCancelarNfseOutput.Body.Fault"] = field(
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
class NfseSoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps_request: Optional[ConsultarLoteRpsRequest] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRpsRequest",
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )


@dataclass
class NfseSoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )
        fault: Optional["NfseSoapConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NfseSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rps_request: Optional[ConsultarNfsePorRpsRequest] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorRpsRequest",
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )


@dataclass
class NfseSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapConsultarNfsePorRpsOutput.Body"] = field(
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
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )
        fault: Optional["NfseSoapConsultarNfsePorRpsOutput.Body.Fault"] = field(
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
class NfseSoapConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_request: Optional[ConsultarNfseRequest] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseRequest",
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )


@dataclass
class NfseSoapConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapConsultarNfseOutput.Body"] = field(
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
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )
        fault: Optional["NfseSoapConsultarNfseOutput.Body.Fault"] = field(
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
class NfseSoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps_request: Optional[ConsultarSituacaoLoteRpsRequest] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRpsRequest",
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )


@dataclass
class NfseSoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapConsultarSituacaoLoteRpsOutput.Body"] = field(
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
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )
        fault: Optional["NfseSoapConsultarSituacaoLoteRpsOutput.Body.Fault"] = field(
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
class NfseSoapGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        gerar_nfse_request: Optional[GerarNfseRequest] = field(
            default=None,
            metadata={
                "name": "GerarNfseRequest",
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )


@dataclass
class NfseSoapGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapGerarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        gerar_nfse_response: Optional[GerarNfseResponse] = field(
            default=None,
            metadata={
                "name": "GerarNfseResponse",
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )
        fault: Optional["NfseSoapGerarNfseOutput.Body.Fault"] = field(
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
class NfseSoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps_request: Optional[RecepcionarLoteRpsRequest] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsRequest",
                "type": "Element",
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )


@dataclass
class NfseSoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSoapRecepcionarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://notacarioca.rio.gov.br/",
            }
        )
        fault: Optional["NfseSoapRecepcionarLoteRpsOutput.Body.Fault"] = field(
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


class NfseSoapCancelarNfse:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://notacarioca.rio.gov.br/CancelarNfse"
    input = NfseSoapCancelarNfseInput
    output = NfseSoapCancelarNfseOutput


class NfseSoapConsultarLoteRps:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://notacarioca.rio.gov.br/ConsultarLoteRps"
    input = NfseSoapConsultarLoteRpsInput
    output = NfseSoapConsultarLoteRpsOutput


class NfseSoapConsultarNfse:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://notacarioca.rio.gov.br/ConsultarNfse"
    input = NfseSoapConsultarNfseInput
    output = NfseSoapConsultarNfseOutput


class NfseSoapConsultarNfsePorRps:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://notacarioca.rio.gov.br/ConsultarNfsePorRps"
    input = NfseSoapConsultarNfsePorRpsInput
    output = NfseSoapConsultarNfsePorRpsOutput


class NfseSoapConsultarSituacaoLoteRps:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://notacarioca.rio.gov.br/ConsultarSituacaoLoteRps"
    input = NfseSoapConsultarSituacaoLoteRpsInput
    output = NfseSoapConsultarSituacaoLoteRpsOutput


class NfseSoapGerarNfse:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://notacarioca.rio.gov.br/GerarNfse"
    input = NfseSoapGerarNfseInput
    output = NfseSoapGerarNfseOutput


class NfseSoapRecepcionarLoteRps:
    style = "document"
    location = "https://notacarioca.rio.gov.br/WSNacional/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://notacarioca.rio.gov.br/RecepcionarLoteRps"
    input = NfseSoapRecepcionarLoteRpsInput
    output = NfseSoapRecepcionarLoteRpsOutput
