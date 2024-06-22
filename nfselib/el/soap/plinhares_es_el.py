from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://des36.el.com.br:8080/el-issonline/"


@dataclass
class RpsServiceCancelarNfseEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceCancelarNfseEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseEnvio: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceCancelarNfseEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceCancelarNfseEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseEnvioResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceCancelarNfseEnvioOutput.Body.Fault"] = (
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
class RpsServiceCancelarNfseMotivoEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceCancelarNfseMotivoEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseMotivoEnvio: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceCancelarNfseMotivoEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceCancelarNfseMotivoEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarNfseMotivoEnvioResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional[
            "RpsServiceCancelarNfseMotivoEnvioOutput.Body.Fault"
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
class RpsServiceConsultarCnaeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarCnaeInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarCnae: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceConsultarCnaeOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarCnaeOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarCnaeResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceConsultarCnaeOutput.Body.Fault"] = field(
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
class RpsServiceConsultarLoteRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarLoteRpsEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsEnvio: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceConsultarLoteRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarLoteRpsEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRpsEnvioResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceConsultarLoteRpsEnvioOutput.Body.Fault"] = (
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
class RpsServiceConsultarNfseEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarNfseEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseEnvio: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceConsultarNfseEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarNfseEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseEnvioResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceConsultarNfseEnvioOutput.Body.Fault"] = (
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
class RpsServiceConsultarNfseRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarNfseRpsEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRpsEnvio: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceConsultarNfseRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarNfseRpsEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseRpsEnvioResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceConsultarNfseRpsEnvioOutput.Body.Fault"] = (
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
class RpsServiceConsultarSituacaoLoteRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarSituacaoLoteRpsEnvioInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsEnvio: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceConsultarSituacaoLoteRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarSituacaoLoteRpsEnvioOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRpsEnvioResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional[
            "RpsServiceConsultarSituacaoLoteRpsEnvioOutput.Body.Fault"
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
class RpsServiceConsultarUltimaRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarUltimaRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarUltimaRps: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceConsultarUltimaRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarUltimaRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarUltimaRpsResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceConsultarUltimaRpsOutput.Body.Fault"] = (
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
class RpsServiceConsultarUltimoLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarUltimoLoteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarUltimoLote: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceConsultarUltimoLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceConsultarUltimoLoteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarUltimoLoteResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceConsultarUltimoLoteOutput.Body.Fault"] = (
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
class RpsServiceEnviarLoteRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceEnviarLoteRpsEnvioInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteRpsEnvio: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceEnviarLoteRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceEnviarLoteRpsEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarLoteRpsEnvioResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceEnviarLoteRpsEnvioOutput.Body.Fault"] = (
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
class RpsServiceListarServicos116MunicipalInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceListarServicos116MunicipalInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ListarServicos116Municipal: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceListarServicos116MunicipalOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceListarServicos116MunicipalOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ListarServicos116MunicipalResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional[
            "RpsServiceListarServicos116MunicipalOutput.Body.Fault"
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
class RpsServiceListarServicosMunicipaisPrestadorInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceListarServicosMunicipaisPrestadorInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ListarServicosMunicipaisPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceListarServicosMunicipaisPrestadorOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "RpsServiceListarServicosMunicipaisPrestadorOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ListarServicosMunicipaisPrestadorResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional[
            "RpsServiceListarServicosMunicipaisPrestadorOutput.Body.Fault"
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
class RpsServiceListarServicosMunicipaisInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceListarServicosMunicipaisInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ListarServicosMunicipais: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceListarServicosMunicipaisOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceListarServicosMunicipaisOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ListarServicosMunicipaisResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional[
            "RpsServiceListarServicosMunicipaisOutput.Body.Fault"
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
class RpsServiceValidarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceValidarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ValidarLoteRps: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceValidarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceValidarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ValidarLoteRpsResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceValidarLoteRpsOutput.Body.Fault"] = field(
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
class RpsServiceAutenticarContribuinteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceAutenticarContribuinteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        autenticarContribuinte: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceAutenticarContribuinteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceAutenticarContribuinteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        autenticarContribuinteResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional[
            "RpsServiceAutenticarContribuinteOutput.Body.Fault"
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
class RpsServiceFecharConexaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceFecharConexaoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        fecharConexao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceFecharConexaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceFecharConexaoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        fecharConexaoResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceFecharConexaoOutput.Body.Fault"] = field(
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
class RpsServiceFinalizarSessaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceFinalizarSessaoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        finalizarSessao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceFinalizarSessaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceFinalizarSessaoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        finalizarSessaoResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceFinalizarSessaoOutput.Body.Fault"] = field(
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
class RpsServiceRequisitarAidfInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceRequisitarAidfInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        requisitarAidf: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceRequisitarAidfOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceRequisitarAidfOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        requisitarAidfResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceRequisitarAidfOutput.Body.Fault"] = field(
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
class RpsServiceValidarAidfInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceValidarAidfInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        validarAidf: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceValidarAidfOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceValidarAidfOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        validarAidfResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceValidarAidfOutput.Body.Fault"] = field(
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
class RpsServiceVerificarContribuinteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceVerificarContribuinteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        verificarContribuinte: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceVerificarContribuinteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceVerificarContribuinteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        verificarContribuinteResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceVerificarContribuinteOutput.Body.Fault"] = (
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
class RpsServiceVerificarEmpresaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceVerificarEmpresaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        verificarEmpresa: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )


@dataclass
class RpsServiceVerificarEmpresaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["RpsServiceVerificarEmpresaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        verificarEmpresaResponse: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://des36.el.com.br:8080/el-issonline/",
            },
        )
        Fault: Optional["RpsServiceVerificarEmpresaOutput.Body.Fault"] = field(
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


class RpsServiceCancelarNfseEnvio:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceCancelarNfseEnvioInput
    output = RpsServiceCancelarNfseEnvioOutput


class RpsServiceCancelarNfseMotivoEnvio:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceCancelarNfseMotivoEnvioInput
    output = RpsServiceCancelarNfseMotivoEnvioOutput


class RpsServiceConsultarCnae:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceConsultarCnaeInput
    output = RpsServiceConsultarCnaeOutput


class RpsServiceConsultarLoteRpsEnvio:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceConsultarLoteRpsEnvioInput
    output = RpsServiceConsultarLoteRpsEnvioOutput


class RpsServiceConsultarNfseEnvio:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceConsultarNfseEnvioInput
    output = RpsServiceConsultarNfseEnvioOutput


class RpsServiceConsultarNfseRpsEnvio:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceConsultarNfseRpsEnvioInput
    output = RpsServiceConsultarNfseRpsEnvioOutput


class RpsServiceConsultarSituacaoLoteRpsEnvio:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceConsultarSituacaoLoteRpsEnvioInput
    output = RpsServiceConsultarSituacaoLoteRpsEnvioOutput


class RpsServiceConsultarUltimaRps:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceConsultarUltimaRpsInput
    output = RpsServiceConsultarUltimaRpsOutput


class RpsServiceConsultarUltimoLote:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceConsultarUltimoLoteInput
    output = RpsServiceConsultarUltimoLoteOutput


class RpsServiceEnviarLoteRpsEnvio:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceEnviarLoteRpsEnvioInput
    output = RpsServiceEnviarLoteRpsEnvioOutput


class RpsServiceListarServicos116Municipal:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceListarServicos116MunicipalInput
    output = RpsServiceListarServicos116MunicipalOutput


class RpsServiceListarServicosMunicipais:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceListarServicosMunicipaisInput
    output = RpsServiceListarServicosMunicipaisOutput


class RpsServiceListarServicosMunicipaisPrestador:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceListarServicosMunicipaisPrestadorInput
    output = RpsServiceListarServicosMunicipaisPrestadorOutput


class RpsServiceValidarLoteRps:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceValidarLoteRpsInput
    output = RpsServiceValidarLoteRpsOutput


class RpsServiceAutenticarContribuinte:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceAutenticarContribuinteInput
    output = RpsServiceAutenticarContribuinteOutput


class RpsServiceFecharConexao:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceFecharConexaoInput
    output = RpsServiceFecharConexaoOutput


class RpsServiceFinalizarSessao:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceFinalizarSessaoInput
    output = RpsServiceFinalizarSessaoOutput


class RpsServiceRequisitarAidf:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceRequisitarAidfInput
    output = RpsServiceRequisitarAidfOutput


class RpsServiceValidarAidf:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceValidarAidfInput
    output = RpsServiceValidarAidfOutput


class RpsServiceVerificarContribuinte:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceVerificarContribuinteInput
    output = RpsServiceVerificarContribuinteOutput


class RpsServiceVerificarEmpresa:
    style = "document"
    location = "https://notafiscal.linhares.es.gov.br/el-nfse/RpsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RpsServiceVerificarEmpresaInput
    output = RpsServiceVerificarEmpresaOutput
