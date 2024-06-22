from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "urn:server.issqn"


@dataclass
class Contribuinte:
    endereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    cidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    pais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    nome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    nomefantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    inscricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    cpfcnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    documento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    rgie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    passaporte: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    nascionalidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    ddd: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    fone: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class NotasArray:
    arrayType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schemas.xmlsoap.org/soap/encoding/",
        },
    )


@dataclass
class Servico:
    quantidade: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    atividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    deducao: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    codigoservico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    codigotributacaomunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    aliquota: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    inss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    total: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class ServicosArray:
    arrayType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schemas.xmlsoap.org/soap/encoding/",
        },
    )


@dataclass
class GravaNotaXmlrequest:
    class Meta:
        name = "gravaNotaXMLRequest"
        namespace = "urn:server.issqn"

    params: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GravaNotaXmlresponse:
    class Meta:
        name = "gravaNotaXMLResponse"
        namespace = "urn:server.issqn"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ListarNotasXmlrequest:
    class Meta:
        name = "listarNotasXMLRequest"
        namespace = "urn:server.issqn"

    params: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ListarNotasXmlresponse:
    class Meta:
        name = "listarNotasXMLResponse"
        namespace = "urn:server.issqn"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ParamsListarNotas:
    class Meta:
        name = "paramsListarNotas"

    ano: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    mes: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    cpfcnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    inscricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    chave: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class ParamsListarTomador:
    class Meta:
        name = "paramsListarTomador"

    cpfcnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    inscricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    cpfcnpjtomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    chave: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


class TipoDeducao(Enum):
    PERCENTUAL = "Percentual"
    VALOR = "Valor"


class TipoIncidencia(Enum):
    LOCAL = "Local"
    FORA = "Fora"


class TipoOptante(Enum):
    SIM = "Sim"
    N_O = "Não"


class TipoRetido(Enum):
    SIM = "Sim"
    N_O = "Não"


@dataclass
class Nota:
    guia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    mes: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    cidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    exercicio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    modelo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    apuracao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valorimposto: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    situacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    deducao: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    basecalculo: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    servicos: Optional[ServicosArray] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    tomador: Optional[Contribuinte] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    prestador: Optional[Contribuinte] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    codigo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    fatura: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valorissretidonafonte: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    retido: Optional[TipoRetido] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    incidencia: Optional[TipoIncidencia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    codigoverificacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valorpis: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valorirrf: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valorcsll: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valorcofins: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    valorinss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class WebservicePrefeituraPortTypeGravaNotaXmlInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebservicePrefeituraPortTypeGravaNotaXmlInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        gravaNotaXML: Optional[GravaNotaXmlrequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:server.issqn",
            },
        )


@dataclass
class WebservicePrefeituraPortTypeGravaNotaXmlOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebservicePrefeituraPortTypeGravaNotaXmlOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        gravaNotaXMLResponse: Optional[GravaNotaXmlresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:server.issqn",
            },
        )
        Fault: Optional[
            "WebservicePrefeituraPortTypeGravaNotaXmlOutput.Body.Fault"
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
class WebservicePrefeituraPortTypeListarNotasXmlInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebservicePrefeituraPortTypeListarNotasXmlInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        listarNotasXML: Optional[ListarNotasXmlrequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:server.issqn",
            },
        )


@dataclass
class WebservicePrefeituraPortTypeListarNotasXmlOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebservicePrefeituraPortTypeListarNotasXmlOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        listarNotasXMLResponse: Optional[ListarNotasXmlresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:server.issqn",
            },
        )
        Fault: Optional[
            "WebservicePrefeituraPortTypeListarNotasXmlOutput.Body.Fault"
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
class ListarNotasRequest:
    class Meta:
        name = "listarNotasRequest"
        namespace = "urn:server.issqn"

    params: Optional[ParamsListarNotas] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ListarNotasResponse:
    class Meta:
        name = "listarNotasResponse"
        namespace = "urn:server.issqn"

    return_value: Optional[NotasArray] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ParamsGravaNota:
    class Meta:
        name = "paramsGravaNota"

    cpfcnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    inscricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    chave: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    modelo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    fatura: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    orcamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    vencimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    tipo: Optional[TipoDeducao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    pis: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    csll: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    cofins: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    irff: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    situacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    optante: Optional[TipoOptante] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    aliquota: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    texto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    servicos: Optional[ServicosArray] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    tomador: Optional[Contribuinte] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    retido: Optional[TipoRetido] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    incidencia: Optional[TipoIncidencia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


class WebservicePrefeituraPortTypeGravaNotaXml:
    style = "rpc"
    location = "https://web.votuporanga.sp.gov.br:443/amfphp/services/RLZ/webservice/server.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:server.issqn#gravaNotaXML"
    input = WebservicePrefeituraPortTypeGravaNotaXmlInput
    output = WebservicePrefeituraPortTypeGravaNotaXmlOutput


class WebservicePrefeituraPortTypeListarNotasXml:
    style = "rpc"
    location = "https://web.votuporanga.sp.gov.br:443/amfphp/services/RLZ/webservice/server.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:server.issqn#listarNotasXML"
    input = WebservicePrefeituraPortTypeListarNotasXmlInput
    output = WebservicePrefeituraPortTypeListarNotasXmlOutput


@dataclass
class WebservicePrefeituraPortTypeListarNotasInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebservicePrefeituraPortTypeListarNotasInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        listarNotas: Optional[ListarNotasRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:server.issqn",
            },
        )


@dataclass
class WebservicePrefeituraPortTypeListarNotasOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebservicePrefeituraPortTypeListarNotasOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        listarNotasResponse: Optional[ListarNotasResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:server.issqn",
            },
        )
        Fault: Optional[
            "WebservicePrefeituraPortTypeListarNotasOutput.Body.Fault"
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
class GravaNotaRequest:
    class Meta:
        name = "gravaNotaRequest"
        namespace = "urn:server.issqn"

    params: Optional[ParamsGravaNota] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class GravaNotaResponse:
    class Meta:
        name = "gravaNotaResponse"
        namespace = "urn:server.issqn"

    return_value: Optional[Nota] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class WebservicePrefeituraPortTypeGravaNotaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebservicePrefeituraPortTypeGravaNotaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gravaNota: Optional[GravaNotaRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:server.issqn",
            },
        )


@dataclass
class WebservicePrefeituraPortTypeGravaNotaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WebservicePrefeituraPortTypeGravaNotaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        gravaNotaResponse: Optional[GravaNotaResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:server.issqn",
            },
        )
        Fault: Optional[
            "WebservicePrefeituraPortTypeGravaNotaOutput.Body.Fault"
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


class WebservicePrefeituraPortTypeListarNotas:
    style = "rpc"
    location = "https://web.votuporanga.sp.gov.br:443/amfphp/services/RLZ/webservice/server.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:server.issqn#listarNotas"
    input = WebservicePrefeituraPortTypeListarNotasInput
    output = WebservicePrefeituraPortTypeListarNotasOutput


class WebservicePrefeituraPortTypeGravaNota:
    style = "rpc"
    location = "https://web.votuporanga.sp.gov.br:443/amfphp/services/RLZ/webservice/server.php"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "urn:server.issqn#gravaNota"
    input = WebservicePrefeituraPortTypeGravaNotaInput
    output = WebservicePrefeituraPortTypeGravaNotaOutput
