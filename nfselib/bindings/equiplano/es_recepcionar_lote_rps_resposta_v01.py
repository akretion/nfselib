from dataclasses import dataclass, field
from typing import Optional
from nfselib.bindings.equiplano.tipos_esnfs_v01 import (
    TcMensagemRetorno,
    TcProtocolo,
)

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        name = "enviarLoteRpsResposta"
        namespace = "http://www.equiplano.com.br/esnfs"

    protocolo: Optional[TcProtocolo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    mensagemRetorno: Optional[TcMensagemRetorno] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
