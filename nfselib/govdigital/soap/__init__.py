from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nfse.abrasf.org.br"


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
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class CancelarNfseResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarLoteRpsRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarLoteRpsResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarNfsePorFaixaRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarNfsePorFaixaResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarNfsePorRpsRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarNfsePorRpsResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarNfseServicoPrestadoRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarNfseServicoPrestadoResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarNfseServicoTomadoRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class ConsultarNfseServicoTomadoResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class GerarNfseRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class GerarNfseResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class RecepcionarLoteRpsRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class RecepcionarLoteRpsResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class RecepcionarLoteRpsSincronoRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class RecepcionarLoteRpsSincronoResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class SubstituirNfseRequest(Input):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


@dataclass
class SubstituirNfseResponse(Output):
    class Meta:
        namespace = "http://nfse.abrasf.org.br"


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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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
class NfseConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfseServicoPrestadoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_servico_prestado_request: Optional[ConsultarNfseServicoPrestadoRequest] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseServicoPrestadoRequest",
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            }
        )


@dataclass
class NfseConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfseServicoPrestadoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_servico_prestado_response: Optional[ConsultarNfseServicoPrestadoResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseServicoPrestadoResponse",
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            }
        )
        fault: Optional["NfseConsultarNfseServicoPrestadoOutput.Body.Fault"] = field(
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
class NfseConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfseServicoTomadoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_servico_tomado_request: Optional[ConsultarNfseServicoTomadoRequest] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseServicoTomadoRequest",
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            }
        )


@dataclass
class NfseConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseConsultarNfseServicoTomadoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_servico_tomado_response: Optional[ConsultarNfseServicoTomadoResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseServicoTomadoResponse",
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            }
        )
        fault: Optional["NfseConsultarNfseServicoTomadoOutput.Body.Fault"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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
class NfseRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseRecepcionarLoteRpsSincronoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps_sincrono_request: Optional[RecepcionarLoteRpsSincronoRequest] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsSincronoRequest",
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            }
        )


@dataclass
class NfseRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseRecepcionarLoteRpsSincronoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps_sincrono_response: Optional[RecepcionarLoteRpsSincronoResponse] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsSincronoResponse",
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            }
        )
        fault: Optional["NfseRecepcionarLoteRpsSincronoOutput.Body.Fault"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
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
                "namespace": "http://nfse.abrasf.org.br",
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


@dataclass
class NfseSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSubstituirNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        substituir_nfse_request: Optional[SubstituirNfseRequest] = field(
            default=None,
            metadata={
                "name": "SubstituirNfseRequest",
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            }
        )


@dataclass
class NfseSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfseSubstituirNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        substituir_nfse_response: Optional[SubstituirNfseResponse] = field(
            default=None,
            metadata={
                "name": "SubstituirNfseResponse",
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            }
        )
        fault: Optional["NfseSubstituirNfseOutput.Body.Fault"] = field(
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
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/CancelarNfse"
    input = NfseCancelarNfseInput
    output = NfseCancelarNfseOutput


class NfseConsultarLoteRps:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/ConsultarLoteRps"
    input = NfseConsultarLoteRpsInput
    output = NfseConsultarLoteRpsOutput


class NfseConsultarNfsePorFaixa:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/ConsultarNfsePorFaixa"
    input = NfseConsultarNfsePorFaixaInput
    output = NfseConsultarNfsePorFaixaOutput


class NfseConsultarNfsePorRps:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/ConsultarNfsePorRps"
    input = NfseConsultarNfsePorRpsInput
    output = NfseConsultarNfsePorRpsOutput


class NfseConsultarNfseServicoPrestado:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/ConsultarNfseServicoPrestado"
    input = NfseConsultarNfseServicoPrestadoInput
    output = NfseConsultarNfseServicoPrestadoOutput


class NfseConsultarNfseServicoTomado:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/ConsultarNfseServicoTomado"
    input = NfseConsultarNfseServicoTomadoInput
    output = NfseConsultarNfseServicoTomadoOutput


class NfseGerarNfse:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/GerarNfse"
    input = NfseGerarNfseInput
    output = NfseGerarNfseOutput


class NfseRecepcionarLoteRps:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/RecepcionarLoteRps"
    input = NfseRecepcionarLoteRpsInput
    output = NfseRecepcionarLoteRpsOutput


class NfseRecepcionarLoteRpsSincrono:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/RecepcionarLoteRpsSincrono"
    input = NfseRecepcionarLoteRpsSincronoInput
    output = NfseRecepcionarLoteRpsSincronoOutput


class NfseSubstituirNfse:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/vgp"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nfse.abrasf.org.br/SubstituirNfse"
    input = NfseSubstituirNfseInput
    output = NfseSubstituirNfseOutput
