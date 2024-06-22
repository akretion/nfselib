from dataclasses import dataclass, field
from typing import Optional

from nfselib.ginfes.bindings.tipos_v03 import (
    ListaMensagemRetorno,
    TcCancelamentoNfse,
)

__NAMESPACE__ = (
    "http://www.ginfes.com.br/servico_cancelar_nfse_resposta_v03.xsd"
)


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = (
            "http://www.ginfes.com.br/servico_cancelar_nfse_resposta_v03.xsd"
        )

    Cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )
