from dataclasses import dataclass, field
from typing import Optional

from nfselib.webiss.bindings.tipos_complexos import (
    ListaMensagemRetorno,
    RetCancelamento,
)

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    retCancelamento: Optional[RetCancelamento] = field(
        default=None,
        metadata={
            "name": "RetCancelamento",
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )
