from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://ws.integracao.nfsd.desenvolve/"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        name = "cancelarNfseEnvio"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarNfseEnvioResponse:
    class Meta:
        name = "cancelarNfseEnvioResponse"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        name = "consultarLoteRpsEnvio"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsEnvioResponse:
    class Meta:
        name = "consultarLoteRpsEnvioResponse"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        name = "consultarNfseRpsEnvio"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseRpsEnvioResponse:
    class Meta:
        name = "consultarNfseRpsEnvioResponse"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        name = "enviarLoteRpsEnvio"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EnviarLoteRpsEnvioResponse:
    class Meta:
        name = "enviarLoteRpsEnvioResponse"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EnviarLoteRpsSincronoEnvio:
    class Meta:
        name = "enviarLoteRpsSincronoEnvio"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EnviarLoteRpsSincronoEnvioResponse:
    class Meta:
        name = "enviarLoteRpsSincronoEnvioResponse"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseEnvio:
    class Meta:
        name = "gerarNfseEnvio"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseEnvioResponse:
    class Meta:
        name = "gerarNfseEnvioResponse"
        namespace = "http://ws.integracao.nfsd.desenvolve/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class IintegracaoNfsdCancelarNfseEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdCancelarNfseEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancelarNfseEnvio: Optional[CancelarNfseEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )


@dataclass
class IintegracaoNfsdCancelarNfseEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdCancelarNfseEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancelarNfseEnvioResponse: Optional[CancelarNfseEnvioResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )
        Fault: Optional[
            "IintegracaoNfsdCancelarNfseEnvioOutput.Body.Fault"
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
class IintegracaoNfsdConsultarLoteRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdConsultarLoteRpsEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarLoteRpsEnvio: Optional[ConsultarLoteRpsEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )


@dataclass
class IintegracaoNfsdConsultarLoteRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdConsultarLoteRpsEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarLoteRpsEnvioResponse: Optional[
            ConsultarLoteRpsEnvioResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )
        Fault: Optional[
            "IintegracaoNfsdConsultarLoteRpsEnvioOutput.Body.Fault"
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
class IintegracaoNfsdConsultarNfseRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdConsultarNfseRpsEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarNfseRpsEnvio: Optional[ConsultarNfseRpsEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )


@dataclass
class IintegracaoNfsdConsultarNfseRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdConsultarNfseRpsEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarNfseRpsEnvioResponse: Optional[
            ConsultarNfseRpsEnvioResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )
        Fault: Optional[
            "IintegracaoNfsdConsultarNfseRpsEnvioOutput.Body.Fault"
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
class IintegracaoNfsdEnviarLoteRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdEnviarLoteRpsEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        enviarLoteRpsEnvio: Optional[EnviarLoteRpsEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )


@dataclass
class IintegracaoNfsdEnviarLoteRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdEnviarLoteRpsEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        enviarLoteRpsEnvioResponse: Optional[EnviarLoteRpsEnvioResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.integracao.nfsd.desenvolve/",
                },
            )
        )
        Fault: Optional[
            "IintegracaoNfsdEnviarLoteRpsEnvioOutput.Body.Fault"
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
class IintegracaoNfsdEnviarLoteRpsSincronoEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdEnviarLoteRpsSincronoEnvioInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        enviarLoteRpsSincronoEnvio: Optional[EnviarLoteRpsSincronoEnvio] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.integracao.nfsd.desenvolve/",
                },
            )
        )


@dataclass
class IintegracaoNfsdEnviarLoteRpsSincronoEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdEnviarLoteRpsSincronoEnvioOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        enviarLoteRpsSincronoEnvioResponse: Optional[
            EnviarLoteRpsSincronoEnvioResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )
        Fault: Optional[
            "IintegracaoNfsdEnviarLoteRpsSincronoEnvioOutput.Body.Fault"
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
class IintegracaoNfsdGerarNfseEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdGerarNfseEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gerarNfseEnvio: Optional[GerarNfseEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )


@dataclass
class IintegracaoNfsdGerarNfseEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IintegracaoNfsdGerarNfseEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gerarNfseEnvioResponse: Optional[GerarNfseEnvioResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integracao.nfsd.desenvolve/",
            },
        )
        Fault: Optional["IintegracaoNfsdGerarNfseEnvioOutput.Body.Fault"] = (
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


class IintegracaoNfsdCancelarNfseEnvio:
    style = "rpc"
    location = (
        "https://paragominas.desenvolvecidade.com.br/nfsd/IntegracaoNfsd"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = IintegracaoNfsdCancelarNfseEnvioInput
    output = IintegracaoNfsdCancelarNfseEnvioOutput


class IintegracaoNfsdConsultarLoteRpsEnvio:
    style = "rpc"
    location = (
        "https://paragominas.desenvolvecidade.com.br/nfsd/IntegracaoNfsd"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = IintegracaoNfsdConsultarLoteRpsEnvioInput
    output = IintegracaoNfsdConsultarLoteRpsEnvioOutput


class IintegracaoNfsdConsultarNfseRpsEnvio:
    style = "rpc"
    location = (
        "https://paragominas.desenvolvecidade.com.br/nfsd/IntegracaoNfsd"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = IintegracaoNfsdConsultarNfseRpsEnvioInput
    output = IintegracaoNfsdConsultarNfseRpsEnvioOutput


class IintegracaoNfsdEnviarLoteRpsEnvio:
    style = "rpc"
    location = (
        "https://paragominas.desenvolvecidade.com.br/nfsd/IntegracaoNfsd"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = IintegracaoNfsdEnviarLoteRpsEnvioInput
    output = IintegracaoNfsdEnviarLoteRpsEnvioOutput


class IintegracaoNfsdEnviarLoteRpsSincronoEnvio:
    style = "rpc"
    location = (
        "https://paragominas.desenvolvecidade.com.br/nfsd/IntegracaoNfsd"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = IintegracaoNfsdEnviarLoteRpsSincronoEnvioInput
    output = IintegracaoNfsdEnviarLoteRpsSincronoEnvioOutput


class IintegracaoNfsdGerarNfseEnvio:
    style = "rpc"
    location = (
        "https://paragominas.desenvolvecidade.com.br/nfsd/IntegracaoNfsd"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = IintegracaoNfsdGerarNfseEnvioInput
    output = IintegracaoNfsdGerarNfseEnvioOutput
