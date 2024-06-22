from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.issnetonline.com.br/webservice/nfd"


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    CancelarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNfsePorRps:
    class Meta:
        name = "ConsultaNFSePorRPS"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNfsePorRpsresponse:
    class Meta:
        name = "ConsultaNFSePorRPSResponse"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultaNFSePorRPSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaSituacaoLoteRps:
    class Meta:
        name = "ConsultaSituacaoLoteRPS"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaSituacaoLoteRpsresponse:
    class Meta:
        name = "ConsultaSituacaoLoteRPSResponse"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultaSituacaoLoteRPSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarDadosCadastrais:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarDadosCadastraisResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultarDadosCadastraisResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultarLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        name = "ConsultarNFSePorRPS"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsresponse:
    class Meta:
        name = "ConsultarNFSePorRPSResponse"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultarNFSePorRPSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRps:
    class Meta:
        name = "ConsultarSituacaoLoteRPS"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsresponse:
    class Meta:
        name = "ConsultarSituacaoLoteRPSResponse"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultarSituacaoLoteRPSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarUrlVisualizacaoNfse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarUrlVisualizacaoNfseResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultarUrlVisualizacaoNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarUrlVisualizacaoNfseSerie:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarUrlVisualizacaoNfseSerieResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    ConsultarUrlVisualizacaoNfseSerieResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    RecepcionarLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ServicosSoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapCancelarNfseInput.Body"] = field(
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
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )
        Fault: Optional["ServicosSoapCancelarNfseOutput.Body.Fault"] = field(
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
class ServicosSoapConsultaNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultaNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultaNFSePorRPS: Optional[ConsultaNfsePorRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultaNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultaNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultaNFSePorRPSResponse: Optional[ConsultaNfsePorRpsresponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.issnetonline.com.br/webservice/nfd",
                },
            )
        )
        Fault: Optional["ServicosSoapConsultaNfsePorRpsOutput.Body.Fault"] = (
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
class ServicosSoapConsultaSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultaSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultaSituacaoLoteRPS: Optional[ConsultaSituacaoLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultaSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultaSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultaSituacaoLoteRPSResponse: Optional[
            ConsultaSituacaoLoteRpsresponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )
        Fault: Optional[
            "ServicosSoapConsultaSituacaoLoteRpsOutput.Body.Fault"
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
class ServicosSoapConsultarDadosCadastraisInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarDadosCadastraisInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarDadosCadastrais: Optional[ConsultarDadosCadastrais] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultarDadosCadastraisOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarDadosCadastraisOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarDadosCadastraisResponse: Optional[
            ConsultarDadosCadastraisResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )
        Fault: Optional[
            "ServicosSoapConsultarDadosCadastraisOutput.Body.Fault"
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
class ServicosSoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )
        Fault: Optional["ServicosSoapConsultarLoteRpsOutput.Body.Fault"] = (
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
class ServicosSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNFSePorRPS: Optional[ConsultarNfsePorRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNFSePorRPSResponse: Optional[ConsultarNfsePorRpsresponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.issnetonline.com.br/webservice/nfd",
                },
            )
        )
        Fault: Optional["ServicosSoapConsultarNfsePorRpsOutput.Body.Fault"] = (
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
class ServicosSoapConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfse: Optional[ConsultarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarNfseOutput.Body"] = field(
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
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )
        Fault: Optional["ServicosSoapConsultarNfseOutput.Body.Fault"] = field(
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
class ServicosSoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRPS: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRPSResponse: Optional[
            ConsultarSituacaoLoteRpsresponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )
        Fault: Optional[
            "ServicosSoapConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class ServicosSoapConsultarUrlVisualizacaoNfseSerieInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ServicosSoapConsultarUrlVisualizacaoNfseSerieInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarUrlVisualizacaoNfseSerie: Optional[
            ConsultarUrlVisualizacaoNfseSerie
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultarUrlVisualizacaoNfseSerieOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ServicosSoapConsultarUrlVisualizacaoNfseSerieOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarUrlVisualizacaoNfseSerieResponse: Optional[
            ConsultarUrlVisualizacaoNfseSerieResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )
        Fault: Optional[
            "ServicosSoapConsultarUrlVisualizacaoNfseSerieOutput.Body.Fault"
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
class ServicosSoapConsultarUrlVisualizacaoNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarUrlVisualizacaoNfseInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarUrlVisualizacaoNfse: Optional[
            ConsultarUrlVisualizacaoNfse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapConsultarUrlVisualizacaoNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapConsultarUrlVisualizacaoNfseOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarUrlVisualizacaoNfseResponse: Optional[
            ConsultarUrlVisualizacaoNfseResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )
        Fault: Optional[
            "ServicosSoapConsultarUrlVisualizacaoNfseOutput.Body.Fault"
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
class ServicosSoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            },
        )


@dataclass
class ServicosSoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ServicosSoapRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://www.issnetonline.com.br/webservice/nfd",
                },
            )
        )
        Fault: Optional["ServicosSoapRecepcionarLoteRpsOutput.Body.Fault"] = (
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


class ServicosSoapCancelarNfse:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.issnetonline.com.br/webservice/nfd/CancelarNfse"
    input = ServicosSoapCancelarNfseInput
    output = ServicosSoapCancelarNfseOutput


class ServicosSoapConsultaNfsePorRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.issnetonline.com.br/webservice/nfd/ConsultaNFSePorRPS"
    )
    input = ServicosSoapConsultaNfsePorRpsInput
    output = ServicosSoapConsultaNfsePorRpsOutput


class ServicosSoapConsultaSituacaoLoteRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.issnetonline.com.br/webservice/nfd/ConsultaSituacaoLoteRPS"
    )
    input = ServicosSoapConsultaSituacaoLoteRpsInput
    output = ServicosSoapConsultaSituacaoLoteRpsOutput


class ServicosSoapConsultarDadosCadastrais:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.issnetonline.com.br/webservice/nfd/ConsultarDadosCadastrais"
    input = ServicosSoapConsultarDadosCadastraisInput
    output = ServicosSoapConsultarDadosCadastraisOutput


class ServicosSoapConsultarLoteRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.issnetonline.com.br/webservice/nfd/ConsultarLoteRps"
    )
    input = ServicosSoapConsultarLoteRpsInput
    output = ServicosSoapConsultarLoteRpsOutput


class ServicosSoapConsultarNfsePorRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.issnetonline.com.br/webservice/nfd/ConsultarNFSePorRPS"
    )
    input = ServicosSoapConsultarNfsePorRpsInput
    output = ServicosSoapConsultarNfsePorRpsOutput


class ServicosSoapConsultarNfse:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.issnetonline.com.br/webservice/nfd/ConsultarNfse"
    input = ServicosSoapConsultarNfseInput
    output = ServicosSoapConsultarNfseOutput


class ServicosSoapConsultarSituacaoLoteRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.issnetonline.com.br/webservice/nfd/ConsultarSituacaoLoteRPS"
    input = ServicosSoapConsultarSituacaoLoteRpsInput
    output = ServicosSoapConsultarSituacaoLoteRpsOutput


class ServicosSoapConsultarUrlVisualizacaoNfse:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.issnetonline.com.br/webservice/nfd/ConsultarUrlVisualizacaoNfse"
    input = ServicosSoapConsultarUrlVisualizacaoNfseInput
    output = ServicosSoapConsultarUrlVisualizacaoNfseOutput


class ServicosSoapConsultarUrlVisualizacaoNfseSerie:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.issnetonline.com.br/webservice/nfd/ConsultarUrlVisualizacaoNfseSerie"
    input = ServicosSoapConsultarUrlVisualizacaoNfseSerieInput
    output = ServicosSoapConsultarUrlVisualizacaoNfseSerieOutput


class ServicosSoapRecepcionarLoteRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/duquedecaxias/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.issnetonline.com.br/webservice/nfd/RecepcionarLoteRps"
    )
    input = ServicosSoapRecepcionarLoteRpsInput
    output = ServicosSoapRecepcionarLoteRpsOutput
