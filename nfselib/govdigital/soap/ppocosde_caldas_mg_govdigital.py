from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nfse.abrasf.org.br"


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

    Body: Optional["NfseCancelarNfseInput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )
        Fault: Optional["NfseCancelarNfseOutput.Body.Fault"] = field(
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
class NfseConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )
        Fault: Optional["NfseConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NfseConsultarNfsePorFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfsePorFaixaInput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseConsultarNfsePorFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfsePorFaixaOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )
        Fault: Optional["NfseConsultarNfsePorFaixaOutput.Body.Fault"] = field(
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
class NfseConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfsePorRpsInput.Body"] = field(
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
                    "namespace": "http://nfse.abrasf.org.br",
                },
            )
        )


@dataclass
class NfseConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "http://nfse.abrasf.org.br",
                },
            )
        )
        Fault: Optional["NfseConsultarNfsePorRpsOutput.Body.Fault"] = field(
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
class NfseConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfseServicoPrestadoInput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfseServicoPrestadoOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )
        Fault: Optional[
            "NfseConsultarNfseServicoPrestadoOutput.Body.Fault"
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
class NfseConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfseServicoTomadoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoTomadoRequest: Optional[
            ConsultarNfseServicoTomadoRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseConsultarNfseServicoTomadoOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )
        Fault: Optional["NfseConsultarNfseServicoTomadoOutput.Body.Fault"] = (
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
class NfseGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseGerarNfseInput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseGerarNfseOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )
        Fault: Optional["NfseGerarNfseOutput.Body.Fault"] = field(
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
class NfseRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseRecepcionarLoteRpsSincronoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincronoRequest: Optional[
            RecepcionarLoteRpsSincronoRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseRecepcionarLoteRpsSincronoOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )
        Fault: Optional["NfseRecepcionarLoteRpsSincronoOutput.Body.Fault"] = (
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
class NfseRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://nfse.abrasf.org.br",
                },
            )
        )
        Fault: Optional["NfseRecepcionarLoteRpsOutput.Body.Fault"] = field(
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
class NfseSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSubstituirNfseInput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )


@dataclass
class NfseSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseSubstituirNfseOutput.Body"] = field(
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
                "namespace": "http://nfse.abrasf.org.br",
            },
        )
        Fault: Optional["NfseSubstituirNfseOutput.Body.Fault"] = field(
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


class NfseCancelarNfse:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/CancelarNfse"
    input = NfseCancelarNfseInput
    output = NfseCancelarNfseOutput


class NfseConsultarLoteRps:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarLoteRps"
    input = NfseConsultarLoteRpsInput
    output = NfseConsultarLoteRpsOutput


class NfseConsultarNfsePorFaixa:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarNfsePorFaixa"
    input = NfseConsultarNfsePorFaixaInput
    output = NfseConsultarNfsePorFaixaOutput


class NfseConsultarNfsePorRps:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarNfsePorRps"
    input = NfseConsultarNfsePorRpsInput
    output = NfseConsultarNfsePorRpsOutput


class NfseConsultarNfseServicoPrestado:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarNfseServicoPrestado"
    input = NfseConsultarNfseServicoPrestadoInput
    output = NfseConsultarNfseServicoPrestadoOutput


class NfseConsultarNfseServicoTomado:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/ConsultarNfseServicoTomado"
    input = NfseConsultarNfseServicoTomadoInput
    output = NfseConsultarNfseServicoTomadoOutput


class NfseGerarNfse:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/GerarNfse"
    input = NfseGerarNfseInput
    output = NfseGerarNfseOutput


class NfseRecepcionarLoteRps:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/RecepcionarLoteRps"
    input = NfseRecepcionarLoteRpsInput
    output = NfseRecepcionarLoteRpsOutput


class NfseRecepcionarLoteRpsSincrono:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/RecepcionarLoteRpsSincrono"
    input = NfseRecepcionarLoteRpsSincronoInput
    output = NfseRecepcionarLoteRpsSincronoOutput


class NfseSubstituirNfse:
    style = "document"
    location = "https://ws.nfe-cidades.com.br/ws/pocos"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://nfse.abrasf.org.br/SubstituirNfse"
    input = NfseSubstituirNfseInput
    output = NfseSubstituirNfseOutput
