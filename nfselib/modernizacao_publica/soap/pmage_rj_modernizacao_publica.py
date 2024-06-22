from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
)


@dataclass
class AppChkRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    P1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    P2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class AppChkResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    AppChkReturn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class AppChkXmlRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    P1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class AppChkXmlResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    AppChkXmlReturn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarNfseRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    CancelarNfseReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    ConsultarLoteRpsReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorFaixaRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorFaixaResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    ConsultarNfsePorFaixaReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRpsRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    ConsultarNfsePorRpsReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    ConsultarNfseServicoPrestadoReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoTomadoRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseServicoTomadoResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    ConsultarNfseServicoTomadoReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    GerarNfseReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    RecepcionarLoteRpsReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    RecepcionarLoteRpsSincronoReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SasNfeSincDadosRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Arq: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SasNfeSincDadosResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    SasNfeSincDadosReturn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SubstituirNfseRequest:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    Nfsecabecmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Nfsedadosmsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SubstituirNfseResponse:
    class Meta:
        namespace = "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"

    SubstituirNfseReturn: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class NfeservicesAppChkXmlInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesAppChkXmlInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        AppChkXml: Optional[AppChkXmlRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesAppChkXmlOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesAppChkXmlOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        AppChkXmlResponse: Optional[AppChkXmlResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional["NfeservicesAppChkXmlOutput.Body.Fault"] = field(
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
class NfeservicesAppChkInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesAppChkInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        AppChk: Optional[AppChkRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesAppChkOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesAppChkOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        AppChkResponse: Optional[AppChkResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional["NfeservicesAppChkOutput.Body.Fault"] = field(
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
class NfeservicesCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesCancelarNfseInput.Body"] = field(
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
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional["NfeservicesCancelarNfseOutput.Body.Fault"] = field(
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
class NfeservicesConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRps: Optional[ConsultarLoteRpsRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional["NfeservicesConsultarLoteRpsOutput.Body.Fault"] = (
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
class NfeservicesConsultarNfsePorFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarNfsePorFaixaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfsePorFaixa: Optional[ConsultarNfsePorFaixaRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesConsultarNfsePorFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarNfsePorFaixaOutput.Body"] = field(
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
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional[
            "NfeservicesConsultarNfsePorFaixaOutput.Body.Fault"
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
class NfeservicesConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarNfsePorRpsInput.Body"] = field(
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
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarNfsePorRpsOutput.Body"] = field(
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
                    "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
                },
            )
        )
        Fault: Optional["NfeservicesConsultarNfsePorRpsOutput.Body.Fault"] = (
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
class NfeservicesConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarNfseServicoPrestadoInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseServicoPrestado: Optional[
            ConsultarNfseServicoPrestadoRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarNfseServicoPrestadoOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNfseServicoPrestadoResponse: Optional[
            ConsultarNfseServicoPrestadoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional[
            "NfeservicesConsultarNfseServicoPrestadoOutput.Body.Fault"
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
class NfeservicesConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarNfseServicoTomadoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNfseServicoTomado: Optional[
            ConsultarNfseServicoTomadoRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesConsultarNfseServicoTomadoOutput.Body"] = field(
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
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional[
            "NfeservicesConsultarNfseServicoTomadoOutput.Body.Fault"
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
class NfeservicesGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarNfse: Optional[GerarNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesGerarNfseOutput.Body"] = field(
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
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional["NfeservicesGerarNfseOutput.Body.Fault"] = field(
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
class NfeservicesRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesRecepcionarLoteRpsSincronoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteRpsSincrono: Optional[
            RecepcionarLoteRpsSincronoRequest
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesRecepcionarLoteRpsSincronoOutput.Body"] = field(
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
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional[
            "NfeservicesRecepcionarLoteRpsSincronoOutput.Body.Fault"
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
class NfeservicesRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
                },
            )
        )
        Fault: Optional["NfeservicesRecepcionarLoteRpsOutput.Body.Fault"] = (
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
class NfeservicesSasNfeSincDadosInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesSasNfeSincDadosInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SasNfeSincDados: Optional[SasNfeSincDadosRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesSasNfeSincDadosOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesSasNfeSincDadosOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SasNfeSincDadosResponse: Optional[SasNfeSincDadosResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional["NfeservicesSasNfeSincDadosOutput.Body.Fault"] = field(
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
class NfeservicesSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesSubstituirNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        SubstituirNfse: Optional[SubstituirNfseRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://DefaultNamespace",
            },
        )


@dataclass
class NfeservicesSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeservicesSubstituirNfseOutput.Body"] = field(
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
                "namespace": "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws",
            },
        )
        Fault: Optional["NfeservicesSubstituirNfseOutput.Body.Fault"] = field(
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


class NfeservicesAppChk:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesAppChkInput
    output = NfeservicesAppChkOutput


class NfeservicesAppChkXml:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesAppChkXmlInput
    output = NfeservicesAppChkXmlOutput


class NfeservicesCancelarNfse:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesCancelarNfseInput
    output = NfeservicesCancelarNfseOutput


class NfeservicesConsultarLoteRps:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesConsultarLoteRpsInput
    output = NfeservicesConsultarLoteRpsOutput


class NfeservicesConsultarNfsePorFaixa:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesConsultarNfsePorFaixaInput
    output = NfeservicesConsultarNfsePorFaixaOutput


class NfeservicesConsultarNfsePorRps:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesConsultarNfsePorRpsInput
    output = NfeservicesConsultarNfsePorRpsOutput


class NfeservicesConsultarNfseServicoPrestado:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesConsultarNfseServicoPrestadoInput
    output = NfeservicesConsultarNfseServicoPrestadoOutput


class NfeservicesConsultarNfseServicoTomado:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesConsultarNfseServicoTomadoInput
    output = NfeservicesConsultarNfseServicoTomadoOutput


class NfeservicesGerarNfse:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesGerarNfseInput
    output = NfeservicesGerarNfseOutput


class NfeservicesRecepcionarLoteRps:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesRecepcionarLoteRpsInput
    output = NfeservicesRecepcionarLoteRpsOutput


class NfeservicesRecepcionarLoteRpsSincrono:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesRecepcionarLoteRpsSincronoInput
    output = NfeservicesRecepcionarLoteRpsSincronoOutput


class NfeservicesSasNfeSincDados:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesSasNfeSincDadosInput
    output = NfeservicesSasNfeSincDadosOutput


class NfeservicesSubstituirNfse:
    style = "rpc"
    location = (
        "http://sis-nfs-e.mage.rj.gov.br:8015/nfe/webservices/NFEServices.jws"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfeservicesSubstituirNfseInput
    output = NfeservicesSubstituirNfseOutput
