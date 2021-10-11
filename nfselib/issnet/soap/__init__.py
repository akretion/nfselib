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
        }
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    cancelar_nfse_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancelarNfseResult",
            "type": "Element",
        }
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
        }
    )


@dataclass
class ConsultaNfsePorRpsresponse:
    class Meta:
        name = "ConsultaNFSePorRPSResponse"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    consulta_nfse_por_rpsresult: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsultaNFSePorRPSResult",
            "type": "Element",
        }
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
        }
    )


@dataclass
class ConsultaSituacaoLoteRpsresponse:
    class Meta:
        name = "ConsultaSituacaoLoteRPSResponse"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    consulta_situacao_lote_rpsresult: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsultaSituacaoLoteRPSResult",
            "type": "Element",
        }
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    consultar_lote_rps_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsultarLoteRpsResult",
            "type": "Element",
        }
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
        }
    )


@dataclass
class ConsultarNfsePorRpsresponse:
    class Meta:
        name = "ConsultarNFSePorRPSResponse"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    consultar_nfse_por_rpsresult: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsultarNFSePorRPSResult",
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    consultar_nfse_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsultarNfseResult",
            "type": "Element",
        }
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
        }
    )


@dataclass
class ConsultarSituacaoLoteRpsresponse:
    class Meta:
        name = "ConsultarSituacaoLoteRPSResponse"
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    consultar_situacao_lote_rpsresult: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsultarSituacaoLoteRPSResult",
            "type": "Element",
        }
    )


@dataclass
class ConsultarUrlVisualizacaoNfse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ConsultarUrlVisualizacaoNfseResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    consultar_url_visualizacao_nfse_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsultarUrlVisualizacaoNfseResult",
            "type": "Element",
        }
    )


@dataclass
class ConsultarUrlVisualizacaoNfseSerie:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ConsultarUrlVisualizacaoNfseSerieResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    consultar_url_visualizacao_nfse_serie_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsultarUrlVisualizacaoNfseSerieResult",
            "type": "Element",
        }
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webservice/nfd"

    recepcionar_lote_rps_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecepcionarLoteRpsResult",
            "type": "Element",
        }
    )


@dataclass
class ServicosSoapCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse: Optional[CancelarNfse] = field(
            default=None,
            metadata={
                "name": "CancelarNfse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse_response: Optional[CancelarNfseResponse] = field(
            default=None,
            metadata={
                "name": "CancelarNfseResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapCancelarNfseOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapConsultaNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultaNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_nfse_por_rps: Optional[ConsultaNfsePorRps] = field(
            default=None,
            metadata={
                "name": "ConsultaNFSePorRPS",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapConsultaNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultaNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_nfse_por_rpsresponse: Optional[ConsultaNfsePorRpsresponse] = field(
            default=None,
            metadata={
                "name": "ConsultaNFSePorRPSResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapConsultaNfsePorRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapConsultaSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultaSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_situacao_lote_rps: Optional[ConsultaSituacaoLoteRps] = field(
            default=None,
            metadata={
                "name": "ConsultaSituacaoLoteRPS",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapConsultaSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultaSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_situacao_lote_rpsresponse: Optional[ConsultaSituacaoLoteRpsresponse] = field(
            default=None,
            metadata={
                "name": "ConsultaSituacaoLoteRPSResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapConsultaSituacaoLoteRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps: Optional[ConsultarLoteRps] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRps",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps_response: Optional[ConsultarLoteRpsResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRpsResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapConsultarLoteRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rps: Optional[ConsultarNfsePorRps] = field(
            default=None,
            metadata={
                "name": "ConsultarNFSePorRPS",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rpsresponse: Optional[ConsultarNfsePorRpsresponse] = field(
            default=None,
            metadata={
                "name": "ConsultarNFSePorRPSResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapConsultarNfsePorRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse: Optional[ConsultarNfse] = field(
            default=None,
            metadata={
                "name": "ConsultarNfse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_response: Optional[ConsultarNfseResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapConsultarNfseOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRPS",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rpsresponse: Optional[ConsultarSituacaoLoteRpsresponse] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRPSResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapConsultarSituacaoLoteRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapConsultarUrlVisualizacaoNfseSerieInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarUrlVisualizacaoNfseSerieInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_url_visualizacao_nfse_serie: Optional[ConsultarUrlVisualizacaoNfseSerie] = field(
            default=None,
            metadata={
                "name": "ConsultarUrlVisualizacaoNfseSerie",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapConsultarUrlVisualizacaoNfseSerieOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarUrlVisualizacaoNfseSerieOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_url_visualizacao_nfse_serie_response: Optional[ConsultarUrlVisualizacaoNfseSerieResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarUrlVisualizacaoNfseSerieResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapConsultarUrlVisualizacaoNfseSerieOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapConsultarUrlVisualizacaoNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarUrlVisualizacaoNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_url_visualizacao_nfse: Optional[ConsultarUrlVisualizacaoNfse] = field(
            default=None,
            metadata={
                "name": "ConsultarUrlVisualizacaoNfse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapConsultarUrlVisualizacaoNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapConsultarUrlVisualizacaoNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_url_visualizacao_nfse_response: Optional[ConsultarUrlVisualizacaoNfseResponse] = field(
            default=None,
            metadata={
                "name": "ConsultarUrlVisualizacaoNfseResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapConsultarUrlVisualizacaoNfseOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ServicosSoapRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps: Optional[RecepcionarLoteRps] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRps",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )


@dataclass
class ServicosSoapRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ServicosSoapRecepcionarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps_response: Optional[RecepcionarLoteRpsResponse] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsResponse",
                "type": "Element",
                "namespace": "http://www.issnetonline.com.br/webservice/nfd",
            }
        )
        fault: Optional["ServicosSoapRecepcionarLoteRpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


class ServicosSoapCancelarNfse:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/CancelarNfse"
    input = ServicosSoapCancelarNfseInput
    output = ServicosSoapCancelarNfseOutput


class ServicosSoapConsultaNfsePorRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/ConsultaNFSePorRPS"
    input = ServicosSoapConsultaNfsePorRpsInput
    output = ServicosSoapConsultaNfsePorRpsOutput


class ServicosSoapConsultaSituacaoLoteRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/ConsultaSituacaoLoteRPS"
    input = ServicosSoapConsultaSituacaoLoteRpsInput
    output = ServicosSoapConsultaSituacaoLoteRpsOutput


class ServicosSoapConsultarLoteRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/ConsultarLoteRps"
    input = ServicosSoapConsultarLoteRpsInput
    output = ServicosSoapConsultarLoteRpsOutput


class ServicosSoapConsultarNfsePorRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/ConsultarNFSePorRPS"
    input = ServicosSoapConsultarNfsePorRpsInput
    output = ServicosSoapConsultarNfsePorRpsOutput


class ServicosSoapConsultarNfse:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/ConsultarNfse"
    input = ServicosSoapConsultarNfseInput
    output = ServicosSoapConsultarNfseOutput


class ServicosSoapConsultarSituacaoLoteRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/ConsultarSituacaoLoteRPS"
    input = ServicosSoapConsultarSituacaoLoteRpsInput
    output = ServicosSoapConsultarSituacaoLoteRpsOutput


class ServicosSoapConsultarUrlVisualizacaoNfse:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/ConsultarUrlVisualizacaoNfse"
    input = ServicosSoapConsultarUrlVisualizacaoNfseInput
    output = ServicosSoapConsultarUrlVisualizacaoNfseOutput


class ServicosSoapConsultarUrlVisualizacaoNfseSerie:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/ConsultarUrlVisualizacaoNfseSerie"
    input = ServicosSoapConsultarUrlVisualizacaoNfseSerieInput
    output = ServicosSoapConsultarUrlVisualizacaoNfseSerieOutput


class ServicosSoapRecepcionarLoteRps:
    style = "document"
    location = "http://www.issnetonline.com.br/webserviceabrasf/anapolis/servicos.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.issnetonline.com.br/webservice/nfd/RecepcionarLoteRps"
    input = ServicosSoapRecepcionarLoteRpsInput
    output = ServicosSoapRecepcionarLoteRpsOutput
