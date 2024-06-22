from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://nfe.sdolivramento.com.br/webservice/index/producao"


@dataclass
class CancelarNfseRequest:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

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
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsResquest:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRpsRequest:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

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
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseRequest:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsRequest:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsRequest:
    class Meta:
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

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
        namespace = (
            "https://nfe.sdolivramento.com.br/webservice/index/producao"
        )

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class DbsellerPortCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfse: Optional[CancelarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )


@dataclass
class DbsellerPortCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortCancelarNfseOutput.Body"] = field(
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
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )
        Fault: Optional["DbsellerPortCancelarNfseOutput.Body.Fault"] = field(
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
class DbsellerPortConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRps: Optional[ConsultarLoteRpsResquest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )


@dataclass
class DbsellerPortConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )
        Fault: Optional["DbsellerPortConsultarLoteRpsOutput.Body.Fault"] = (
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
class DbsellerPortConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorRps: Optional[ConsultarNfsePorRpsRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )


@dataclass
class DbsellerPortConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
                },
            )
        )
        Fault: Optional["DbsellerPortConsultarNfsePorRpsOutput.Body.Fault"] = (
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
class DbsellerPortConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfse: Optional[ConsultarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )


@dataclass
class DbsellerPortConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortConsultarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseResponse: Optional[ConsultarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )
        Fault: Optional["DbsellerPortConsultarNfseOutput.Body.Fault"] = field(
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
class DbsellerPortConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRps: Optional[ConsultarSituacaoLoteRpsRequest] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
                },
            )
        )


@dataclass
class DbsellerPortConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortConsultarSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsResponse: Optional[
            ConsultarSituacaoLoteRpsResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )
        Fault: Optional[
            "DbsellerPortConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class DbsellerPortRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRps: Optional[RecepcionarLoteRpsRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
            },
        )


@dataclass
class DbsellerPortRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["DbsellerPortRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "https://nfe.sdolivramento.com.br/webservice/index/producao",
                },
            )
        )
        Fault: Optional["DbsellerPortRecepcionarLoteRpsOutput.Body.Fault"] = (
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


class DbsellerPortCancelarNfse:
    style = "rpc"
    location = "https://nfe.sdolivramento.com.br/webservice/index/producao"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = DbsellerPortCancelarNfseInput
    output = DbsellerPortCancelarNfseOutput


class DbsellerPortConsultarLoteRps:
    style = "rpc"
    location = "https://nfe.sdolivramento.com.br/webservice/index/producao"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = DbsellerPortConsultarLoteRpsInput
    output = DbsellerPortConsultarLoteRpsOutput


class DbsellerPortConsultarNfse:
    style = "rpc"
    location = "https://nfe.sdolivramento.com.br/webservice/index/producao"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = DbsellerPortConsultarNfseInput
    output = DbsellerPortConsultarNfseOutput


class DbsellerPortConsultarNfsePorRps:
    style = "rpc"
    location = "https://nfe.sdolivramento.com.br/webservice/index/producao"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = DbsellerPortConsultarNfsePorRpsInput
    output = DbsellerPortConsultarNfsePorRpsOutput


class DbsellerPortConsultarSituacaoLoteRps:
    style = "rpc"
    location = "https://nfe.sdolivramento.com.br/webservice/index/producao"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = DbsellerPortConsultarSituacaoLoteRpsInput
    output = DbsellerPortConsultarSituacaoLoteRpsOutput


class DbsellerPortRecepcionarLoteRps:
    style = "rpc"
    location = "https://nfe.sdolivramento.com.br/webservice/index/producao"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = DbsellerPortRecepcionarLoteRpsInput
    output = DbsellerPortRecepcionarLoteRpsOutput
