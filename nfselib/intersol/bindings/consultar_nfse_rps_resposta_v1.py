from dataclasses import dataclass, field
from typing import Optional

from nfselib.intersol.bindings.tipos_v1 import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://ws.speedgov.com.br/consultar_nfse_rps_resposta_v1.xsd"


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = (
            "http://ws.speedgov.com.br/consultar_nfse_rps_resposta_v1.xsd"
        )

    compNfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://ws.speedgov.com.br/tipos_v1.xsd",
        },
    )
