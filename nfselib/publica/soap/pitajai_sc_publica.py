from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://service.nfse.integracao.ws.publica/"


@dataclass
class CancelarDirEnvio:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarDirEnvioResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CartaCorrecaoNfseEnvio:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CartaCorrecaoNfseEnvioResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarDirEnvio:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarDirEnvioResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarDirFaixa:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarDirFaixaResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteDir:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteDirResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

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
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

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
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseFaixaResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

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
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseRecebida:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseRecebidaResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSituacaoLoteDir:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSituacaoLoteDirResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSituacaoLoteRps:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

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
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteDir:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteDirResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

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
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

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
        namespace = "http://service.nfse.integracao.ws.publica/"

    XML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SubstituirNfseResponse:
    class Meta:
        namespace = "http://service.nfse.integracao.ws.publica/"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ServicesCancelarDirEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesCancelarDirEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarDirEnvio: Optional[CancelarDirEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesCancelarDirEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesCancelarDirEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarDirEnvioResponse: Optional[CancelarDirEnvioResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesCancelarDirEnvioOutput.Body.Fault"] = field(
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
class ServicesCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesCancelarNfseInput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesCancelarNfseOutput.Body.Fault"] = field(
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
class ServicesCartaCorrecaoNfseEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesCartaCorrecaoNfseEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CartaCorrecaoNfseEnvio: Optional[CartaCorrecaoNfseEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesCartaCorrecaoNfseEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesCartaCorrecaoNfseEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CartaCorrecaoNfseEnvioResponse: Optional[
            CartaCorrecaoNfseEnvioResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesCartaCorrecaoNfseEnvioOutput.Body.Fault"] = (
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
class ServicesConsultarDirEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarDirEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarDirEnvio: Optional[ConsultarDirEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarDirEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarDirEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarDirEnvioResponse: Optional[ConsultarDirEnvioResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesConsultarDirEnvioOutput.Body.Fault"] = field(
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
class ServicesConsultarDirFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarDirFaixaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarDirFaixa: Optional[ConsultarDirFaixa] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarDirFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarDirFaixaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarDirFaixaResponse: Optional[ConsultarDirFaixaResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesConsultarDirFaixaOutput.Body.Fault"] = field(
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
class ServicesConsultarLoteDirInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarLoteDirInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteDir: Optional[ConsultarLoteDir] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarLoteDirOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarLoteDirOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteDirResponse: Optional[ConsultarLoteDirResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesConsultarLoteDirOutput.Body.Fault"] = field(
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
class ServicesConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesConsultarLoteRpsOutput.Body.Fault"] = field(
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
class ServicesConsultarNfseFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarNfseFaixaInput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarNfseFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarNfseFaixaOutput.Body"] = field(
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
                    "namespace": "http://service.nfse.integracao.ws.publica/",
                },
            )
        )
        Fault: Optional["ServicesConsultarNfseFaixaOutput.Body.Fault"] = field(
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
class ServicesConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarNfsePorRpsInput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "http://service.nfse.integracao.ws.publica/",
                },
            )
        )
        Fault: Optional["ServicesConsultarNfsePorRpsOutput.Body.Fault"] = (
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
class ServicesConsultarNfseRecebidaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarNfseRecebidaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRecebida: Optional[ConsultarNfseRecebida] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarNfseRecebidaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarNfseRecebidaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRecebidaResponse: Optional[
            ConsultarNfseRecebidaResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesConsultarNfseRecebidaOutput.Body.Fault"] = (
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
class ServicesConsultarSituacaoLoteDirInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarSituacaoLoteDirInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteDir: Optional[ConsultarSituacaoLoteDir] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarSituacaoLoteDirOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarSituacaoLoteDirOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteDirResponse: Optional[
            ConsultarSituacaoLoteDirResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional[
            "ServicesConsultarSituacaoLoteDirOutput.Body.Fault"
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
class ServicesConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRps: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesConsultarSituacaoLoteRpsOutput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional[
            "ServicesConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class ServicesGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesGerarNfseInput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesGerarNfseOutput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesGerarNfseOutput.Body.Fault"] = field(
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
class ServicesRecepcionarLoteDirInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesRecepcionarLoteDirInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteDir: Optional[RecepcionarLoteDir] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesRecepcionarLoteDirOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesRecepcionarLoteDirOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteDirResponse: Optional[RecepcionarLoteDirResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://service.nfse.integracao.ws.publica/",
                },
            )
        )
        Fault: Optional["ServicesRecepcionarLoteDirOutput.Body.Fault"] = field(
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
class ServicesRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://service.nfse.integracao.ws.publica/",
                },
            )
        )
        Fault: Optional["ServicesRecepcionarLoteRpsOutput.Body.Fault"] = field(
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
class ServicesSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesSubstituirNfseInput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )


@dataclass
class ServicesSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicesSubstituirNfseOutput.Body"] = field(
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
                "namespace": "http://service.nfse.integracao.ws.publica/",
            },
        )
        Fault: Optional["ServicesSubstituirNfseOutput.Body.Fault"] = field(
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


class ServicesCancelarDirEnvio:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesCancelarDirEnvioInput
    output = ServicesCancelarDirEnvioOutput


class ServicesCancelarNfse:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesCancelarNfseInput
    output = ServicesCancelarNfseOutput


class ServicesCartaCorrecaoNfseEnvio:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesCartaCorrecaoNfseEnvioInput
    output = ServicesCartaCorrecaoNfseEnvioOutput


class ServicesConsultarDirEnvio:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarDirEnvioInput
    output = ServicesConsultarDirEnvioOutput


class ServicesConsultarDirFaixa:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarDirFaixaInput
    output = ServicesConsultarDirFaixaOutput


class ServicesConsultarLoteDir:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarLoteDirInput
    output = ServicesConsultarLoteDirOutput


class ServicesConsultarLoteRps:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarLoteRpsInput
    output = ServicesConsultarLoteRpsOutput


class ServicesConsultarNfseFaixa:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarNfseFaixaInput
    output = ServicesConsultarNfseFaixaOutput


class ServicesConsultarNfsePorRps:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarNfsePorRpsInput
    output = ServicesConsultarNfsePorRpsOutput


class ServicesConsultarNfseRecebida:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarNfseRecebidaInput
    output = ServicesConsultarNfseRecebidaOutput


class ServicesConsultarSituacaoLoteDir:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarSituacaoLoteDirInput
    output = ServicesConsultarSituacaoLoteDirOutput


class ServicesConsultarSituacaoLoteRps:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesConsultarSituacaoLoteRpsInput
    output = ServicesConsultarSituacaoLoteRpsOutput


class ServicesGerarNfse:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesGerarNfseInput
    output = ServicesGerarNfseOutput


class ServicesRecepcionarLoteDir:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesRecepcionarLoteDirInput
    output = ServicesRecepcionarLoteDirOutput


class ServicesRecepcionarLoteRps:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesRecepcionarLoteRpsInput
    output = ServicesRecepcionarLoteRpsOutput


class ServicesSubstituirNfse:
    style = "rpc"
    location = "https://nfse.itajai.sc.gov.br:443/nfse_integracao/Services"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ServicesSubstituirNfseInput
    output = ServicesSubstituirNfseOutput
