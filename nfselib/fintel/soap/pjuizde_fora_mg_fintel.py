from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.fintel.com.br/WebService"


@dataclass
class CancelarCupom:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarCupomResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    CancelarCupomResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    CancelarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConfigurarTerminal:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConfigurarTerminalResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConfigurarTerminalResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaEmissoresNfse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaEmissoresNfseResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultaEmissoresNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarCfse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarCfseResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarCfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarDadosCadastro:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarDadosCadastroResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarDadosCadastroResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarDeclaracoesSemMovimento:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarDeclaracoesSemMovimentoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarDeclaracoesSemMovimentoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteCupom:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteCupomResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarLoteCupomResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteNotasFiscais:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteNotasFiscaisResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarLoteNotasFiscaisResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseFaixa:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseFaixaResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarNfseFaixaResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarNfsePorRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoPrestado:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarNfseServicoPrestadoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoTomado:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoTomadoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarNfseServicoTomadoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNotasFiscais:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNotasFiscaisResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarNotasFiscaisResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRps:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    ConsultarSituacaoLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class DeclararServicoTomadoAutomatizado:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class DeclararServicoTomadoAutomatizadoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    DeclararServicoTomadoAutomatizadoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarImportacaoNotasFiscais:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarImportacaoNotasFiscaisResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    EnviarImportacaoNotasFiscaisResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarCartaCorrecao:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarCartaCorrecaoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    GerarCartaCorrecaoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    GerarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InformarManutencaoTerminal:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InformarManutencaoTerminalResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    InformarManutencaoTerminalResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InformeTrasmissaoSemMovimento:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InformeTrasmissaoSemMovimentoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    InformeTrasmissaoSemMovimentoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarDeclaracoesSemMovimento:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarDeclaracoesSemMovimentoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    RecepcionarDeclaracoesSemMovimentoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteCfse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteCfseResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    RecepcionarLoteCfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteCfseSincrono:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteCfseSincronoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    RecepcionarLoteCfseSincronoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    RecepcionarLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsSincrono:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsSincronoResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    RecepcionarLoteRpsSincronoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SubstituirNfse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    cabecalho: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SubstituirNfseResponse:
    class Meta:
        namespace = "http://www.fintel.com.br/WebService"

    SubstituirNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class WebX0020ServiceSoapCancelarCupomInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapCancelarCupomInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarCupom: Optional[CancelarCupom] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapCancelarCupomOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapCancelarCupomOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        CancelarCupomResponse: Optional[CancelarCupomResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapCancelarCupomOutput.Body.Fault"
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
class WebX0020ServiceSoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapCancelarNfseInput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapCancelarNfseOutput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional["WebX0020ServiceSoapCancelarNfseOutput.Body.Fault"] = (
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
class WebX0020ServiceSoapConfigurarTerminalInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConfigurarTerminalInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConfigurarTerminal: Optional[ConfigurarTerminal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConfigurarTerminalOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConfigurarTerminalOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConfigurarTerminalResponse: Optional[ConfigurarTerminalResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )
        Fault: Optional[
            "WebX0020ServiceSoapConfigurarTerminalOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultaEmissoresNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultaEmissoresNfseInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultaEmissoresNfse: Optional[ConsultaEmissoresNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultaEmissoresNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultaEmissoresNfseOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultaEmissoresNfseResponse: Optional[
            ConsultaEmissoresNfseResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultaEmissoresNfseOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarCfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarCfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarCfse: Optional[ConsultarCfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarCfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarCfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarCfseResponse: Optional[ConsultarCfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarCfseOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarDadosCadastroInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarDadosCadastroInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarDadosCadastro: Optional[ConsultarDadosCadastro] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarDadosCadastroOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarDadosCadastroOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarDadosCadastroResponse: Optional[
            ConsultarDadosCadastroResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarDadosCadastroOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarDeclaracoesSemMovimentoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarDeclaracoesSemMovimentoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarDeclaracoesSemMovimento: Optional[
            ConsultarDeclaracoesSemMovimento
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarDeclaracoesSemMovimentoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarDeclaracoesSemMovimentoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarDeclaracoesSemMovimentoResponse: Optional[
            ConsultarDeclaracoesSemMovimentoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarDeclaracoesSemMovimentoOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarLoteCupomInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarLoteCupomInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteCupom: Optional[ConsultarLoteCupom] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarLoteCupomOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarLoteCupomOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteCupomResponse: Optional[ConsultarLoteCupomResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarLoteCupomOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarLoteNotasFiscaisInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarLoteNotasFiscaisInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteNotasFiscais: Optional[ConsultarLoteNotasFiscais] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarLoteNotasFiscaisOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarLoteNotasFiscaisOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarLoteNotasFiscaisResponse: Optional[
            ConsultarLoteNotasFiscaisResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarLoteNotasFiscaisOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarLoteRpsInput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarLoteRpsOutput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarLoteRpsOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarNfseFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarNfseFaixaInput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarNfseFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarNfseFaixaOutput.Body"] = field(
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
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarNfseFaixaOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarNfsePorRpsInput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarNfsePorRpsOutput.Body"] = (
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
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarNfsePorRpsOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarNfseServicoPrestadoInput.Body"
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarNfseServicoPrestadoOutput.Body"
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarNfseServicoPrestadoOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarNfseServicoTomadoInput.Body"
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
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )


@dataclass
class WebX0020ServiceSoapConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarNfseServicoTomadoOutput.Body"
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarNfseServicoTomadoOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarNotasFiscaisInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarNotasFiscaisInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNotasFiscais: Optional[ConsultarNotasFiscais] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarNotasFiscaisOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarNotasFiscaisOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNotasFiscaisResponse: Optional[
            ConsultarNotasFiscaisResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarNotasFiscaisOutput.Body.Fault"
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
class WebX0020ServiceSoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapConsultarSituacaoLoteRpsInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRps: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapConsultarSituacaoLoteRpsOutput.Body"
    ] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class WebX0020ServiceSoapDeclararServicoTomadoAutomatizadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapDeclararServicoTomadoAutomatizadoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        DeclararServicoTomadoAutomatizado: Optional[
            DeclararServicoTomadoAutomatizado
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapDeclararServicoTomadoAutomatizadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapDeclararServicoTomadoAutomatizadoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        DeclararServicoTomadoAutomatizadoResponse: Optional[
            DeclararServicoTomadoAutomatizadoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapDeclararServicoTomadoAutomatizadoOutput.Body.Fault"
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
class WebX0020ServiceSoapEnviarImportacaoNotasFiscaisInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapEnviarImportacaoNotasFiscaisInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarImportacaoNotasFiscais: Optional[
            EnviarImportacaoNotasFiscais
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapEnviarImportacaoNotasFiscaisOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapEnviarImportacaoNotasFiscaisOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        EnviarImportacaoNotasFiscaisResponse: Optional[
            EnviarImportacaoNotasFiscaisResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapEnviarImportacaoNotasFiscaisOutput.Body.Fault"
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
class WebX0020ServiceSoapGerarCartaCorrecaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapGerarCartaCorrecaoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarCartaCorrecao: Optional[GerarCartaCorrecao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapGerarCartaCorrecaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapGerarCartaCorrecaoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        GerarCartaCorrecaoResponse: Optional[GerarCartaCorrecaoResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )
        Fault: Optional[
            "WebX0020ServiceSoapGerarCartaCorrecaoOutput.Body.Fault"
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
class WebX0020ServiceSoapGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapGerarNfseInput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapGerarNfseOutput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional["WebX0020ServiceSoapGerarNfseOutput.Body.Fault"] = (
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
class WebX0020ServiceSoapInformarManutencaoTerminalInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapInformarManutencaoTerminalInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        InformarManutencaoTerminal: Optional[InformarManutencaoTerminal] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )


@dataclass
class WebX0020ServiceSoapInformarManutencaoTerminalOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapInformarManutencaoTerminalOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        InformarManutencaoTerminalResponse: Optional[
            InformarManutencaoTerminalResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapInformarManutencaoTerminalOutput.Body.Fault"
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
class WebX0020ServiceSoapInformeTrasmissaoSemMovimentoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapInformeTrasmissaoSemMovimentoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        InformeTrasmissaoSemMovimento: Optional[
            InformeTrasmissaoSemMovimento
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapInformeTrasmissaoSemMovimentoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapInformeTrasmissaoSemMovimentoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        InformeTrasmissaoSemMovimentoResponse: Optional[
            InformeTrasmissaoSemMovimentoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapInformeTrasmissaoSemMovimentoOutput.Body.Fault"
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
class WebX0020ServiceSoapRecepcionarDeclaracoesSemMovimentoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapRecepcionarDeclaracoesSemMovimentoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarDeclaracoesSemMovimento: Optional[
            RecepcionarDeclaracoesSemMovimento
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapRecepcionarDeclaracoesSemMovimentoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapRecepcionarDeclaracoesSemMovimentoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarDeclaracoesSemMovimentoResponse: Optional[
            RecepcionarDeclaracoesSemMovimentoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapRecepcionarDeclaracoesSemMovimentoOutput.Body.Fault"
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
class WebX0020ServiceSoapRecepcionarLoteCfseSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapRecepcionarLoteCfseSincronoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteCfseSincrono: Optional[RecepcionarLoteCfseSincrono] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )


@dataclass
class WebX0020ServiceSoapRecepcionarLoteCfseSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapRecepcionarLoteCfseSincronoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteCfseSincronoResponse: Optional[
            RecepcionarLoteCfseSincronoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapRecepcionarLoteCfseSincronoOutput.Body.Fault"
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
class WebX0020ServiceSoapRecepcionarLoteCfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapRecepcionarLoteCfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        RecepcionarLoteCfse: Optional[RecepcionarLoteCfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapRecepcionarLoteCfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapRecepcionarLoteCfseOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        RecepcionarLoteCfseResponse: Optional[RecepcionarLoteCfseResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )
        Fault: Optional[
            "WebX0020ServiceSoapRecepcionarLoteCfseOutput.Body.Fault"
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
class WebX0020ServiceSoapRecepcionarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapRecepcionarLoteRpsSincronoInput.Body"
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
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )


@dataclass
class WebX0020ServiceSoapRecepcionarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "WebX0020ServiceSoapRecepcionarLoteRpsSincronoOutput.Body"
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapRecepcionarLoteRpsSincronoOutput.Body.Fault"
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
class WebX0020ServiceSoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapRecepcionarLoteRpsInput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapRecepcionarLoteRpsOutput.Body"] = field(
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
                    "namespace": "http://www.fintel.com.br/WebService",
                },
            )
        )
        Fault: Optional[
            "WebX0020ServiceSoapRecepcionarLoteRpsOutput.Body.Fault"
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
class WebX0020ServiceSoapSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapSubstituirNfseInput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )


@dataclass
class WebX0020ServiceSoapSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebX0020ServiceSoapSubstituirNfseOutput.Body"] = field(
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
                "namespace": "http://www.fintel.com.br/WebService",
            },
        )
        Fault: Optional[
            "WebX0020ServiceSoapSubstituirNfseOutput.Body.Fault"
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


class WebX0020ServiceSoapCancelarCupom:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/CancelarCupom"
    input = WebX0020ServiceSoapCancelarCupomInput
    output = WebX0020ServiceSoapCancelarCupomOutput


class WebX0020ServiceSoapCancelarNfse:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/CancelarNfse"
    input = WebX0020ServiceSoapCancelarNfseInput
    output = WebX0020ServiceSoapCancelarNfseOutput


class WebX0020ServiceSoapConfigurarTerminal:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConfigurarTerminal"
    input = WebX0020ServiceSoapConfigurarTerminalInput
    output = WebX0020ServiceSoapConfigurarTerminalOutput


class WebX0020ServiceSoapConsultaEmissoresNfse:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultaEmissoresNfse"
    input = WebX0020ServiceSoapConsultaEmissoresNfseInput
    output = WebX0020ServiceSoapConsultaEmissoresNfseOutput


class WebX0020ServiceSoapConsultarCfse:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultarCfse"
    input = WebX0020ServiceSoapConsultarCfseInput
    output = WebX0020ServiceSoapConsultarCfseOutput


class WebX0020ServiceSoapConsultarDadosCadastro:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultarDadosCadastro"
    input = WebX0020ServiceSoapConsultarDadosCadastroInput
    output = WebX0020ServiceSoapConsultarDadosCadastroOutput


class WebX0020ServiceSoapConsultarDeclaracoesSemMovimento:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/ConsultarDeclaracoesSemMovimento"
    )
    input = WebX0020ServiceSoapConsultarDeclaracoesSemMovimentoInput
    output = WebX0020ServiceSoapConsultarDeclaracoesSemMovimentoOutput


class WebX0020ServiceSoapConsultarLoteCupom:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultarLoteCupom"
    input = WebX0020ServiceSoapConsultarLoteCupomInput
    output = WebX0020ServiceSoapConsultarLoteCupomOutput


class WebX0020ServiceSoapConsultarLoteNotasFiscais:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/ConsultarLoteNotasFiscais"
    )
    input = WebX0020ServiceSoapConsultarLoteNotasFiscaisInput
    output = WebX0020ServiceSoapConsultarLoteNotasFiscaisOutput


class WebX0020ServiceSoapConsultarLoteRps:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultarLoteRps"
    input = WebX0020ServiceSoapConsultarLoteRpsInput
    output = WebX0020ServiceSoapConsultarLoteRpsOutput


class WebX0020ServiceSoapConsultarNfseFaixa:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultarNfseFaixa"
    input = WebX0020ServiceSoapConsultarNfseFaixaInput
    output = WebX0020ServiceSoapConsultarNfseFaixaOutput


class WebX0020ServiceSoapConsultarNfsePorRps:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultarNfsePorRps"
    input = WebX0020ServiceSoapConsultarNfsePorRpsInput
    output = WebX0020ServiceSoapConsultarNfsePorRpsOutput


class WebX0020ServiceSoapConsultarNfseServicoPrestado:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/ConsultarNfseServicoPrestado"
    )
    input = WebX0020ServiceSoapConsultarNfseServicoPrestadoInput
    output = WebX0020ServiceSoapConsultarNfseServicoPrestadoOutput


class WebX0020ServiceSoapConsultarNfseServicoTomado:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/ConsultarNfseServicoTomado"
    )
    input = WebX0020ServiceSoapConsultarNfseServicoTomadoInput
    output = WebX0020ServiceSoapConsultarNfseServicoTomadoOutput


class WebX0020ServiceSoapConsultarNotasFiscais:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultarNotasFiscais"
    input = WebX0020ServiceSoapConsultarNotasFiscaisInput
    output = WebX0020ServiceSoapConsultarNotasFiscaisOutput


class WebX0020ServiceSoapConsultarSituacaoLoteRps:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/ConsultarSituacaoLoteRps"
    input = WebX0020ServiceSoapConsultarSituacaoLoteRpsInput
    output = WebX0020ServiceSoapConsultarSituacaoLoteRpsOutput


class WebX0020ServiceSoapDeclararServicoTomadoAutomatizado:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/DeclararServicoTomadoAutomatizado"
    )
    input = WebX0020ServiceSoapDeclararServicoTomadoAutomatizadoInput
    output = WebX0020ServiceSoapDeclararServicoTomadoAutomatizadoOutput


class WebX0020ServiceSoapEnviarImportacaoNotasFiscais:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/EnviarImportacaoNotasFiscais"
    )
    input = WebX0020ServiceSoapEnviarImportacaoNotasFiscaisInput
    output = WebX0020ServiceSoapEnviarImportacaoNotasFiscaisOutput


class WebX0020ServiceSoapGerarCartaCorrecao:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/GerarCartaCorrecao"
    input = WebX0020ServiceSoapGerarCartaCorrecaoInput
    output = WebX0020ServiceSoapGerarCartaCorrecaoOutput


class WebX0020ServiceSoapGerarNfse:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/GerarNfse"
    input = WebX0020ServiceSoapGerarNfseInput
    output = WebX0020ServiceSoapGerarNfseOutput


class WebX0020ServiceSoapInformarManutencaoTerminal:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/InformarManutencaoTerminal"
    )
    input = WebX0020ServiceSoapInformarManutencaoTerminalInput
    output = WebX0020ServiceSoapInformarManutencaoTerminalOutput


class WebX0020ServiceSoapInformeTrasmissaoSemMovimento:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/InformeTrasmissaoSemMovimento"
    )
    input = WebX0020ServiceSoapInformeTrasmissaoSemMovimentoInput
    output = WebX0020ServiceSoapInformeTrasmissaoSemMovimentoOutput


class WebX0020ServiceSoapRecepcionarDeclaracoesSemMovimento:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/RecepcionarDeclaracoesSemMovimento"
    input = WebX0020ServiceSoapRecepcionarDeclaracoesSemMovimentoInput
    output = WebX0020ServiceSoapRecepcionarDeclaracoesSemMovimentoOutput


class WebX0020ServiceSoapRecepcionarLoteCfse:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/RecepcionarLoteCfse"
    input = WebX0020ServiceSoapRecepcionarLoteCfseInput
    output = WebX0020ServiceSoapRecepcionarLoteCfseOutput


class WebX0020ServiceSoapRecepcionarLoteCfseSincrono:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/RecepcionarLoteCfseSincrono"
    )
    input = WebX0020ServiceSoapRecepcionarLoteCfseSincronoInput
    output = WebX0020ServiceSoapRecepcionarLoteCfseSincronoOutput


class WebX0020ServiceSoapRecepcionarLoteRps:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/RecepcionarLoteRps"
    input = WebX0020ServiceSoapRecepcionarLoteRpsInput
    output = WebX0020ServiceSoapRecepcionarLoteRpsOutput


class WebX0020ServiceSoapRecepcionarLoteRpsSincrono:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://www.fintel.com.br/WebService/RecepcionarLoteRpsSincrono"
    )
    input = WebX0020ServiceSoapRecepcionarLoteRpsSincronoInput
    output = WebX0020ServiceSoapRecepcionarLoteRpsSincronoOutput


class WebX0020ServiceSoapSubstituirNfse:
    style = "document"
    location = "https://nfse.pjf.mg.gov.br:4431/WebService.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.fintel.com.br/WebService/SubstituirNfse"
    input = WebX0020ServiceSoapSubstituirNfseInput
    output = WebX0020ServiceSoapSubstituirNfseOutput
