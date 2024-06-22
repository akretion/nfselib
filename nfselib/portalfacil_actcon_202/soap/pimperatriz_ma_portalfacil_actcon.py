from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class Input:
    class Meta:
        name = "input"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Output:
    class Meta:
        name = "output"

    outputXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class CancelarNfseRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class CancelarNfseResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarLoteRpsRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarLoteRpsResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarNfsePorFaixaRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarNfsePorFaixaResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarNfsePorRpsRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarNfsePorRpsResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarNfseServicoPrestadoRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarNfseServicoPrestadoResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarNfseServicoTomadoRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class ConsultarNfseServicoTomadoResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class GerarNfseRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class GerarNfseResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class RecepcionarLoteRpsRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class RecepcionarLoteRpsResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class RecepcionarLoteRpsSincronoRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class RecepcionarLoteRpsSincronoResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class SubstituirNfseRequest(Input):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class SubstituirNfseResponse(Output):
    class Meta:
        namespace = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl"


@dataclass
class NfseSoapPortTypeCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeCancelarNfseInput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )
        Fault: Optional["NfseSoapPortTypeCancelarNfseOutput.Body.Fault"] = (
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
class NfseSoapPortTypeConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )
        Fault: Optional[
            "NfseSoapPortTypeConsultarLoteRpsOutput.Body.Fault"
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
class NfseSoapPortTypeConsultarNfsePorFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeConsultarNfsePorFaixaInput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeConsultarNfsePorFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeConsultarNfsePorFaixaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorFaixaResponse: Optional[
            ConsultarNfsePorFaixaResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )
        Fault: Optional[
            "NfseSoapPortTypeConsultarNfsePorFaixaOutput.Body.Fault"
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
class NfseSoapPortTypeConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeConsultarNfsePorRpsInput.Body"] = field(
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
                    "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
                },
            )
        )


@dataclass
class NfseSoapPortTypeConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
                },
            )
        )
        Fault: Optional[
            "NfseSoapPortTypeConsultarNfsePorRpsOutput.Body.Fault"
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
class NfseSoapPortTypeConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfseSoapPortTypeConsultarNfseServicoPrestadoInput.Body"
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfseSoapPortTypeConsultarNfseServicoPrestadoOutput.Body"
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )
        Fault: Optional[
            "NfseSoapPortTypeConsultarNfseServicoPrestadoOutput.Body.Fault"
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
class NfseSoapPortTypeConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeConsultarNfseServicoTomadoInput.Body"] = (
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeConsultarNfseServicoTomadoOutput.Body"] = (
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )
        Fault: Optional[
            "NfseSoapPortTypeConsultarNfseServicoTomadoOutput.Body.Fault"
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
class NfseSoapPortTypeGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeGerarNfseInput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeGerarNfseOutput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )
        Fault: Optional["NfseSoapPortTypeGerarNfseOutput.Body.Fault"] = field(
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
class NfseSoapPortTypeRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeRecepcionarLoteRpsSincronoInput.Body"] = (
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeRecepcionarLoteRpsSincronoOutput.Body"] = (
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )
        Fault: Optional[
            "NfseSoapPortTypeRecepcionarLoteRpsSincronoOutput.Body.Fault"
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
class NfseSoapPortTypeRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
                },
            )
        )
        Fault: Optional[
            "NfseSoapPortTypeRecepcionarLoteRpsOutput.Body.Fault"
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
class NfseSoapPortTypeSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeSubstituirNfseInput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )


@dataclass
class NfseSoapPortTypeSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSoapPortTypeSubstituirNfseOutput.Body"] = field(
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
                "namespace": "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/nfse.wsdl",
            },
        )
        Fault: Optional["NfseSoapPortTypeSubstituirNfseOutput.Body.Fault"] = (
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


class NfseSoapPortTypeCancelarNfse:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#CancelarNfse"
    input = NfseSoapPortTypeCancelarNfseInput
    output = NfseSoapPortTypeCancelarNfseOutput


class NfseSoapPortTypeConsultarLoteRps:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#ConsultarLoteRps"
    input = NfseSoapPortTypeConsultarLoteRpsInput
    output = NfseSoapPortTypeConsultarLoteRpsOutput


class NfseSoapPortTypeConsultarNfsePorFaixa:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#ConsultarNfsePorFaixa"
    input = NfseSoapPortTypeConsultarNfsePorFaixaInput
    output = NfseSoapPortTypeConsultarNfsePorFaixaOutput


class NfseSoapPortTypeConsultarNfsePorRps:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#ConsultarNfsePorRps"
    input = NfseSoapPortTypeConsultarNfsePorRpsInput
    output = NfseSoapPortTypeConsultarNfsePorRpsOutput


class NfseSoapPortTypeConsultarNfseServicoPrestado:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#ConsultarNfseServicoPrestado"
    input = NfseSoapPortTypeConsultarNfseServicoPrestadoInput
    output = NfseSoapPortTypeConsultarNfseServicoPrestadoOutput


class NfseSoapPortTypeConsultarNfseServicoTomado:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#ConsultarNfseServicoTomado"
    input = NfseSoapPortTypeConsultarNfseServicoTomadoInput
    output = NfseSoapPortTypeConsultarNfseServicoTomadoOutput


class NfseSoapPortTypeGerarNfse:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#GerarNfse"
    input = NfseSoapPortTypeGerarNfseInput
    output = NfseSoapPortTypeGerarNfseOutput


class NfseSoapPortTypeRecepcionarLoteRps:
    style = "document"
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#RecepcionarLoteRps"
    input = NfseSoapPortTypeRecepcionarLoteRpsInput
    output = NfseSoapPortTypeRecepcionarLoteRpsOutput


class NfseSoapPortTypeRecepcionarLoteRpsSincrono:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#RecepcionarLoteRpsSincrono"
    input = NfseSoapPortTypeRecepcionarLoteRpsSincronoInput
    output = NfseSoapPortTypeRecepcionarLoteRpsSincronoOutput


class NfseSoapPortTypeSubstituirNfse:
    location = "https://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse-ma-imperatriz.portalfacil.com.br/nfseserv/webservice/servicos#SubstituirNfse"
    input = NfseSoapPortTypeSubstituirNfseInput
    output = NfseSoapPortTypeSubstituirNfseOutput
