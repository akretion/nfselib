from dataclasses import dataclass, field
from typing import Optional
from nfselib.bindings.equiplano.tipos_esnfs_v01 import (
    TcIdentificacaoNfse,
    TcMensagemRetorno,
)

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsConsultarNfsePorRpsResposta:
    class Meta:
        name = "esConsultarNfsePorRpsResposta"
        namespace = "http://www.equiplano.com.br/esnfs"

    nfse: Optional[TcIdentificacaoNfse] = field(
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
