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

    ListaNfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://ws.speedgov.com.br/tipos_v1.xsd",
        }
    )

    @dataclass
    class ListaNfse:
        compNfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            }
        )
