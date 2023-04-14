from dataclasses import dataclass, field
from typing import Optional
from nfselib.equiplano.tipos_esnfs_v01 import TcMensagemRetorno

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsConsultarSituacaoLoteRpsResposta:
    class Meta:
        name = "esConsultarSituacaoLoteRpsResposta"
        namespace = "http://www.equiplano.com.br/esnfs"

    nr_lote_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrLoteRps",
            "type": "Element",
            "namespace": "",
        }
    )
    st_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "stLote",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-4]{1}",
        }
    )
    mensagem_retorno: Optional[TcMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "mensagemRetorno",
            "type": "Element",
            "namespace": "",
        }
    )