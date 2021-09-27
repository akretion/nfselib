from dataclasses import dataclass, field
from typing import Optional
from nfselib.intersol.tipos_v1 import (
    ListaMensagemRetorno,
    TcCancelamentoNfse,
)

__NAMESPACE__ = "http://ws.speedgov.com.br/cancelar_nfse_resposta_v1.xsd"


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://ws.speedgov.com.br/cancelar_nfse_resposta_v1.xsd"

    cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "Cancelamento",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://ws.speedgov.com.br/tipos_v1.xsd",
        }
    )
