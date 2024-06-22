from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDateTime


@dataclass
class Qname:
    class Meta:
        name = "QName"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class AnyType:
    class Meta:
        name = "anyType"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AnyUri:
    class Meta:
        name = "anyURI"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[str] = field(
        default="",
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Base64Binary:
    class Meta:
        name = "base64Binary"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "nillable": True,
            "format": "base64",
        },
    )


@dataclass
class Boolean:
    class Meta:
        name = "boolean"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Byte:
    class Meta:
        name = "byte"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Char:
    class Meta:
        name = "char"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class DateTime:
    class Meta:
        name = "dateTime"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class DecimalType:
    class Meta:
        name = "decimal"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Double:
    class Meta:
        name = "double"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[float] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Duration:
    class Meta:
        name = "duration"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[str] = field(
        default="",
        metadata={
            "min_inclusive": "-P10675199DT2H48M5.4775808S",
            "max_inclusive": "P10675199DT2H48M5.4775807S",
            "pattern": r"\-?P(\d*D)?(T(\d*H)?(\d*M)?(\d*(\.\d*)?S)?)?",
            "nillable": True,
        },
    )


@dataclass
class Float:
    class Meta:
        name = "float"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[float] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Guid:
    class Meta:
        name = "guid"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[str] = field(
        default="",
        metadata={
            "pattern": r"[\da-fA-F]{8}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{12}",
            "nillable": True,
        },
    )


@dataclass
class Int:
    class Meta:
        name = "int"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Long:
    class Meta:
        name = "long"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Short:
    class Meta:
        name = "short"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class String:
    class Meta:
        name = "string"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[str] = field(
        default="",
        metadata={
            "nillable": True,
        },
    )


@dataclass
class UnsignedByte:
    class Meta:
        name = "unsignedByte"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class UnsignedInt:
    class Meta:
        name = "unsignedInt"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class UnsignedLong:
    class Meta:
        name = "unsignedLong"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class UnsignedShort:
    class Meta:
        name = "unsignedShort"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Cabecalho1:
    class Meta:
        name = "Cabecalho"
        namespace = "http://tempuri.org/"

    versaoDados: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CancelarCartaCorrecao:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarCartaCorrecaoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    CancelarCartaCorrecaoResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfse:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CancelarNfseResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    CancelarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarCartaCorrecao:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarCartaCorrecaoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarCartaCorrecaoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteDeclaracaoNota:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteDeclaracaoNotaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarLoteDeclaracaoNotaResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseDeiss:
    class Meta:
        name = "ConsultarNFSeDEISS"
        namespace = "http://tempuri.org/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNfseDeissresponse:
    class Meta:
        name = "ConsultarNFSeDEISSResponse"
        namespace = "http://tempuri.org/"

    ConsultarNFSeDEISSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNfse:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorFaixa:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorFaixaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNfsePorRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoPrestado:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoPrestadoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNfseServicoPrestadoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoTomado:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNfseServicoTomadoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNfseServicoTomadoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarNotasFaltantesNfseDeiss:
    class Meta:
        name = "ConsultarNotasFaltantesNFSeDEISS"
        namespace = "http://tempuri.org/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNotasFaltantesNfseDeissresponse:
    class Meta:
        name = "ConsultarNotasFaltantesNFSeDEISSResponse"
        namespace = "http://tempuri.org/"

    ConsultarNotasFaltantesNFSeDEISSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNotasPorServico:
    class Meta:
        namespace = "http://tempuri.org/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNotasPorServicoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNotasPorServicoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarSituacaoLoteRps:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarSituacaoLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarTodasNotasPorPeriodo:
    class Meta:
        namespace = "http://tempuri.org/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarTodasNotasPorPeriodoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarTodasNotasPorPeriodoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EntregarDeclaracao:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EntregarDeclaracaoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EntregarDeclaracaoResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteDeclaracao:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteDeclaracaoNotaReceive:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteDeclaracaoNotaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarLoteDeclaracaoNotaResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteDeclaracaoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarLoteDeclaracaoResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteRpsSincrono:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarLoteRpsSincronoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarLoteRpsSincronoResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarReceitaBrutaAcumulada:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarReceitaBrutaAcumuladaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarReceitaBrutaAcumuladaResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarRegimeApuracao:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EnviarRegimeApuracaoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarRegimeApuracaoResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarCartaCorrecao:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarCartaCorrecaoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    GerarCartaCorrecaoResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarManifestacao:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarManifestacaoResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    GerarManifestacaoResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfse:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class GerarNfseResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    GerarNfseResponseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ObterNotasDeiss:
    class Meta:
        name = "ObterNotasDEISS"
        namespace = "http://tempuri.org/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ObterNotasDeissresponse:
    class Meta:
        name = "ObterNotasDEISSResponse"
        namespace = "http://tempuri.org/"

    ObterNotasDEISSResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ObterNotasIntermediadas:
    class Meta:
        namespace = "http://tempuri.org/"

    xml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ObterNotasIntermediadasResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ObterNotasIntermediadasResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    RecepcionarLoteRpsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SubstituirNfse:
    class Meta:
        namespace = "http://tempuri.org/"

    xmlEnvio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class SubstituirNfseResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    SubstituirNfseResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class WebServiceReceive:
    class Meta:
        namespace = "http://tempuri.org/"

    receive: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class WebServiceResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class InfseIntegracaoDeissConsultarNfseDeissInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Body: Optional["InfseIntegracaoDeissConsultarNfseDeissInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNFSeDEISS: Optional[ConsultarNfseDeiss] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseIntegracaoDeissConsultarNfseDeissOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Body: Optional["InfseIntegracaoDeissConsultarNfseDeissOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        ConsultarNFSeDEISSResponse: Optional[ConsultarNfseDeissresponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )
        Fault: Optional[
            "InfseIntegracaoDeissConsultarNfseDeissOutput.Body.Fault"
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
class InfseIntegracaoDeissConsultarNotasFaltantesNfseDeissInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Body: Optional[
        "InfseIntegracaoDeissConsultarNotasFaltantesNfseDeissInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNotasFaltantesNFSeDEISS: Optional[
            ConsultarNotasFaltantesNfseDeiss
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseIntegracaoDeissConsultarNotasFaltantesNfseDeissOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Body: Optional[
        "InfseIntegracaoDeissConsultarNotasFaltantesNfseDeissOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarNotasFaltantesNFSeDEISSResponse: Optional[
            ConsultarNotasFaltantesNfseDeissresponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseIntegracaoDeissConsultarNotasFaltantesNfseDeissOutput.Body.Fault"
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
class InfseIntegracaoDeissConsultarTodasNotasPorPeriodoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Body: Optional[
        "InfseIntegracaoDeissConsultarTodasNotasPorPeriodoInput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarTodasNotasPorPeriodo: Optional[
            ConsultarTodasNotasPorPeriodo
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseIntegracaoDeissConsultarTodasNotasPorPeriodoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Body: Optional[
        "InfseIntegracaoDeissConsultarTodasNotasPorPeriodoOutput.Body"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ConsultarTodasNotasPorPeriodoResponse: Optional[
            ConsultarTodasNotasPorPeriodoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseIntegracaoDeissConsultarTodasNotasPorPeriodoOutput.Body.Fault"
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
class InfseIntegracaoDeissObterNotasDeissInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Body: Optional["InfseIntegracaoDeissObterNotasDeissInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ObterNotasDEISS: Optional[ObterNotasDeiss] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseIntegracaoDeissObterNotasDeissOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Body: Optional["InfseIntegracaoDeissObterNotasDeissOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ObterNotasDEISSResponse: Optional[ObterNotasDeissresponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseIntegracaoDeissObterNotasDeissOutput.Body.Fault"
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
class Cabecalho(Cabecalho1):
    class Meta:
        name = "cabecalho"
        namespace = "http://tempuri.org/"


@dataclass
class InfseconsultasConsultarCartaCorrecaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarCartaCorrecaoInput.Header"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    Body: Optional["InfseconsultasConsultarCartaCorrecaoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarCartaCorrecao: Optional[ConsultarCartaCorrecao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarCartaCorrecaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarCartaCorrecaoOutput.Header"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    Body: Optional["InfseconsultasConsultarCartaCorrecaoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarCartaCorrecaoResponse: Optional[
            ConsultarCartaCorrecaoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseconsultasConsultarCartaCorrecaoOutput.Body.Fault"
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
class InfseconsultasConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarLoteRpsInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarLoteRps: Optional[ConsultarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarLoteRpsOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarLoteRpsResponse: Optional[ConsultarLoteRpsResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfseconsultasConsultarLoteRpsOutput.Body.Fault"] = (
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
class InfseconsultasConsultarNfsePorFaixaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarNfsePorFaixaInput.Header"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    Body: Optional["InfseconsultasConsultarNfsePorFaixaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarNfsePorFaixa: Optional[ConsultarNfsePorFaixa] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarNfsePorFaixaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarNfsePorFaixaOutput.Header"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    Body: Optional["InfseconsultasConsultarNfsePorFaixaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
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
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseconsultasConsultarNfsePorFaixaOutput.Body.Fault"
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
class InfseconsultasConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarNfsePorRpsInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarNfsePorRps: Optional[ConsultarNfsePorRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarNfsePorRpsOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarNfsePorRpsResponse: Optional[ConsultarNfsePorRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )
        Fault: Optional[
            "InfseconsultasConsultarNfsePorRpsOutput.Body.Fault"
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
class InfseconsultasConsultarNfseServicoPrestadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional[
        "InfseconsultasConsultarNfseServicoPrestadoInput.Header"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarNfseServicoPrestadoInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
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
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarNfseServicoPrestadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional[
        "InfseconsultasConsultarNfseServicoPrestadoOutput.Header"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarNfseServicoPrestadoOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
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
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseconsultasConsultarNfseServicoPrestadoOutput.Body.Fault"
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
class InfseconsultasConsultarNfseServicoTomadoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional[
        "InfseconsultasConsultarNfseServicoTomadoInput.Header"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarNfseServicoTomadoInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarNfseServicoTomado: Optional[ConsultarNfseServicoTomado] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )


@dataclass
class InfseconsultasConsultarNfseServicoTomadoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional[
        "InfseconsultasConsultarNfseServicoTomadoOutput.Header"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarNfseServicoTomadoOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
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
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseconsultasConsultarNfseServicoTomadoOutput.Body.Fault"
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
class InfseconsultasConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarNfseInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarNfse: Optional[ConsultarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarNfseOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfseconsultasConsultarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarNfseResponse: Optional[ConsultarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfseconsultasConsultarNfseOutput.Body.Fault"] = (
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
class InfseconsultasConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarSituacaoLoteRpsInput.Header"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    Body: Optional["InfseconsultasConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        ConsultarSituacaoLoteRps: Optional[ConsultarSituacaoLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfseconsultasConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfseconsultasConsultarSituacaoLoteRpsOutput.Header"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    Body: Optional["InfseconsultasConsultarSituacaoLoteRpsOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
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
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfseconsultasConsultarSituacaoLoteRpsOutput.Body.Fault"
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
class InfsegeracaoCancelarCartaCorrecaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoCancelarCartaCorrecaoInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoCancelarCartaCorrecaoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        CancelarCartaCorrecao: Optional[CancelarCartaCorrecao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoCancelarCartaCorrecaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoCancelarCartaCorrecaoOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoCancelarCartaCorrecaoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        CancelarCartaCorrecaoResponse: Optional[
            CancelarCartaCorrecaoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfsegeracaoCancelarCartaCorrecaoOutput.Body.Fault"
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
class InfsegeracaoCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoCancelarNfseInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        CancelarNfse: Optional[CancelarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoCancelarNfseOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        CancelarNfseResponse: Optional[CancelarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfsegeracaoCancelarNfseOutput.Body.Fault"] = field(
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
class InfsegeracaoEnviarLoteRpsSincronoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoEnviarLoteRpsSincronoInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoEnviarLoteRpsSincronoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        EnviarLoteRpsSincrono: Optional[EnviarLoteRpsSincrono] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoEnviarLoteRpsSincronoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoEnviarLoteRpsSincronoOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoEnviarLoteRpsSincronoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        EnviarLoteRpsSincronoResponse: Optional[
            EnviarLoteRpsSincronoResponse
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional[
            "InfsegeracaoEnviarLoteRpsSincronoOutput.Body.Fault"
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
class InfsegeracaoGerarCartaCorrecaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoGerarCartaCorrecaoInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoGerarCartaCorrecaoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        GerarCartaCorrecao: Optional[GerarCartaCorrecao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoGerarCartaCorrecaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoGerarCartaCorrecaoOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoGerarCartaCorrecaoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        GerarCartaCorrecaoResponse: Optional[GerarCartaCorrecaoResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )
        Fault: Optional["InfsegeracaoGerarCartaCorrecaoOutput.Body.Fault"] = (
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
class InfsegeracaoGerarManifestacaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoGerarManifestacaoInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoGerarManifestacaoInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        GerarManifestacao: Optional[GerarManifestacao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoGerarManifestacaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoGerarManifestacaoOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoGerarManifestacaoOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        GerarManifestacaoResponse: Optional[GerarManifestacaoResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfsegeracaoGerarManifestacaoOutput.Body.Fault"] = (
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
class InfsegeracaoGerarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoGerarNfseInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoGerarNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        GerarNfse: Optional[GerarNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoGerarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoGerarNfseOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoGerarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        GerarNfseResponse: Optional[GerarNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfsegeracaoGerarNfseOutput.Body.Fault"] = field(
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
class InfsegeracaoRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoRecepcionarLoteRpsInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        RecepcionarLoteRps: Optional[RecepcionarLoteRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoRecepcionarLoteRpsOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoRecepcionarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        RecepcionarLoteRpsResponse: Optional[RecepcionarLoteRpsResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://tempuri.org/",
                },
            )
        )
        Fault: Optional["InfsegeracaoRecepcionarLoteRpsOutput.Body.Fault"] = (
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
class InfsegeracaoSubstituirNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoSubstituirNfseInput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoSubstituirNfseInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        SubstituirNfse: Optional[SubstituirNfse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )


@dataclass
class InfsegeracaoSubstituirNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://tempuri.org/"

    Header: Optional["InfsegeracaoSubstituirNfseOutput.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Body: Optional["InfsegeracaoSubstituirNfseOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        cabecalho: Optional[Cabecalho] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )

    @dataclass
    class Body:
        SubstituirNfseResponse: Optional[SubstituirNfseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://tempuri.org/",
            },
        )
        Fault: Optional["InfsegeracaoSubstituirNfseOutput.Body.Fault"] = field(
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


class InfseIntegracaoDeissConsultarNfseDeiss:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSeIntegracaoDEISS/ConsultarNFSeDEISS"
    input = InfseIntegracaoDeissConsultarNfseDeissInput
    output = InfseIntegracaoDeissConsultarNfseDeissOutput


class InfseIntegracaoDeissConsultarNotasFaltantesNfseDeiss:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSeIntegracaoDEISS/ConsultarNotasFaltantesNFSeDEISS"
    input = InfseIntegracaoDeissConsultarNotasFaltantesNfseDeissInput
    output = InfseIntegracaoDeissConsultarNotasFaltantesNfseDeissOutput


class InfseIntegracaoDeissConsultarTodasNotasPorPeriodo:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://tempuri.org/INFSeIntegracaoDEISS/ConsultarTodasNotasPorPeriodo"
    )
    input = InfseIntegracaoDeissConsultarTodasNotasPorPeriodoInput
    output = InfseIntegracaoDeissConsultarTodasNotasPorPeriodoOutput


class InfseIntegracaoDeissObterNotasDeiss:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSeIntegracaoDEISS/ObterNotasDEISS"
    input = InfseIntegracaoDeissObterNotasDeissInput
    output = InfseIntegracaoDeissObterNotasDeissOutput


class InfseconsultasConsultarCartaCorrecao:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarCartaCorrecao"
    input = InfseconsultasConsultarCartaCorrecaoInput
    output = InfseconsultasConsultarCartaCorrecaoOutput


class InfseconsultasConsultarLoteRps:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarLoteRps"
    input = InfseconsultasConsultarLoteRpsInput
    output = InfseconsultasConsultarLoteRpsOutput


class InfseconsultasConsultarNfse:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarNfse"
    input = InfseconsultasConsultarNfseInput
    output = InfseconsultasConsultarNfseOutput


class InfseconsultasConsultarNfsePorFaixa:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarNfsePorFaixa"
    input = InfseconsultasConsultarNfsePorFaixaInput
    output = InfseconsultasConsultarNfsePorFaixaOutput


class InfseconsultasConsultarNfsePorRps:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarNfsePorRps"
    input = InfseconsultasConsultarNfsePorRpsInput
    output = InfseconsultasConsultarNfsePorRpsOutput


class InfseconsultasConsultarNfseServicoPrestado:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = (
        "http://tempuri.org/INFSEConsultas/ConsultarNfseServicoPrestado"
    )
    input = InfseconsultasConsultarNfseServicoPrestadoInput
    output = InfseconsultasConsultarNfseServicoPrestadoOutput


class InfseconsultasConsultarNfseServicoTomado:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarNfseServicoTomado"
    input = InfseconsultasConsultarNfseServicoTomadoInput
    output = InfseconsultasConsultarNfseServicoTomadoOutput


class InfseconsultasConsultarSituacaoLoteRps:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEConsultas/ConsultarSituacaoLoteRps"
    input = InfseconsultasConsultarSituacaoLoteRpsInput
    output = InfseconsultasConsultarSituacaoLoteRpsOutput


class InfsegeracaoCancelarCartaCorrecao:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/CancelarCartaCorrecao"
    input = InfsegeracaoCancelarCartaCorrecaoInput
    output = InfsegeracaoCancelarCartaCorrecaoOutput


class InfsegeracaoCancelarNfse:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/CancelarNfse"
    input = InfsegeracaoCancelarNfseInput
    output = InfsegeracaoCancelarNfseOutput


class InfsegeracaoEnviarLoteRpsSincrono:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/EnviarLoteRpsSincrono"
    input = InfsegeracaoEnviarLoteRpsSincronoInput
    output = InfsegeracaoEnviarLoteRpsSincronoOutput


class InfsegeracaoGerarCartaCorrecao:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/GerarCartaCorrecao"
    input = InfsegeracaoGerarCartaCorrecaoInput
    output = InfsegeracaoGerarCartaCorrecaoOutput


class InfsegeracaoGerarManifestacao:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/GerarManifestacao"
    input = InfsegeracaoGerarManifestacaoInput
    output = InfsegeracaoGerarManifestacaoOutput


class InfsegeracaoGerarNfse:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/GerarNfse"
    input = InfsegeracaoGerarNfseInput
    output = InfsegeracaoGerarNfseOutput


class InfsegeracaoRecepcionarLoteRps:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/RecepcionarLoteRps"
    input = InfsegeracaoRecepcionarLoteRpsInput
    output = InfsegeracaoRecepcionarLoteRpsOutput


class InfsegeracaoSubstituirNfse:
    style = "document"
    location = "http://nota.montesclaros.mg.gov.br/NFSe.Portal.Integracao/Services.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://tempuri.org/INFSEGeracao/SubstituirNfse"
    input = InfsegeracaoSubstituirNfseInput
    output = InfsegeracaoSubstituirNfseOutput
