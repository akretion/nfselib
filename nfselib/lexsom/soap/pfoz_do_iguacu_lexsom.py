from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class AtualizarDadosContribuinte:
    class Meta:
        namespace = "http://tempuri.org/"

    cpfCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    razaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    endLogradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    endNumPredial: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    endBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    endCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    endCidadeUF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    endComplemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    usuarioAlteracao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    endCidadeIBGE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    endCep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class AtualizarDadosContribuinteResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    AtualizarDadosContribuinteResult: Optional[
        "AtualizarDadosContribuinteResponse.AtualizarDadosContribuinteResult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class AtualizarDadosContribuinteResult:
        schema: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
                "required": True,
            },
        )
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )


@dataclass
class AtualizarOptSimplesNacional:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjempresa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    optanteSN: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    usuarioAlteracao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class AtualizarOptSimplesNacionalResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    AtualizarOptSimplesNacionalResult: Optional[
        "AtualizarOptSimplesNacionalResponse.AtualizarOptSimplesNacionalResult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class AtualizarOptSimplesNacionalResult:
        schema: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
                "required": True,
            },
        )
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )


@dataclass
class BaixarEmpresa:
    class Meta:
        namespace = "http://tempuri.org/"

    cnpjempresa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    usuarioAlteracao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class BaixarEmpresaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    BaixarEmpresaResult: Optional[
        "BaixarEmpresaResponse.BaixarEmpresaResult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class BaixarEmpresaResult:
        schema: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
                "required": True,
            },
        )
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )


@dataclass
class CancelamentoNfse:
    class Meta:
        name = "CancelamentoNFSE"
        namespace = "http://tempuri.org/"

    xml: Optional["CancelamentoNfse.Xml"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Xml:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class CancelamentoNfseresponse:
    class Meta:
        name = "CancelamentoNFSEResponse"
        namespace = "http://tempuri.org/"

    CancelamentoNFSEResult: Optional[
        "CancelamentoNfseresponse.CancelamentoNfseresult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class CancelamentoNfseresult:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultaNfse:
    class Meta:
        name = "ConsultaNFSE"
        namespace = "http://tempuri.org/"

    xml: Optional["ConsultaNfse.Xml"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Xml:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultaNfseresponse:
    class Meta:
        name = "ConsultaNFSEResponse"
        namespace = "http://tempuri.org/"

    ConsultaNFSEResult: Optional["ConsultaNfseresponse.ConsultaNfseresult"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class ConsultaNfseresult:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultarLoteRps:
    class Meta:
        name = "ConsultarLoteRPS"
        namespace = "http://tempuri.org/"

    xml: Optional["ConsultarLoteRps.Xml"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Xml:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultarLoteRpsresponse:
    class Meta:
        name = "ConsultarLoteRPSResponse"
        namespace = "http://tempuri.org/"

    ConsultarLoteRPSResult: Optional[
        "ConsultarLoteRpsresponse.ConsultarLoteRpsresult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class ConsultarLoteRpsresult:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultarNfseporRps:
    class Meta:
        name = "ConsultarNFSEPorRPS"
        namespace = "http://tempuri.org/"

    xml: Optional["ConsultarNfseporRps.Xml"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Xml:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultarNfseporRpsresponse:
    class Meta:
        name = "ConsultarNFSEPorRPSResponse"
        namespace = "http://tempuri.org/"

    ConsultarNFSEPorRPSResult: Optional[
        "ConsultarNfseporRpsresponse.ConsultarNfseporRpsresult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class ConsultarNfseporRpsresult:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultarNotasRecebidas:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional["ConsultarNotasRecebidas.XmlEnvio"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class XmlEnvio:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultarNotasRecebidasResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNotasRecebidasResult: Optional[
        "ConsultarNotasRecebidasResponse.ConsultarNotasRecebidasResult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class ConsultarNotasRecebidasResult:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultarSituacaoLoteRps:
    class Meta:
        name = "ConsultarSituacaoLoteRPS"
        namespace = "http://tempuri.org/"

    xml: Optional["ConsultarSituacaoLoteRps.Xml"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Xml:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ConsultarSituacaoLoteRpsresponse:
    class Meta:
        name = "ConsultarSituacaoLoteRPSResponse"
        namespace = "http://tempuri.org/"

    ConsultarSituacaoLoteRPSResult: Optional[
        "ConsultarSituacaoLoteRpsresponse.ConsultarSituacaoLoteRpsresult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class ConsultarSituacaoLoteRpsresult:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class HelloWorld:
    class Meta:
        namespace = "http://tempuri.org/"


@dataclass
class HelloWorldResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    HelloWorldResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class PegaDividaNota:
    class Meta:
        namespace = "http://tempuri.org/"

    cpfcnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    anoCompetencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    mesCompetencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    nfseNumero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    dtNota: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PegaDividaNotaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    PegaDividaNotaResult: Optional[
        "PegaDividaNotaResponse.PegaDividaNotaResult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class PegaDividaNotaResult:
        schema: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
                "required": True,
            },
        )
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )


@dataclass
class PegaNotaPelaDivida:
    class Meta:
        namespace = "http://tempuri.org/"

    dividas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    empresaId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class PegaNotaPelaDividaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    PegaNotaPelaDividaResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecebeLoteRps:
    class Meta:
        name = "RecebeLoteRPS"
        namespace = "http://tempuri.org/"

    xml: Optional["RecebeLoteRps.Xml"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Xml:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class RecebeLoteRpsresponse:
    class Meta:
        name = "RecebeLoteRPSResponse"
        namespace = "http://tempuri.org/"

    RecebeLoteRPSResult: Optional[
        "RecebeLoteRpsresponse.RecebeLoteRpsresult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class RecebeLoteRpsresult:
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class ValidarLoteRps:
    class Meta:
        name = "ValidarLoteRPS"
        namespace = "http://tempuri.org/"

    outterXml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ValidarLoteRpsresponse:
    class Meta:
        name = "ValidarLoteRPSResponse"
        namespace = "http://tempuri.org/"

    ValidarLoteRPSResult: Optional[
        "ValidarLoteRpsresponse.ValidarLoteRpsresult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class ValidarLoteRpsresult:
        schema: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.w3.org/2001/XMLSchema",
                "required": True,
            },
        )
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )


@dataclass
class GetLoteById:
    class Meta:
        name = "getLoteByID"
        namespace = "http://tempuri.org/"

    idlote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GetLoteByIdresponse:
    class Meta:
        name = "getLoteByIDResponse"
        namespace = "http://tempuri.org/"


@dataclass
class NfsewssoapAtualizarDadosContribuinteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapAtualizarDadosContribuinteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        AtualizarDadosContribuinte: Optional[AtualizarDadosContribuinte] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )


@dataclass
class NfsewssoapAtualizarDadosContribuinteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapAtualizarDadosContribuinteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        AtualizarDadosContribuinteResponse: Optional[
            AtualizarDadosContribuinteResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "NfsewssoapAtualizarDadosContribuinteOutput.Body.Fault"
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
class NfsewssoapAtualizarOptSimplesNacionalInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapAtualizarOptSimplesNacionalInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        AtualizarOptSimplesNacional: Optional[AtualizarOptSimplesNacional] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )


@dataclass
class NfsewssoapAtualizarOptSimplesNacionalOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapAtualizarOptSimplesNacionalOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        AtualizarOptSimplesNacionalResponse: Optional[
            AtualizarOptSimplesNacionalResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "NfsewssoapAtualizarOptSimplesNacionalOutput.Body.Fault"
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
class NfsewssoapBaixarEmpresaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapBaixarEmpresaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        BaixarEmpresa: Optional[BaixarEmpresa] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapBaixarEmpresaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapBaixarEmpresaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        BaixarEmpresaResponse: Optional[BaixarEmpresaResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapBaixarEmpresaOutput.Body.Fault"] = field(
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
class NfsewssoapCancelamentoNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapCancelamentoNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelamentoNFSE: Optional[CancelamentoNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapCancelamentoNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapCancelamentoNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelamentoNFSEResponse: Optional[CancelamentoNfseresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapCancelamentoNfseOutput.Body.Fault"] = field(
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
class NfsewssoapConsultaNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultaNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultaNFSE: Optional[ConsultaNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapConsultaNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultaNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultaNFSEResponse: Optional[ConsultaNfseresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapConsultaNfseOutput.Body.Fault"] = field(
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
class NfsewssoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRPS: Optional[ConsultarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteRPSResponse: Optional[ConsultarLoteRpsresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapConsultarLoteRpsOutput.Body.Fault"] = field(
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
class NfsewssoapConsultarNfseporRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultarNfseporRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNFSEPorRPS: Optional[ConsultarNfseporRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapConsultarNfseporRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultarNfseporRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNFSEPorRPSResponse: Optional[ConsultarNfseporRpsresponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )
        Fault: Optional["NfsewssoapConsultarNfseporRpsOutput.Body.Fault"] = (
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
class NfsewssoapConsultarNotasRecebidasInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultarNotasRecebidasInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNotasRecebidas: Optional[ConsultarNotasRecebidas] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapConsultarNotasRecebidasOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultarNotasRecebidasOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNotasRecebidasResponse: Optional[
            ConsultarNotasRecebidasResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "NfsewssoapConsultarNotasRecebidasOutput.Body.Fault"
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
class NfsewssoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultarSituacaoLoteRpsInput.Body"] = field(
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
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapConsultarSituacaoLoteRpsOutput.Body"] = field(
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
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "NfsewssoapConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class NfsewssoapHelloWorldInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapHelloWorldInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        HelloWorld: Optional[HelloWorld] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapHelloWorldOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapHelloWorldOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        HelloWorldResponse: Optional[HelloWorldResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapHelloWorldOutput.Body.Fault"] = field(
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
class NfsewssoapPegaDividaNotaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapPegaDividaNotaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        PegaDividaNota: Optional[PegaDividaNota] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapPegaDividaNotaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapPegaDividaNotaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        PegaDividaNotaResponse: Optional[PegaDividaNotaResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapPegaDividaNotaOutput.Body.Fault"] = field(
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
class NfsewssoapPegaNotaPelaDividaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapPegaNotaPelaDividaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        PegaNotaPelaDivida: Optional[PegaNotaPelaDivida] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapPegaNotaPelaDividaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapPegaNotaPelaDividaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        PegaNotaPelaDividaResponse: Optional[PegaNotaPelaDividaResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )
        Fault: Optional["NfsewssoapPegaNotaPelaDividaOutput.Body.Fault"] = (
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
class NfsewssoapRecebeLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapRecebeLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecebeLoteRPS: Optional[RecebeLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapRecebeLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapRecebeLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecebeLoteRPSResponse: Optional[RecebeLoteRpsresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapRecebeLoteRpsOutput.Body.Fault"] = field(
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
class NfsewssoapValidarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapValidarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ValidarLoteRPS: Optional[ValidarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapValidarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapValidarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ValidarLoteRPSResponse: Optional[ValidarLoteRpsresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapValidarLoteRpsOutput.Body.Fault"] = field(
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
class NfsewssoapGetLoteByIdInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapGetLoteByIdInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        getLoteByID: Optional[GetLoteById] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class NfsewssoapGetLoteByIdOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfsewssoapGetLoteByIdOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        getLoteByIDResponse: Optional[GetLoteByIdresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["NfsewssoapGetLoteByIdOutput.Body.Fault"] = field(
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


class NfsewssoapAtualizarDadosContribuinte:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/AtualizarDadosContribuinte"
    input = NfsewssoapAtualizarDadosContribuinteInput
    output = NfsewssoapAtualizarDadosContribuinteOutput


class NfsewssoapAtualizarOptSimplesNacional:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/AtualizarOptSimplesNacional"
    input = NfsewssoapAtualizarOptSimplesNacionalInput
    output = NfsewssoapAtualizarOptSimplesNacionalOutput


class NfsewssoapBaixarEmpresa:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/BaixarEmpresa"
    input = NfsewssoapBaixarEmpresaInput
    output = NfsewssoapBaixarEmpresaOutput


class NfsewssoapCancelamentoNfse:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/CancelamentoNFSE"
    input = NfsewssoapCancelamentoNfseInput
    output = NfsewssoapCancelamentoNfseOutput


class NfsewssoapConsultaNfse:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ConsultaNFSE"
    input = NfsewssoapConsultaNfseInput
    output = NfsewssoapConsultaNfseOutput


class NfsewssoapConsultarLoteRps:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ConsultarLoteRPS"
    input = NfsewssoapConsultarLoteRpsInput
    output = NfsewssoapConsultarLoteRpsOutput


class NfsewssoapConsultarNfseporRps:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ConsultarNFSEPorRPS"
    input = NfsewssoapConsultarNfseporRpsInput
    output = NfsewssoapConsultarNfseporRpsOutput


class NfsewssoapConsultarNotasRecebidas:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ConsultarNotasRecebidas"
    input = NfsewssoapConsultarNotasRecebidasInput
    output = NfsewssoapConsultarNotasRecebidasOutput


class NfsewssoapConsultarSituacaoLoteRps:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ConsultarSituacaoLoteRPS"
    input = NfsewssoapConsultarSituacaoLoteRpsInput
    output = NfsewssoapConsultarSituacaoLoteRpsOutput


class NfsewssoapHelloWorld:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/HelloWorld"
    input = NfsewssoapHelloWorldInput
    output = NfsewssoapHelloWorldOutput


class NfsewssoapPegaDividaNota:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/PegaDividaNota"
    input = NfsewssoapPegaDividaNotaInput
    output = NfsewssoapPegaDividaNotaOutput


class NfsewssoapPegaNotaPelaDivida:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/PegaNotaPelaDivida"
    input = NfsewssoapPegaNotaPelaDividaInput
    output = NfsewssoapPegaNotaPelaDividaOutput


class NfsewssoapRecebeLoteRps:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/RecebeLoteRPS"
    input = NfsewssoapRecebeLoteRpsInput
    output = NfsewssoapRecebeLoteRpsOutput


class NfsewssoapValidarLoteRps:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/ValidarLoteRPS"
    input = NfsewssoapValidarLoteRpsInput
    output = NfsewssoapValidarLoteRpsOutput


class NfsewssoapGetLoteById:
    style = "document"
    location = "http://nfse.pmfi.pr.gov.br/nfsews/nfse.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/getLoteByID"
    input = NfsewssoapGetLoteByIdInput
    output = NfsewssoapGetLoteByIdOutput
