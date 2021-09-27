from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.issnet.tipos_complexos import (
    TcCancelamentoNfse,
    TcMensagemRetorno,
)

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_cancelar_nfse_resposta.xsd"


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_cancelar_nfse_resposta.xsd"

    cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "Cancelamento",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional["CancelarNfseResposta.ListaMensagemRetorno"] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaMensagemRetorno:
        mensagem_retorno: List[TcMensagemRetorno] = field(
            default_factory=list,
            metadata={
                "name": "MensagemRetorno",
                "type": "Element",
                "min_occurs": 1,
            }
        )
