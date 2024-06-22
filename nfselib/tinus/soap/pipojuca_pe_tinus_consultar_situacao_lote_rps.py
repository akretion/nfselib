from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarSituacaoLoteRpsResult: Optional[
        "ConsultarSituacaoLoteRpsResposta"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Test:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class TestResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    TestResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    Cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 14,
            "max_length": 14,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 15,
        },
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"

    Codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 200,
        },
    )
    Correcao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_length": 1,
            "max_length": 200,
        },
    )


@dataclass
class ArrayOfMensagemRetornotcMensagemRetorno:
    MensagemRetorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "nillable": True,
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "required": True,
            "max_length": 50,
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsSoapConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ConsultarSituacaoLoteRpsSoapConsultarSituacaoLoteRpsOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        consultarSituacaoLoteRpsResposta: Optional[
            ConsultarSituacaoLoteRpsResposta
        ] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRpsResposta",
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "ConsultarSituacaoLoteRpsSoapConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class ConsultarSituacaoLoteRpsSoapTestInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarSituacaoLoteRpsSoapTestInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        Test: Optional[Test] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


@dataclass
class ConsultarSituacaoLoteRpsSoapTestOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["ConsultarSituacaoLoteRpsSoapTestOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        TestResponse: Optional[TestResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )
        Fault: Optional[
            "ConsultarSituacaoLoteRpsSoapTestOutput.Body.Fault"
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
class ConsultarSituacaoLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"

    ConsultarSituacaoLoteRpsEnvio: Optional[ConsultarSituacaoLoteRpsEnvio] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )


class ConsultarSituacaoLoteRpsSoapTest:
    style = "document"
    location = "http://www.tinus.com.br/csp/ipojuca/WSNFSE.ConsultarSituacaoLoteRps.cls"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/WSNFSE.ConsultarSituacaoLoteRps.Test"
    input = ConsultarSituacaoLoteRpsSoapTestInput
    output = ConsultarSituacaoLoteRpsSoapTestOutput


@dataclass
class ListaMensagemRetorno(ArrayOfMensagemRetornotcMensagemRetorno):
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse.xsd"


@dataclass
class ConsultarSituacaoLoteRpsResposta1:
    class Meta:
        name = "ConsultarSituacaoLoteRpsResposta"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": 0,
        },
    )
    Situacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
            "min_inclusive": "-128",
            "max_inclusive": "127",
            "pattern": r"1|2|3|4",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/nfse.xsd",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsSoapConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "ConsultarSituacaoLoteRpsSoapConsultarSituacaoLoteRpsInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRps: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.abrasf.org.br/nfse.xsd",
            },
        )


class ConsultarSituacaoLoteRpsSoapConsultarSituacaoLoteRps:
    style = "document"
    location = "http://www.tinus.com.br/csp/ipojuca/WSNFSE.ConsultarSituacaoLoteRps.cls"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.abrasf.org.br/nfse.xsd/WSNFSE.ConsultarSituacaoLoteRps.ConsultarSituacaoLoteRps"
    input = ConsultarSituacaoLoteRpsSoapConsultarSituacaoLoteRpsInput
    output = ConsultarSituacaoLoteRpsSoapConsultarSituacaoLoteRpsOutput
