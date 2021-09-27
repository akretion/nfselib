from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.intersol.tipos_v1 import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://ws.speedgov.com.br/consultar_nfse_resposta_v1.xsd"


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://ws.speedgov.com.br/consultar_nfse_resposta_v1.xsd"

    lista_nfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
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

    @dataclass
    class ListaNfse:
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            }
        )
