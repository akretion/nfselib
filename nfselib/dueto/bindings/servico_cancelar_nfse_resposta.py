from dataclasses import dataclass, field
from typing import Optional

from nfselib.dueto.bindings.tipos_complexos import (
    ListaMensagemRetorno,
    TcCancelamentoNfse,
)

__NAMESPACE__ = "http://tempuri.org/servico_cancelar_nfse_resposta.xsd"


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_cancelar_nfse_resposta.xsd"

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
            "namespace": "http://tempuri.org/tipos_complexos.xsd",
        },
    )
