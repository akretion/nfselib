from dataclasses import dataclass, field
from typing import Optional
from nfselib.equiplano.tipos_esnfs_v01 import (
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
    mensagem_retorno: Optional[TcMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "mensagemRetorno",
            "type": "Element",
            "namespace": "",
        }
    )
