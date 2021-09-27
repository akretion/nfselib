from dataclasses import dataclass, field
from typing import Optional
from nfselib.webiss.tipos_complexos import (
    ListaMensagemRetorno,
    RetCancelamento,
)

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    ret_cancelamento: Optional[RetCancelamento] = field(
        default=None,
        metadata={
            "name": "RetCancelamento",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )
