from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nfse.abrasf.org.br/"


@dataclass
class CancelarNfseRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorFaixaRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorFaixaResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRpsRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoTomadoRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoTomadoResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SubstituirNfseRequest:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SubstituirNfseResponse:
    class Meta:
        namespace = "http://nfse.abrasf.org.br/"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class NfseWsserviceSoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseRequest: Optional[CancelarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseResponse: Optional[CancelarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )
        Fault: Optional["NfseWsserviceSoapCancelarNfseOutput.Body.Fault"] = (
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
class NfseWsserviceSoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsRequest: Optional[ConsultarLoteRpsRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )
        Fault: Optional[
            "NfseWsserviceSoapConsultarLoteRpsOutput.Body.Fault"
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
class NfseWsserviceSoapConsultarNfsePorFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapConsultarNfsePorFaixaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorFaixaRequest: Optional[
            ConsultarNfsePorFaixaRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapConsultarNfsePorFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapConsultarNfsePorFaixaOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfsePorFaixaResponse: Optional[
            ConsultarNfsePorFaixaResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )
        Fault: Optional[
            "NfseWsserviceSoapConsultarNfsePorFaixaOutput.Body.Fault"
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
class NfseWsserviceSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsRequest: Optional[ConsultarNfsePorRpsRequest] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://nfse.abrasf.org.br/",
                },
            )
        )


@dataclass
class NfseWsserviceSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "http://nfse.abrasf.org.br/",
                },
            )
        )
        Fault: Optional[
            "NfseWsserviceSoapConsultarNfsePorRpsOutput.Body.Fault"
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
class NfseWsserviceSoapConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfseWsserviceSoapConsultarNfseServicoPrestadoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoPrestadoRequest: Optional[
            ConsultarNfseServicoPrestadoRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfseWsserviceSoapConsultarNfseServicoPrestadoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoPrestadoResponse: Optional[
            ConsultarNfseServicoPrestadoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )
        Fault: Optional[
            "NfseWsserviceSoapConsultarNfseServicoPrestadoOutput.Body.Fault"
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
class NfseWsserviceSoapConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapConsultarNfseServicoTomadoInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseServicoTomadoRequest: Optional[
            ConsultarNfseServicoTomadoRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfseWsserviceSoapConsultarNfseServicoTomadoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoTomadoResponse: Optional[
            ConsultarNfseServicoTomadoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )
        Fault: Optional[
            "NfseWsserviceSoapConsultarNfseServicoTomadoOutput.Body.Fault"
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
class NfseWsserviceSoapGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfseRequest: Optional[GerarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapGerarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfseResponse: Optional[GerarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )
        Fault: Optional["NfseWsserviceSoapGerarNfseOutput.Body.Fault"] = field(
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
class NfseWsserviceSoapRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapRecepcionarLoteRpsSincronoInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincronoRequest: Optional[
            RecepcionarLoteRpsSincronoRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfseWsserviceSoapRecepcionarLoteRpsSincronoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincronoResponse: Optional[
            RecepcionarLoteRpsSincronoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )
        Fault: Optional[
            "NfseWsserviceSoapRecepcionarLoteRpsSincronoOutput.Body.Fault"
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
class NfseWsserviceSoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsRequest: Optional[RecepcionarLoteRpsRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://nfse.abrasf.org.br/",
                },
            )
        )
        Fault: Optional[
            "NfseWsserviceSoapRecepcionarLoteRpsOutput.Body.Fault"
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
class NfseWsserviceSoapSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapSubstituirNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SubstituirNfseRequest: Optional[SubstituirNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )


@dataclass
class NfseWsserviceSoapSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsserviceSoapSubstituirNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SubstituirNfseResponse: Optional[SubstituirNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br/",
            },
        )
        Fault: Optional["NfseWsserviceSoapSubstituirNfseOutput.Body.Fault"] = (
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


class NfseWsserviceSoapCancelarNfse:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/CancelarNfse"
    input = NfseWsserviceSoapCancelarNfseInput
    output = NfseWsserviceSoapCancelarNfseOutput


class NfseWsserviceSoapConsultarLoteRps:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarLoteRps"
    input = NfseWsserviceSoapConsultarLoteRpsInput
    output = NfseWsserviceSoapConsultarLoteRpsOutput


class NfseWsserviceSoapConsultarNfsePorFaixa:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarNfsePorFaixa"
    input = NfseWsserviceSoapConsultarNfsePorFaixaInput
    output = NfseWsserviceSoapConsultarNfsePorFaixaOutput


class NfseWsserviceSoapConsultarNfsePorRps:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarNfsePorRps"
    input = NfseWsserviceSoapConsultarNfsePorRpsInput
    output = NfseWsserviceSoapConsultarNfsePorRpsOutput


class NfseWsserviceSoapConsultarNfseServicoPrestado:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarNfseServicoPrestado"
    input = NfseWsserviceSoapConsultarNfseServicoPrestadoInput
    output = NfseWsserviceSoapConsultarNfseServicoPrestadoOutput


class NfseWsserviceSoapConsultarNfseServicoTomado:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarNfseServicoTomado"
    input = NfseWsserviceSoapConsultarNfseServicoTomadoInput
    output = NfseWsserviceSoapConsultarNfseServicoTomadoOutput


class NfseWsserviceSoapGerarNfse:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/GerarNfse"
    input = NfseWsserviceSoapGerarNfseInput
    output = NfseWsserviceSoapGerarNfseOutput


class NfseWsserviceSoapRecepcionarLoteRps:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/RecepcionarLoteRps"
    input = NfseWsserviceSoapRecepcionarLoteRpsInput
    output = NfseWsserviceSoapRecepcionarLoteRpsOutput


class NfseWsserviceSoapRecepcionarLoteRpsSincrono:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/RecepcionarLoteRpsSincrono"
    input = NfseWsserviceSoapRecepcionarLoteRpsSincronoInput
    output = NfseWsserviceSoapRecepcionarLoteRpsSincronoOutput


class NfseWsserviceSoapSubstituirNfse:
    style = "document"
    location = "https://nfse.niteroi.rj.gov.br/nfse/WSNacional2/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/SubstituirNfse"
    input = NfseWsserviceSoapSubstituirNfseInput
    output = NfseWsserviceSoapSubstituirNfseOutput
