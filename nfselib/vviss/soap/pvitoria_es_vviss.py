from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    CancelarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseFaixa:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseFaixaResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarNfseFaixaResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarNfsePorRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoPrestado:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarNfseServicoPrestadoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoTomado:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoTomadoResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarNfseServicoTomadoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    GerarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    RecepcionarLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsSincrono:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    RecepcionarLoteRpsSincronoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SubstituirNfse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    mensagemXML: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SubstituirNfseResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    SubstituirNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class NotaFiscalServiceSoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapCancelarNfseInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class NotaFiscalServiceSoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "NotaFiscalServiceSoapCancelarNfseOutput.Body.Fault"
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
class NotaFiscalServiceSoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class NotaFiscalServiceSoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "NotaFiscalServiceSoapConsultarLoteRpsOutput.Body.Fault"
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
class NotaFiscalServiceSoapConsultarNfseFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapConsultarNfseFaixaInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseFaixa: Optional[ConsultarNfseFaixa] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class NotaFiscalServiceSoapConsultarNfseFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapConsultarNfseFaixaOutput.Body"] = (
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
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                },
            )
        )
        Fault: Optional[
            "NotaFiscalServiceSoapConsultarNfseFaixaOutput.Body.Fault"
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
class NotaFiscalServiceSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapConsultarNfsePorRpsInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfsePorRps: Optional[ConsultarNfsePorRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class NotaFiscalServiceSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapConsultarNfsePorRpsOutput.Body"] = (
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
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                },
            )
        )
        Fault: Optional[
            "NotaFiscalServiceSoapConsultarNfsePorRpsOutput.Body.Fault"
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
class NotaFiscalServiceSoapConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NotaFiscalServiceSoapConsultarNfseServicoPrestadoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoPrestado: Optional[
            ConsultarNfseServicoPrestado
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class NotaFiscalServiceSoapConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NotaFiscalServiceSoapConsultarNfseServicoPrestadoOutput.Body"
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "NotaFiscalServiceSoapConsultarNfseServicoPrestadoOutput.Body.Fault"
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
class NotaFiscalServiceSoapConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NotaFiscalServiceSoapConsultarNfseServicoTomadoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoTomado: Optional[ConsultarNfseServicoTomado] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                },
            )
        )


@dataclass
class NotaFiscalServiceSoapConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NotaFiscalServiceSoapConsultarNfseServicoTomadoOutput.Body"
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "NotaFiscalServiceSoapConsultarNfseServicoTomadoOutput.Body.Fault"
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
class NotaFiscalServiceSoapGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapGerarNfseInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class NotaFiscalServiceSoapGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapGerarNfseOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional["NotaFiscalServiceSoapGerarNfseOutput.Body.Fault"] = (
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
class NotaFiscalServiceSoapRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NotaFiscalServiceSoapRecepcionarLoteRpsSincronoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincrono: Optional[RecepcionarLoteRpsSincrono] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                },
            )
        )


@dataclass
class NotaFiscalServiceSoapRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NotaFiscalServiceSoapRecepcionarLoteRpsSincronoOutput.Body"
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "NotaFiscalServiceSoapRecepcionarLoteRpsSincronoOutput.Body.Fault"
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
class NotaFiscalServiceSoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapRecepcionarLoteRpsInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteRps: Optional[RecepcionarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class NotaFiscalServiceSoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapRecepcionarLoteRpsOutput.Body"] = (
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
                    "namespace": "http://www.abrasf.org.br/nfse.xsd",
                },
            )
        )
        Fault: Optional[
            "NotaFiscalServiceSoapRecepcionarLoteRpsOutput.Body.Fault"
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
class NotaFiscalServiceSoapSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapSubstituirNfseInput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class NotaFiscalServiceSoapSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NotaFiscalServiceSoapSubstituirNfseOutput.Body"] = field(
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
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "NotaFiscalServiceSoapSubstituirNfseOutput.Body.Fault"
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


class NotaFiscalServiceSoapCancelarNfse:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/CancelarNfse"
    input = NotaFiscalServiceSoapCancelarNfseInput
    output = NotaFiscalServiceSoapCancelarNfseOutput


class NotaFiscalServiceSoapConsultarLoteRps:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/ConsultarLoteRps"
    input = NotaFiscalServiceSoapConsultarLoteRpsInput
    output = NotaFiscalServiceSoapConsultarLoteRpsOutput


class NotaFiscalServiceSoapConsultarNfseFaixa:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/ConsultarNfseFaixa"
    input = NotaFiscalServiceSoapConsultarNfseFaixaInput
    output = NotaFiscalServiceSoapConsultarNfseFaixaOutput


class NotaFiscalServiceSoapConsultarNfsePorRps:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/ConsultarNfsePorRps"
    input = NotaFiscalServiceSoapConsultarNfsePorRpsInput
    output = NotaFiscalServiceSoapConsultarNfsePorRpsOutput


class NotaFiscalServiceSoapConsultarNfseServicoPrestado:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.abrasf.org.br/nfse.xsd/ConsultarNfseServicoPrestado"
    )
    input = NotaFiscalServiceSoapConsultarNfseServicoPrestadoInput
    output = NotaFiscalServiceSoapConsultarNfseServicoPrestadoOutput


class NotaFiscalServiceSoapConsultarNfseServicoTomado:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/ConsultarNfseServicoTomado"
    input = NotaFiscalServiceSoapConsultarNfseServicoTomadoInput
    output = NotaFiscalServiceSoapConsultarNfseServicoTomadoOutput


class NotaFiscalServiceSoapGerarNfse:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/GerarNfse"
    input = NotaFiscalServiceSoapGerarNfseInput
    output = NotaFiscalServiceSoapGerarNfseOutput


class NotaFiscalServiceSoapRecepcionarLoteRps:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/RecepcionarLoteRps"
    input = NotaFiscalServiceSoapRecepcionarLoteRpsInput
    output = NotaFiscalServiceSoapRecepcionarLoteRpsOutput


class NotaFiscalServiceSoapRecepcionarLoteRpsSincrono:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/RecepcionarLoteRpsSincrono"
    input = NotaFiscalServiceSoapRecepcionarLoteRpsSincronoInput
    output = NotaFiscalServiceSoapRecepcionarLoteRpsSincronoOutput


class NotaFiscalServiceSoapSubstituirNfse:
    style = "document"
    location = (
        "https://wsnfse.vitoria.es.gov.br/Producao/NotaFiscalService.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/SubstituirNfse"
    input = NotaFiscalServiceSoapSubstituirNfseInput
    output = NotaFiscalServiceSoapSubstituirNfseOutput
