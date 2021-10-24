from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://ws.bhiss.pbh.gov.br"


@dataclass
class Input:
    class Meta:
        name = "input"

    nfse_cabec_msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "nfseCabecMsg",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nfse_dados_msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "nfseDadosMsg",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Output:
    class Meta:
        name = "output"

    output_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputXML",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class CancelarNfseRequest(Input):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class CancelarNfseResponse(Output):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarLoteRpsRequest(Input):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarLoteRpsResponse(Output):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarNfsePorFaixaRequest(Input):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarNfsePorFaixaResponse(Output):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarNfsePorRpsRequest(Input):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarNfsePorRpsResponse(Output):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarNfseRequest(Input):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarNfseResponse(Output):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarSituacaoLoteRpsRequest(Input):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class ConsultarSituacaoLoteRpsResponse(Output):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class GerarNfseRequest(Input):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class GerarNfseResponse(Output):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class RecepcionarLoteRpsRequest(Input):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class RecepcionarLoteRpsResponse(Output):
    class Meta:
        namespace = "http://ws.bhiss.pbh.gov.br"


@dataclass
class NfseCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseCancelarNfseInput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )


@dataclass
class NfseCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )
        fault: Optional["NfseCancelarNfseOutput.Body.Fault"] = field(
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
class NfseConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )


@dataclass
class NfseConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )
        fault: Optional["NfseConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NfseConsultarNfsePorFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfsePorFaixaInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_faixa_request: Optional[ConsultarNfsePorFaixaRequest] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorFaixaRequest",
                "type": "Element",
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )


@dataclass
class NfseConsultarNfsePorFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfsePorFaixaOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_faixa_response: Optional[ConsultarNfsePorFaixaResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorFaixaResponse",
                "type": "Element",
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )
        fault: Optional["NfseConsultarNfsePorFaixaOutput.Body.Fault"] = field(
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
class NfseConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfsePorRpsInput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )


@dataclass
class NfseConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfsePorRpsOutput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )
        fault: Optional["NfseConsultarNfsePorRpsOutput.Body.Fault"] = field(
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
class NfseConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfseInput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )


@dataclass
class NfseConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfseOutput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )
        fault: Optional["NfseConsultarNfseOutput.Body.Fault"] = field(
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
class NfseConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarSituacaoLoteRpsInput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )


@dataclass
class NfseConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarSituacaoLoteRpsOutput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )
        fault: Optional["NfseConsultarSituacaoLoteRpsOutput.Body.Fault"] = field(
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
class NfseGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseGerarNfseInput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )


@dataclass
class NfseGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseGerarNfseOutput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )
        fault: Optional["NfseGerarNfseOutput.Body.Fault"] = field(
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
class NfseRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )


@dataclass
class NfseRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseRecepcionarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://ws.bhiss.pbh.gov.br",
            }
        )
        fault: Optional["NfseRecepcionarLoteRpsOutput.Body.Fault"] = field(
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


class NfseCancelarNfse:
    style = "document"
    location = "https://nfe.portoalegre.rs.gov.br:443/bhiss-ws/nfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://ws.bhiss.pbh.gov.br/CancelarNfse"
    input = NfseCancelarNfseInput
    output = NfseCancelarNfseOutput


class NfseConsultarLoteRps:
    style = "document"
    location = "https://nfe.portoalegre.rs.gov.br:443/bhiss-ws/nfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://ws.bhiss.pbh.gov.br/ConsultarLoteRps"
    input = NfseConsultarLoteRpsInput
    output = NfseConsultarLoteRpsOutput


class NfseConsultarNfse:
    style = "document"
    location = "https://nfe.portoalegre.rs.gov.br:443/bhiss-ws/nfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://ws.bhiss.pbh.gov.br/ConsultarNfse"
    input = NfseConsultarNfseInput
    output = NfseConsultarNfseOutput


class NfseConsultarNfsePorFaixa:
    style = "document"
    location = "https://nfe.portoalegre.rs.gov.br:443/bhiss-ws/nfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://ws.bhiss.pbh.gov.br/ConsultarNfsePorFaixa"
    input = NfseConsultarNfsePorFaixaInput
    output = NfseConsultarNfsePorFaixaOutput


class NfseConsultarNfsePorRps:
    style = "document"
    location = "https://nfe.portoalegre.rs.gov.br:443/bhiss-ws/nfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://ws.bhiss.pbh.gov.br/ConsultarNfsePorRps"
    input = NfseConsultarNfsePorRpsInput
    output = NfseConsultarNfsePorRpsOutput


class NfseConsultarSituacaoLoteRps:
    style = "document"
    location = "https://nfe.portoalegre.rs.gov.br:443/bhiss-ws/nfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://ws.bhiss.pbh.gov.br/ConsultarSituacaoLoteRps"
    input = NfseConsultarSituacaoLoteRpsInput
    output = NfseConsultarSituacaoLoteRpsOutput


class NfseGerarNfse:
    style = "document"
    location = "https://nfe.portoalegre.rs.gov.br:443/bhiss-ws/nfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://ws.bhiss.pbh.gov.br/GerarNfse"
    input = NfseGerarNfseInput
    output = NfseGerarNfseOutput


class NfseRecepcionarLoteRps:
    style = "document"
    location = "https://nfe.portoalegre.rs.gov.br:443/bhiss-ws/nfse"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://ws.bhiss.pbh.gov.br/RecepcionarLoteRps"
    input = NfseRecepcionarLoteRpsInput
    output = NfseRecepcionarLoteRpsOutput
