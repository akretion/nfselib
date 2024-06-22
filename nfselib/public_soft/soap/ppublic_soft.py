from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:index.GerarNfseEnvio"


@dataclass
class CancelarNfseEnvioRequest:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarNfseEnvioResponse:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseFaixaEnvioRequest:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseFaixaEnvioResponse:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseRpsEnvioRequest:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseRpsEnvioResponse:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoEnvioRequest:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoEnvioResponse:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseEnvioRequest:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseEnvioResponse:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class LinksNotaFiscalRequest:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class LinksNotaFiscalResponse:
    class Meta:
        namespace = "urn:index.GerarNfseEnvio"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class IndexGerarNfseEnvioPortTypeCancelarNfseEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IndexGerarNfseEnvioPortTypeCancelarNfseEnvioInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseEnvio: Optional[CancelarNfseEnvioRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.CancelarNfseEnvio",
            },
        )


@dataclass
class IndexGerarNfseEnvioPortTypeCancelarNfseEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IndexGerarNfseEnvioPortTypeCancelarNfseEnvioOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseEnvioResponse: Optional[CancelarNfseEnvioResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.CancelarNfseEnvio",
            },
        )
        Fault: Optional[
            "IndexGerarNfseEnvioPortTypeCancelarNfseEnvioOutput.Body.Fault"
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
class IndexGerarNfseEnvioPortTypeConsultarNfseFaixaEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IndexGerarNfseEnvioPortTypeConsultarNfseFaixaEnvioInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseFaixaEnvio: Optional[ConsultarNfseFaixaEnvioRequest] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn:index.ConsultarNfseFaixaEnvio",
                },
            )
        )


@dataclass
class IndexGerarNfseEnvioPortTypeConsultarNfseFaixaEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IndexGerarNfseEnvioPortTypeConsultarNfseFaixaEnvioOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseFaixaEnvioResponse: Optional[
            ConsultarNfseFaixaEnvioResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.ConsultarNfseFaixaEnvio",
            },
        )
        Fault: Optional[
            "IndexGerarNfseEnvioPortTypeConsultarNfseFaixaEnvioOutput.Body.Fault"
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
class IndexGerarNfseEnvioPortTypeConsultarNfseRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IndexGerarNfseEnvioPortTypeConsultarNfseRpsEnvioInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRpsEnvio: Optional[ConsultarNfseRpsEnvioRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.ConsultarNfseRpsEnvio",
            },
        )


@dataclass
class IndexGerarNfseEnvioPortTypeConsultarNfseRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IndexGerarNfseEnvioPortTypeConsultarNfseRpsEnvioOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRpsEnvioResponse: Optional[
            ConsultarNfseRpsEnvioResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.ConsultarNfseRpsEnvio",
            },
        )
        Fault: Optional[
            "IndexGerarNfseEnvioPortTypeConsultarNfseRpsEnvioOutput.Body.Fault"
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
class IndexGerarNfseEnvioPortTypeConsultarNfseServicoPrestadoEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IndexGerarNfseEnvioPortTypeConsultarNfseServicoPrestadoEnvioInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoPrestadoEnvio: Optional[
            ConsultarNfseServicoPrestadoEnvioRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.ConsultarNfseServicoPrestadoEnvio",
            },
        )


@dataclass
class IndexGerarNfseEnvioPortTypeConsultarNfseServicoPrestadoEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "IndexGerarNfseEnvioPortTypeConsultarNfseServicoPrestadoEnvioOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoPrestadoEnvioResponse: Optional[
            ConsultarNfseServicoPrestadoEnvioResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.ConsultarNfseServicoPrestadoEnvio",
            },
        )
        Fault: Optional[
            "IndexGerarNfseEnvioPortTypeConsultarNfseServicoPrestadoEnvioOutput.Body.Fault"
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
class IndexGerarNfseEnvioPortTypeGerarNfseEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IndexGerarNfseEnvioPortTypeGerarNfseEnvioInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        GerarNfseEnvio: Optional[GerarNfseEnvioRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.GerarNfseEnvio",
            },
        )


@dataclass
class IndexGerarNfseEnvioPortTypeGerarNfseEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IndexGerarNfseEnvioPortTypeGerarNfseEnvioOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        GerarNfseEnvioResponse: Optional[GerarNfseEnvioResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.GerarNfseEnvio",
            },
        )
        Fault: Optional[
            "IndexGerarNfseEnvioPortTypeGerarNfseEnvioOutput.Body.Fault"
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
class IndexGerarNfseEnvioPortTypeLinksNotaFiscalInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IndexGerarNfseEnvioPortTypeLinksNotaFiscalInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        LinksNotaFiscal: Optional[LinksNotaFiscalRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.LinksNotaFiscal",
            },
        )


@dataclass
class IndexGerarNfseEnvioPortTypeLinksNotaFiscalOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["IndexGerarNfseEnvioPortTypeLinksNotaFiscalOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        LinksNotaFiscalResponse: Optional[LinksNotaFiscalResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:index.LinksNotaFiscal",
            },
        )
        Fault: Optional[
            "IndexGerarNfseEnvioPortTypeLinksNotaFiscalOutput.Body.Fault"
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


class IndexGerarNfseEnvioPortTypeCancelarNfseEnvio:
    style = "rpc"
    location = "http://portaldocontribuinte.publicsoft.com.br/sistemas/PortalDoContribuinte/views/NotasFiscais/NotaFiscalServico/webservice/producao/index.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:index.CancelarNfseEnvio#CancelarNfseEnvio"
    input = IndexGerarNfseEnvioPortTypeCancelarNfseEnvioInput
    output = IndexGerarNfseEnvioPortTypeCancelarNfseEnvioOutput


class IndexGerarNfseEnvioPortTypeConsultarNfseFaixaEnvio:
    style = "rpc"
    location = "http://portaldocontribuinte.publicsoft.com.br/sistemas/PortalDoContribuinte/views/NotasFiscais/NotaFiscalServico/webservice/producao/index.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:index.ConsultarNfseFaixaEnvio#ConsultarNfseFaixaEnvio"
    input = IndexGerarNfseEnvioPortTypeConsultarNfseFaixaEnvioInput
    output = IndexGerarNfseEnvioPortTypeConsultarNfseFaixaEnvioOutput


class IndexGerarNfseEnvioPortTypeConsultarNfseRpsEnvio:
    style = "rpc"
    location = "http://portaldocontribuinte.publicsoft.com.br/sistemas/PortalDoContribuinte/views/NotasFiscais/NotaFiscalServico/webservice/producao/index.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:index.ConsultarNfseRpsEnvio#ConsultarNfseRpsEnvio"
    input = IndexGerarNfseEnvioPortTypeConsultarNfseRpsEnvioInput
    output = IndexGerarNfseEnvioPortTypeConsultarNfseRpsEnvioOutput


class IndexGerarNfseEnvioPortTypeConsultarNfseServicoPrestadoEnvio:
    style = "rpc"
    location = "http://portaldocontribuinte.publicsoft.com.br/sistemas/PortalDoContribuinte/views/NotasFiscais/NotaFiscalServico/webservice/producao/index.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:index.ConsultarNfseServicoPrestadoEnvio#ConsultarNfseServicoPrestadoEnvio"
    input = IndexGerarNfseEnvioPortTypeConsultarNfseServicoPrestadoEnvioInput
    output = IndexGerarNfseEnvioPortTypeConsultarNfseServicoPrestadoEnvioOutput


class IndexGerarNfseEnvioPortTypeGerarNfseEnvio:
    style = "rpc"
    location = "http://portaldocontribuinte.publicsoft.com.br/sistemas/PortalDoContribuinte/views/NotasFiscais/NotaFiscalServico/webservice/producao/index.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:index.GerarNfseEnvio#GerarNfseEnvio"
    input = IndexGerarNfseEnvioPortTypeGerarNfseEnvioInput
    output = IndexGerarNfseEnvioPortTypeGerarNfseEnvioOutput


class IndexGerarNfseEnvioPortTypeLinksNotaFiscal:
    style = "rpc"
    location = "http://portaldocontribuinte.publicsoft.com.br/sistemas/PortalDoContribuinte/views/NotasFiscais/NotaFiscalServico/webservice/producao/index.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:index.LinksNotaFiscal#LinksNotaFiscal"
    input = IndexGerarNfseEnvioPortTypeLinksNotaFiscalInput
    output = IndexGerarNfseEnvioPortTypeLinksNotaFiscalOutput
