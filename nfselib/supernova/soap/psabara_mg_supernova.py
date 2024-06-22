from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://ws.supernova.com.br/"


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseFaixa:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseFaixaResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoPrestado:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoTomado:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoTomadoResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsSincrono:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SubstituirNfse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SubstituirNfseResponse:
    class Meta:
        namespace = "http://ws.supernova.com.br/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SnissdigitalsvcCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfse: Optional[CancelarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.supernova.com.br/",
            },
        )


@dataclass
class SnissdigitalsvcCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://ws.supernova.com.br/",
            },
        )
        Fault: Optional["SnissdigitalsvcCancelarNfseOutput.Body.Fault"] = (
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
class SnissdigitalsvcConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://ws.supernova.com.br/",
            },
        )


@dataclass
class SnissdigitalsvcConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://ws.supernova.com.br/",
            },
        )
        Fault: Optional["SnissdigitalsvcConsultarLoteRpsOutput.Body.Fault"] = (
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
class SnissdigitalsvcConsultarNfseFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarNfseFaixaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseFaixa: Optional[ConsultarNfseFaixa] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.supernova.com.br/",
            },
        )


@dataclass
class SnissdigitalsvcConsultarNfseFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarNfseFaixaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseFaixaResponse: Optional[ConsultarNfseFaixaResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.supernova.com.br/",
                },
            )
        )
        Fault: Optional[
            "SnissdigitalsvcConsultarNfseFaixaOutput.Body.Fault"
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
class SnissdigitalsvcConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarNfsePorRpsInput.Body"] = field(
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
                "namespace": "http://ws.supernova.com.br/",
            },
        )


@dataclass
class SnissdigitalsvcConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "http://ws.supernova.com.br/",
                },
            )
        )
        Fault: Optional[
            "SnissdigitalsvcConsultarNfsePorRpsOutput.Body.Fault"
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
class SnissdigitalsvcConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarNfseServicoPrestadoInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseServicoPrestado: Optional[
            ConsultarNfseServicoPrestado
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.supernova.com.br/",
            },
        )


@dataclass
class SnissdigitalsvcConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "SnissdigitalsvcConsultarNfseServicoPrestadoOutput.Body"
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
                "namespace": "http://ws.supernova.com.br/",
            },
        )
        Fault: Optional[
            "SnissdigitalsvcConsultarNfseServicoPrestadoOutput.Body.Fault"
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
class SnissdigitalsvcConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarNfseServicoTomadoInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseServicoTomado: Optional[ConsultarNfseServicoTomado] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.supernova.com.br/",
                },
            )
        )


@dataclass
class SnissdigitalsvcConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcConsultarNfseServicoTomadoOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseServicoTomadoResponse: Optional[
            ConsultarNfseServicoTomadoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.supernova.com.br/",
            },
        )
        Fault: Optional[
            "SnissdigitalsvcConsultarNfseServicoTomadoOutput.Body.Fault"
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
class SnissdigitalsvcGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfse: Optional[GerarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.supernova.com.br/",
            },
        )


@dataclass
class SnissdigitalsvcGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcGerarNfseOutput.Body"] = field(
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
                "namespace": "http://ws.supernova.com.br/",
            },
        )
        Fault: Optional["SnissdigitalsvcGerarNfseOutput.Body.Fault"] = field(
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
class SnissdigitalsvcRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcRecepcionarLoteRpsSincronoInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincrono: Optional[RecepcionarLoteRpsSincrono] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.supernova.com.br/",
                },
            )
        )


@dataclass
class SnissdigitalsvcRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcRecepcionarLoteRpsSincronoOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincronoResponse: Optional[
            RecepcionarLoteRpsSincronoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.supernova.com.br/",
            },
        )
        Fault: Optional[
            "SnissdigitalsvcRecepcionarLoteRpsSincronoOutput.Body.Fault"
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
class SnissdigitalsvcRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://ws.supernova.com.br/",
            },
        )


@dataclass
class SnissdigitalsvcRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://ws.supernova.com.br/",
                },
            )
        )
        Fault: Optional[
            "SnissdigitalsvcRecepcionarLoteRpsOutput.Body.Fault"
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
class SnissdigitalsvcSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcSubstituirNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SubstituirNfse: Optional[SubstituirNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.supernova.com.br/",
            },
        )


@dataclass
class SnissdigitalsvcSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["SnissdigitalsvcSubstituirNfseOutput.Body"] = field(
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
                "namespace": "http://ws.supernova.com.br/",
            },
        )
        Fault: Optional["SnissdigitalsvcSubstituirNfseOutput.Body.Fault"] = (
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


class SnissdigitalsvcCancelarNfse:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcCancelarNfseInput
    output = SnissdigitalsvcCancelarNfseOutput


class SnissdigitalsvcConsultarLoteRps:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcConsultarLoteRpsInput
    output = SnissdigitalsvcConsultarLoteRpsOutput


class SnissdigitalsvcConsultarNfseFaixa:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcConsultarNfseFaixaInput
    output = SnissdigitalsvcConsultarNfseFaixaOutput


class SnissdigitalsvcConsultarNfsePorRps:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcConsultarNfsePorRpsInput
    output = SnissdigitalsvcConsultarNfsePorRpsOutput


class SnissdigitalsvcConsultarNfseServicoPrestado:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcConsultarNfseServicoPrestadoInput
    output = SnissdigitalsvcConsultarNfseServicoPrestadoOutput


class SnissdigitalsvcConsultarNfseServicoTomado:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcConsultarNfseServicoTomadoInput
    output = SnissdigitalsvcConsultarNfseServicoTomadoOutput


class SnissdigitalsvcGerarNfse:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcGerarNfseInput
    output = SnissdigitalsvcGerarNfseOutput


class SnissdigitalsvcRecepcionarLoteRps:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcRecepcionarLoteRpsInput
    output = SnissdigitalsvcRecepcionarLoteRpsOutput


class SnissdigitalsvcRecepcionarLoteRpsSincrono:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcRecepcionarLoteRpsSincronoInput
    output = SnissdigitalsvcRecepcionarLoteRpsSincronoOutput


class SnissdigitalsvcSubstituirNfse:
    style = "document"
    location = "http://sabara.supernova.com.br:8091/nfe/snissdigitalsvc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = SnissdigitalsvcSubstituirNfseInput
    output = SnissdigitalsvcSubstituirNfseOutput
