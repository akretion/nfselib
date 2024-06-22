from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class Input:
    class Meta:
        name = "input"

    nfseCabecMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            "required": True,
        },
    )
    nfseDadosMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
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
            "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            "required": True,
        },
    )


@dataclass
class CancelarNfseRequest(Input):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class CancelarNfseResponse(Output):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class ConsultarLoteRpsRequest(Input):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class ConsultarLoteRpsResponse(Output):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class ConsultarNfseFaixaRequest(Input):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class ConsultarNfseFaixaResponse(Output):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class ConsultarNfsePorRpsRequest(Input):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class ConsultarNfsePorRpsResponse(Output):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class GerarNfseRequest(Input):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class GerarNfseResponse(Output):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class RecepcionarLoteRpsRequest(Input):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class RecepcionarLoteRpsResponse(Output):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class RecepcionarLoteRpsSincronoRequest(Input):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class RecepcionarLoteRpsSincronoResponse(Output):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class SubstituirNfseRequest(Input):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class SubstituirNfseResponse(Output):
    class Meta:
        namespace = "http://webservice.ereceita.net.br/soap/NfseWebService"


@dataclass
class NfseWebServicePortTypeCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeCancelarNfseInput.Body"] = field(
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )


@dataclass
class NfseWebServicePortTypeCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )
        Fault: Optional[
            "NfseWebServicePortTypeCancelarNfseOutput.Body.Fault"
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
class NfseWebServicePortTypeConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )


@dataclass
class NfseWebServicePortTypeConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeConsultarLoteRpsOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarLoteRpsResponse: Optional[ConsultarLoteRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )
        Fault: Optional[
            "NfseWebServicePortTypeConsultarLoteRpsOutput.Body.Fault"
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
class NfseWebServicePortTypeConsultarNfseFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeConsultarNfseFaixaInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseFaixaRequest: Optional[ConsultarNfseFaixaRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )


@dataclass
class NfseWebServicePortTypeConsultarNfseFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeConsultarNfseFaixaOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseFaixaResponse: Optional[ConsultarNfseFaixaResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
                },
            )
        )
        Fault: Optional[
            "NfseWebServicePortTypeConsultarNfseFaixaOutput.Body.Fault"
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
class NfseWebServicePortTypeConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeConsultarNfsePorRpsInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsRequest: Optional[ConsultarNfsePorRpsRequest] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
                },
            )
        )


@dataclass
class NfseWebServicePortTypeConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeConsultarNfsePorRpsOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfsePorRpsResponse: Optional[ConsultarNfsePorRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
                },
            )
        )
        Fault: Optional[
            "NfseWebServicePortTypeConsultarNfsePorRpsOutput.Body.Fault"
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
class NfseWebServicePortTypeGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeGerarNfseInput.Body"] = field(
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )


@dataclass
class NfseWebServicePortTypeGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeGerarNfseOutput.Body"] = field(
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )
        Fault: Optional["NfseWebServicePortTypeGerarNfseOutput.Body.Fault"] = (
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
class NfseWebServicePortTypeRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfseWebServicePortTypeRecepcionarLoteRpsSincronoInput.Body"
    ] = field(
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )


@dataclass
class NfseWebServicePortTypeRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfseWebServicePortTypeRecepcionarLoteRpsSincronoOutput.Body"
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )
        Fault: Optional[
            "NfseWebServicePortTypeRecepcionarLoteRpsSincronoOutput.Body.Fault"
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
class NfseWebServicePortTypeRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeRecepcionarLoteRpsInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsRequest: Optional[RecepcionarLoteRpsRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )


@dataclass
class NfseWebServicePortTypeRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeRecepcionarLoteRpsOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsResponse: Optional[RecepcionarLoteRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
                },
            )
        )
        Fault: Optional[
            "NfseWebServicePortTypeRecepcionarLoteRpsOutput.Body.Fault"
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
class NfseWebServicePortTypeSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeSubstituirNfseInput.Body"] = field(
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )


@dataclass
class NfseWebServicePortTypeSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWebServicePortTypeSubstituirNfseOutput.Body"] = field(
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
                "namespace": "http://webservice.ereceita.net.br/soap/NfseWebService",
            },
        )
        Fault: Optional[
            "NfseWebServicePortTypeSubstituirNfseOutput.Body.Fault"
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


class NfseWebServicePortTypeCancelarNfse:
    style = "document"
    location = (
        "https://webservice.ereceita.net.br:443/ws/ssparaiso/wsProducao.php"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.ereceita.net.br/CancelarNfse"
    input = NfseWebServicePortTypeCancelarNfseInput
    output = NfseWebServicePortTypeCancelarNfseOutput


class NfseWebServicePortTypeConsultarLoteRps:
    style = "document"
    location = (
        "https://webservice.ereceita.net.br:443/ws/ssparaiso/wsProducao.php"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.ereceita.net.br/ConsultarLoteRps"
    input = NfseWebServicePortTypeConsultarLoteRpsInput
    output = NfseWebServicePortTypeConsultarLoteRpsOutput


class NfseWebServicePortTypeConsultarNfseFaixa:
    style = "document"
    location = (
        "https://webservice.ereceita.net.br:443/ws/ssparaiso/wsProducao.php"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.ereceita.net.br/ConsultarNfseFaixa"
    input = NfseWebServicePortTypeConsultarNfseFaixaInput
    output = NfseWebServicePortTypeConsultarNfseFaixaOutput


class NfseWebServicePortTypeConsultarNfsePorRps:
    style = "document"
    location = (
        "https://webservice.ereceita.net.br:443/ws/ssparaiso/wsProducao.php"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.ereceita.net.br/ConsultarNfsePorRps"
    input = NfseWebServicePortTypeConsultarNfsePorRpsInput
    output = NfseWebServicePortTypeConsultarNfsePorRpsOutput


class NfseWebServicePortTypeGerarNfse:
    style = "document"
    location = (
        "https://webservice.ereceita.net.br:443/ws/ssparaiso/wsProducao.php"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.ereceita.net.br/GerarNfse"
    input = NfseWebServicePortTypeGerarNfseInput
    output = NfseWebServicePortTypeGerarNfseOutput


class NfseWebServicePortTypeRecepcionarLoteRps:
    style = "document"
    location = (
        "https://webservice.ereceita.net.br:443/ws/ssparaiso/wsProducao.php"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.ereceita.net.br/RecepcionarLoteRps"
    input = NfseWebServicePortTypeRecepcionarLoteRpsInput
    output = NfseWebServicePortTypeRecepcionarLoteRpsOutput


class NfseWebServicePortTypeRecepcionarLoteRpsSincrono:
    style = "document"
    location = (
        "https://webservice.ereceita.net.br:443/ws/ssparaiso/wsProducao.php"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.ereceita.net.br/RecepcionarLoteRpsSincrono"
    input = NfseWebServicePortTypeRecepcionarLoteRpsSincronoInput
    output = NfseWebServicePortTypeRecepcionarLoteRpsSincronoOutput


class NfseWebServicePortTypeSubstituirNfse:
    style = "document"
    location = (
        "https://webservice.ereceita.net.br:443/ws/ssparaiso/wsProducao.php"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "https://www.ereceita.net.br/SubstituirNfse"
    input = NfseWebServicePortTypeSubstituirNfseInput
    output = NfseWebServicePortTypeSubstituirNfseOutput
