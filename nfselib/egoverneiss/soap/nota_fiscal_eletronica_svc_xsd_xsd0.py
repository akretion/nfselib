from dataclasses import dataclass, field
from typing import Optional

from nfselib.egoverneiss.soap.nota_fiscal_eletronica_svc_xsd_xsd2 import (
    CancelamentoNotaFiscalLoteRequest,
    CancelamentoNotaFiscalLoteResponse,
    CancelamentoNotaFiscalRepasseRequest,
    CancelamentoNotaFiscalRequest,
    CancelamentoNotaFiscalResponse,
    ConsultaCancelamentoNotasLoteRequest,
    ConsultaExecutoresVinculadosRequest,
    ConsultaExecutoresVinculadosResponse,
    ConsultaNotaFiscalCompletaResponse,
    ConsultaNotaFiscalLoteRequest,
    ConsultaNotaFiscalLoteResponse,
    ConsultaNotaFiscalRepasseR2LoteRequest,
    ConsultaNotaFiscalRepasseR2LoteResponse,
    ConsultaNotaFiscalRepasseR2Response,
    ConsultaNotaFiscalRepasseRequest,
    ConsultaNotaFiscalRepasseResponse,
    ConsultaNotaFiscalRequest,
    ConsultaNotaFiscalResponse,
    EmissaoNotaFiscalLoteRequest,
    EmissaoNotaFiscalLoteResponse,
    EmissaoNotaFiscalRepasseR2LoteRequest,
    EmissaoNotaFiscalRepasseR2LoteResponse,
    EmissaoNotaFiscalRepasseR2Request,
    EmissaoNotaFiscalRepasseRequest,
    EmissaoNotaFiscalRepasseResponse,
    EmissaoNotaFiscalRequest,
    EmissaoNotaFiscalResponse,
    EnviarExecutoresRequest,
)
from nfselib.egoverneiss.soap.nota_fiscal_eletronica_svc_xsd_xsd2 import (
    ConsultaCancelamentoNotasLoteResponse as NotaFiscalEletronicaSvcXsdXsd2ConsultaCancelamentoNotasLoteResponse,
)
from nfselib.egoverneiss.soap.nota_fiscal_eletronica_svc_xsd_xsd2 import (
    EnviarExecutoresResponse as NotaFiscalEletronicaSvcXsdXsd2EnviarExecutoresResponse,
)

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class Cancelar:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[CancelamentoNotaFiscalRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelarNotaLote:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[CancelamentoNotaFiscalLoteRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelarNotaLoteResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    CancelarNotaLoteResult: Optional[CancelamentoNotaFiscalLoteResponse] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
    )


@dataclass
class CancelarNotaRepasse:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[CancelamentoNotaFiscalRepasseRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelarNotaRepasseR2:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[CancelamentoNotaFiscalRepasseRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelarNotaRepasseR2Response:
    class Meta:
        namespace = "http://tempuri.org/"

    CancelarNotaRepasseR2Result: Optional[CancelamentoNotaFiscalResponse] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
    )


@dataclass
class CancelarNotaRepasseResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    CancelarNotaRepasseResult: Optional[CancelamentoNotaFiscalResponse] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
    )


@dataclass
class CancelarResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    CancelarResult: Optional[CancelamentoNotaFiscalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaCancelamentoNotasLote:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[ConsultaCancelamentoNotasLoteRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaCancelamentoNotasLoteResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultaCancelamentoNotasLoteResult: Optional[
        NotaFiscalEletronicaSvcXsdXsd2ConsultaCancelamentoNotasLoteResponse
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaNotasRepasseR2Lote:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[ConsultaNotaFiscalRepasseR2LoteRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaNotasRepasseR2LoteResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultaNotasRepasseR2LoteResult: Optional[
        ConsultaNotaFiscalRepasseR2LoteResponse
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class Consultar:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[ConsultaNotaFiscalRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarExecutores:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[ConsultaExecutoresVinculadosRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarExecutoresResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarExecutoresResult: Optional[
        ConsultaExecutoresVinculadosResponse
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarLote:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[ConsultaNotaFiscalLoteRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarLoteResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarLoteResult: Optional[ConsultaNotaFiscalLoteResponse] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNfr:
    class Meta:
        name = "ConsultarNFR"
        namespace = "http://tempuri.org/"

    request: Optional[ConsultaNotaFiscalRepasseRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNfr2:
    class Meta:
        name = "ConsultarNFR2"
        namespace = "http://tempuri.org/"

    request: Optional[ConsultaNotaFiscalRepasseRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNfr2Response:
    class Meta:
        name = "ConsultarNFR2Response"
        namespace = "http://tempuri.org/"

    ConsultarNFR2Result: Optional[ConsultaNotaFiscalRepasseR2Response] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNfrresponse:
    class Meta:
        name = "ConsultarNFRResponse"
        namespace = "http://tempuri.org/"

    ConsultarNFRResult: Optional[ConsultaNotaFiscalRepasseResponse] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNotaCompleta:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[ConsultaNotaFiscalRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarNotaCompletaResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarNotaCompletaResult: Optional[
        ConsultaNotaFiscalCompletaResponse
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultarResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    ConsultarResult: Optional[ConsultaNotaFiscalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class Emitir:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[EmissaoNotaFiscalRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmitirEmLote:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[EmissaoNotaFiscalLoteRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmitirEmLoteRepasseR2:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[EmissaoNotaFiscalRepasseR2LoteRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmitirEmLoteRepasseR2Response:
    class Meta:
        namespace = "http://tempuri.org/"

    EmitirEmLoteRepasseR2Result: Optional[
        EmissaoNotaFiscalRepasseR2LoteResponse
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmitirEmLoteResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EmitirEmLoteResult: Optional[EmissaoNotaFiscalLoteResponse] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmitirNotaRepasse:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[EmissaoNotaFiscalRepasseRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmitirNotaRepasseR2:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[EmissaoNotaFiscalRepasseR2Request] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmitirNotaRepasseR2Response:
    class Meta:
        namespace = "http://tempuri.org/"

    EmitirNotaRepasseR2Result: Optional[EmissaoNotaFiscalRepasseResponse] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
    )


@dataclass
class EmitirNotaRepasseResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EmitirNotaRepasseResult: Optional[EmissaoNotaFiscalRepasseResponse] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
    )


@dataclass
class EmitirResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EmitirResult: Optional[EmissaoNotaFiscalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EnviarExecutores:
    class Meta:
        namespace = "http://tempuri.org/"

    request: Optional[EnviarExecutoresRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EnviarExecutoresResponse:
    class Meta:
        namespace = "http://tempuri.org/"

    EnviarExecutoresResult: Optional[
        NotaFiscalEletronicaSvcXsdXsd2EnviarExecutoresResponse
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
