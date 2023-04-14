from dataclasses import dataclass, field
from typing import Optional
from nfselib.equiplano.tipos_esnfs_v01 import TcMensagemRetorno

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsConsultarSituacaoLoteRpsResposta:
    class Meta:
        name = "esConsultarSituacaoLoteRpsResposta"
        namespace = "http://www.equiplano.com.br/esnfs"

    nrLoteRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    stLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-4]{1}",
        }
    )
    mensagemRetorno: Optional[TcMensagemRetorno] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
