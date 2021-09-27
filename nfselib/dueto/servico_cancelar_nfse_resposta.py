from dataclasses import dataclass, field
from typing import Optional
from nfselib.dueto.tipos_complexos import (
    ListaMensagemRetorno,
    TcCancelamentoNfse,
)

__NAMESPACE__ = "http://tempuri.org/servico_cancelar_nfse_resposta.xsd"


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_cancelar_nfse_resposta.xsd"

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
            "namespace": "http://tempuri.org/tipos_complexos.xsd",
        }
    )
