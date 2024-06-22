from dataclasses import dataclass, field
from typing import Optional

from nfselib.bsitbr.soap.nfse_ws_wsdl_nfse_ws import (
    CancelarNfse,
    CancelarNfseResponse,
    CancelarRps,
    CancelarRpsResponse,
    ConsultarLoteRps,
    ConsultarLoteRpsResponse,
    ConsultarNfseRps,
    ConsultarNfseRpsResponse,
    ConsultarPdfNfseRps,
    ConsultarPdfNfseRpsResponse,
    ConsultarPdfRest,
    ConsultarPdfRestResponse,
    CredenciarUsuarioDeiss,
    CredenciarUsuarioDeissresponse,
    CredenciarUsuarioNfse,
    CredenciarUsuarioNfseResponse,
    EnviarLoteRpsSincrono,
    EnviarLoteRpsSincronoResponse,
    GerarNfse,
    GerarNfseResponse,
    OpcoesDeEmissaoNfsecontribuinte,
    OpcoesDeEmissaoNfsecontribuinteResponse,
    OpcoesDeEmissaoNfseempresa,
    OpcoesDeEmissaoNfseempresaResponse,
    VerificarStatusIntegracao,
    VerificarStatusIntegracaoResponse,
)

__NAMESPACE__ = "http://impl.ws.integration.pm.bsit.com.br/"


@dataclass
class NfseWsCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancelarNfse: Optional[CancelarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancelarNfseResponse: Optional[CancelarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsCancelarNfseOutput.Body.Fault"] = field(
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
class NfseWsCancelarRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsCancelarRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancelarRps: Optional[CancelarRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsCancelarRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsCancelarRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancelarRpsResponse: Optional[CancelarRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsCancelarRpsOutput.Body.Fault"] = field(
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
class NfseWsConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarLoteRps: Optional[ConsultarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarLoteRpsResponse: Optional[ConsultarLoteRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NfseWsConsultarNfseRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsConsultarNfseRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarNfseRps: Optional[ConsultarNfseRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsConsultarNfseRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsConsultarNfseRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarNfseRpsResponse: Optional[ConsultarNfseRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsConsultarNfseRpsOutput.Body.Fault"] = field(
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
class NfseWsConsultarPdfNfseRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsConsultarPdfNfseRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarPdfNfseRps: Optional[ConsultarPdfNfseRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsConsultarPdfNfseRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsConsultarPdfNfseRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarPdfNfseRpsResponse: Optional[ConsultarPdfNfseRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.integration.pm.bsit.com.br/",
                },
            )
        )
        Fault: Optional["NfseWsConsultarPdfNfseRpsOutput.Body.Fault"] = field(
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
class NfseWsConsultarPdfRestInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsConsultarPdfRestInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarPdfRest: Optional[ConsultarPdfRest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsConsultarPdfRestOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsConsultarPdfRestOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarPdfRestResponse: Optional[ConsultarPdfRestResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsConsultarPdfRestOutput.Body.Fault"] = field(
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
class NfseWsCredenciarUsuarioDeissInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsCredenciarUsuarioDeissInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        credenciarUsuarioDEISS: Optional[CredenciarUsuarioDeiss] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsCredenciarUsuarioDeissOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsCredenciarUsuarioDeissOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        credenciarUsuarioDEISSResponse: Optional[
            CredenciarUsuarioDeissresponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsCredenciarUsuarioDeissOutput.Body.Fault"] = (
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
class NfseWsCredenciarUsuarioNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsCredenciarUsuarioNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        credenciarUsuarioNfse: Optional[CredenciarUsuarioNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsCredenciarUsuarioNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsCredenciarUsuarioNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        credenciarUsuarioNfseResponse: Optional[
            CredenciarUsuarioNfseResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsCredenciarUsuarioNfseOutput.Body.Fault"] = (
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
class NfseWsEnviarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsEnviarLoteRpsSincronoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        enviarLoteRpsSincrono: Optional[EnviarLoteRpsSincrono] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsEnviarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsEnviarLoteRpsSincronoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        enviarLoteRpsSincronoResponse: Optional[
            EnviarLoteRpsSincronoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsEnviarLoteRpsSincronoOutput.Body.Fault"] = (
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
class NfseWsGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gerarNfse: Optional[GerarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsGerarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gerarNfseResponse: Optional[GerarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsGerarNfseOutput.Body.Fault"] = field(
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
class NfseWsOpcoesDeEmissaoNfsecontribuinteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsOpcoesDeEmissaoNfsecontribuinteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        opcoesDeEmissaoNFSEContribuinte: Optional[
            OpcoesDeEmissaoNfsecontribuinte
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsOpcoesDeEmissaoNfsecontribuinteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsOpcoesDeEmissaoNfsecontribuinteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        opcoesDeEmissaoNFSEContribuinteResponse: Optional[
            OpcoesDeEmissaoNfsecontribuinteResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional[
            "NfseWsOpcoesDeEmissaoNfsecontribuinteOutput.Body.Fault"
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
class NfseWsOpcoesDeEmissaoNfseempresaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsOpcoesDeEmissaoNfseempresaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        opcoesDeEmissaoNFSEEmpresa: Optional[OpcoesDeEmissaoNfseempresa] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://ws.integration.pm.bsit.com.br/",
                },
            )
        )


@dataclass
class NfseWsOpcoesDeEmissaoNfseempresaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsOpcoesDeEmissaoNfseempresaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        opcoesDeEmissaoNFSEEmpresaResponse: Optional[
            OpcoesDeEmissaoNfseempresaResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional[
            "NfseWsOpcoesDeEmissaoNfseempresaOutput.Body.Fault"
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
class NfseWsVerificarStatusIntegracaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsVerificarStatusIntegracaoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        verificarStatusIntegracao: Optional[VerificarStatusIntegracao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )


@dataclass
class NfseWsVerificarStatusIntegracaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfseWsVerificarStatusIntegracaoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        verificarStatusIntegracaoResponse: Optional[
            VerificarStatusIntegracaoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://ws.integration.pm.bsit.com.br/",
            },
        )
        Fault: Optional["NfseWsVerificarStatusIntegracaoOutput.Body.Fault"] = (
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


class NfseWsCancelarNfse:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsCancelarNfseInput
    output = NfseWsCancelarNfseOutput


class NfseWsCancelarRps:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsCancelarRpsInput
    output = NfseWsCancelarRpsOutput


class NfseWsConsultarLoteRps:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsConsultarLoteRpsInput
    output = NfseWsConsultarLoteRpsOutput


class NfseWsConsultarNfseRps:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsConsultarNfseRpsInput
    output = NfseWsConsultarNfseRpsOutput


class NfseWsConsultarPdfNfseRps:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsConsultarPdfNfseRpsInput
    output = NfseWsConsultarPdfNfseRpsOutput


class NfseWsConsultarPdfRest:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsConsultarPdfRestInput
    output = NfseWsConsultarPdfRestOutput


class NfseWsCredenciarUsuarioDeiss:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsCredenciarUsuarioDeissInput
    output = NfseWsCredenciarUsuarioDeissOutput


class NfseWsCredenciarUsuarioNfse:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsCredenciarUsuarioNfseInput
    output = NfseWsCredenciarUsuarioNfseOutput


class NfseWsEnviarLoteRpsSincrono:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsEnviarLoteRpsSincronoInput
    output = NfseWsEnviarLoteRpsSincronoOutput


class NfseWsGerarNfse:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsGerarNfseInput
    output = NfseWsGerarNfseOutput


class NfseWsOpcoesDeEmissaoNfsecontribuinte:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsOpcoesDeEmissaoNfsecontribuinteInput
    output = NfseWsOpcoesDeEmissaoNfsecontribuinteOutput


class NfseWsOpcoesDeEmissaoNfseempresa:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsOpcoesDeEmissaoNfseempresaInput
    output = NfseWsOpcoesDeEmissaoNfseempresaOutput


class NfseWsVerificarStatusIntegracao:
    style = "rpc"
    location = "http://gestaopublica.orizona.bsit-br.com.br/integracao/services/nfseWS"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NfseWsVerificarStatusIntegracaoInput
    output = NfseWsVerificarStatusIntegracaoOutput
