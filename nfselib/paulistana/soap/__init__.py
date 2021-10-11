from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class CancelamentoNfeRequest:
    class Meta:
        name = "CancelamentoNFeRequest"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class CancelamentoNfeResponse:
    class Meta:
        name = "CancelamentoNFeResponse"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaCnpjrequest:
    class Meta:
        name = "ConsultaCNPJRequest"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaCnpjresponse:
    class Meta:
        name = "ConsultaCNPJResponse"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaInformacoesLoteRequest:
    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaInformacoesLoteResponse:
    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaLoteRequest:
    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaLoteResponse:
    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaNfeEmitidasRequest:
    class Meta:
        name = "ConsultaNFeEmitidasRequest"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaNfeEmitidasResponse:
    class Meta:
        name = "ConsultaNFeEmitidasResponse"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaNfeRecebidasRequest:
    class Meta:
        name = "ConsultaNFeRecebidasRequest"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaNfeRecebidasResponse:
    class Meta:
        name = "ConsultaNFeRecebidasResponse"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaNfeRequest:
    class Meta:
        name = "ConsultaNFeRequest"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class ConsultaNfeResponse:
    class Meta:
        name = "ConsultaNFeResponse"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class EnvioLoteRpsrequest:
    class Meta:
        name = "EnvioLoteRPSRequest"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class EnvioLoteRpsresponse:
    class Meta:
        name = "EnvioLoteRPSResponse"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class EnvioRpsrequest:
    class Meta:
        name = "EnvioRPSRequest"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class EnvioRpsresponse:
    class Meta:
        name = "EnvioRPSResponse"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class TesteEnvioLoteRpsrequest:
    class Meta:
        name = "TesteEnvioLoteRPSRequest"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    versao_schema: Optional[int] = field(
        default=None,
        metadata={
            "name": "VersaoSchema",
            "type": "Element",
            "required": True,
        }
    )
    mensagem_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "MensagemXML",
            "type": "Element",
        }
    )


@dataclass
class TesteEnvioLoteRpsresponse:
    class Meta:
        name = "TesteEnvioLoteRPSResponse"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    retorno_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetornoXML",
            "type": "Element",
        }
    )


@dataclass
class LoteNfeSoapCancelamentoNfeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapCancelamentoNfeInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelamento_nfe_request: Optional[CancelamentoNfeRequest] = field(
            default=None,
            metadata={
                "name": "CancelamentoNFeRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapCancelamentoNfeOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapCancelamentoNfeOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelamento_nfe_response: Optional[CancelamentoNfeResponse] = field(
            default=None,
            metadata={
                "name": "CancelamentoNFeResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapCancelamentoNfeOutput.Body.Fault"] = field(
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
class LoteNfeSoapConsultaCnpjInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaCnpjInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_cnpjrequest: Optional[ConsultaCnpjrequest] = field(
            default=None,
            metadata={
                "name": "ConsultaCNPJRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapConsultaCnpjOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaCnpjOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_cnpjresponse: Optional[ConsultaCnpjresponse] = field(
            default=None,
            metadata={
                "name": "ConsultaCNPJResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapConsultaCnpjOutput.Body.Fault"] = field(
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
class LoteNfeSoapConsultaInformacoesLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaInformacoesLoteInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_informacoes_lote_request: Optional[ConsultaInformacoesLoteRequest] = field(
            default=None,
            metadata={
                "name": "ConsultaInformacoesLoteRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapConsultaInformacoesLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaInformacoesLoteOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_informacoes_lote_response: Optional[ConsultaInformacoesLoteResponse] = field(
            default=None,
            metadata={
                "name": "ConsultaInformacoesLoteResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapConsultaInformacoesLoteOutput.Body.Fault"] = field(
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
class LoteNfeSoapConsultaLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaLoteInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_lote_request: Optional[ConsultaLoteRequest] = field(
            default=None,
            metadata={
                "name": "ConsultaLoteRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapConsultaLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaLoteOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_lote_response: Optional[ConsultaLoteResponse] = field(
            default=None,
            metadata={
                "name": "ConsultaLoteResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapConsultaLoteOutput.Body.Fault"] = field(
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
class LoteNfeSoapConsultaNfeEmitidasInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaNfeEmitidasInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_nfe_emitidas_request: Optional[ConsultaNfeEmitidasRequest] = field(
            default=None,
            metadata={
                "name": "ConsultaNFeEmitidasRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapConsultaNfeEmitidasOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaNfeEmitidasOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_nfe_emitidas_response: Optional[ConsultaNfeEmitidasResponse] = field(
            default=None,
            metadata={
                "name": "ConsultaNFeEmitidasResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapConsultaNfeEmitidasOutput.Body.Fault"] = field(
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
class LoteNfeSoapConsultaNfeRecebidasInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaNfeRecebidasInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_nfe_recebidas_request: Optional[ConsultaNfeRecebidasRequest] = field(
            default=None,
            metadata={
                "name": "ConsultaNFeRecebidasRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapConsultaNfeRecebidasOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaNfeRecebidasOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_nfe_recebidas_response: Optional[ConsultaNfeRecebidasResponse] = field(
            default=None,
            metadata={
                "name": "ConsultaNFeRecebidasResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapConsultaNfeRecebidasOutput.Body.Fault"] = field(
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
class LoteNfeSoapConsultaNfeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaNfeInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_nfe_request: Optional[ConsultaNfeRequest] = field(
            default=None,
            metadata={
                "name": "ConsultaNFeRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapConsultaNfeOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapConsultaNfeOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consulta_nfe_response: Optional[ConsultaNfeResponse] = field(
            default=None,
            metadata={
                "name": "ConsultaNFeResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapConsultaNfeOutput.Body.Fault"] = field(
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
class LoteNfeSoapEnvioLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapEnvioLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        envio_lote_rpsrequest: Optional[EnvioLoteRpsrequest] = field(
            default=None,
            metadata={
                "name": "EnvioLoteRPSRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapEnvioLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapEnvioLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        envio_lote_rpsresponse: Optional[EnvioLoteRpsresponse] = field(
            default=None,
            metadata={
                "name": "EnvioLoteRPSResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapEnvioLoteRpsOutput.Body.Fault"] = field(
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
class LoteNfeSoapEnvioRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapEnvioRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        envio_rpsrequest: Optional[EnvioRpsrequest] = field(
            default=None,
            metadata={
                "name": "EnvioRPSRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapEnvioRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapEnvioRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        envio_rpsresponse: Optional[EnvioRpsresponse] = field(
            default=None,
            metadata={
                "name": "EnvioRPSResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapEnvioRpsOutput.Body.Fault"] = field(
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
class LoteNfeSoapTesteEnvioLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapTesteEnvioLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        teste_envio_lote_rpsrequest: Optional[TesteEnvioLoteRpsrequest] = field(
            default=None,
            metadata={
                "name": "TesteEnvioLoteRPSRequest",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )


@dataclass
class LoteNfeSoapTesteEnvioLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["LoteNfeSoapTesteEnvioLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        teste_envio_lote_rpsresponse: Optional[TesteEnvioLoteRpsresponse] = field(
            default=None,
            metadata={
                "name": "TesteEnvioLoteRPSResponse",
                "type": "Element",
                "namespace": "http://www.prefeitura.sp.gov.br/nfe",
            }
        )
        fault: Optional["LoteNfeSoapTesteEnvioLoteRpsOutput.Body.Fault"] = field(
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


class LoteNfeSoapCancelamentoNfe:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/cancelamentoNFe"
    input = LoteNfeSoapCancelamentoNfeInput
    output = LoteNfeSoapCancelamentoNfeOutput


class LoteNfeSoapConsultaCnpj:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/consultaCNPJ"
    input = LoteNfeSoapConsultaCnpjInput
    output = LoteNfeSoapConsultaCnpjOutput


class LoteNfeSoapConsultaInformacoesLote:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/consultaInformacoesLote"
    input = LoteNfeSoapConsultaInformacoesLoteInput
    output = LoteNfeSoapConsultaInformacoesLoteOutput


class LoteNfeSoapConsultaLote:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/consultaLote"
    input = LoteNfeSoapConsultaLoteInput
    output = LoteNfeSoapConsultaLoteOutput


class LoteNfeSoapConsultaNfe:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/consultaNFe"
    input = LoteNfeSoapConsultaNfeInput
    output = LoteNfeSoapConsultaNfeOutput


class LoteNfeSoapConsultaNfeEmitidas:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/consultaNFeEmitidas"
    input = LoteNfeSoapConsultaNfeEmitidasInput
    output = LoteNfeSoapConsultaNfeEmitidasOutput


class LoteNfeSoapConsultaNfeRecebidas:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/consultaNFeRecebidas"
    input = LoteNfeSoapConsultaNfeRecebidasInput
    output = LoteNfeSoapConsultaNfeRecebidasOutput


class LoteNfeSoapEnvioLoteRps:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/envioLoteRPS"
    input = LoteNfeSoapEnvioLoteRpsInput
    output = LoteNfeSoapEnvioLoteRpsOutput


class LoteNfeSoapEnvioRps:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/envioRPS"
    input = LoteNfeSoapEnvioRpsInput
    output = LoteNfeSoapEnvioRpsOutput


class LoteNfeSoapTesteEnvioLoteRps:
    style = "document"
    location = "https://nfe.prefeitura.sp.gov.br/ws/lotenfe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://www.prefeitura.sp.gov.br/nfe/ws/testeenvio"
    input = LoteNfeSoapTesteEnvioLoteRpsInput
    output = LoteNfeSoapTesteEnvioLoteRpsOutput
