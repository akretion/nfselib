from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.webiss.tipos_complexos import (
    ListaMensagemRetorno,
    ListaMensagemRetornoLote,
    TcCompNfse,
)

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    lista_nfse: Optional["ConsultarLoteRpsResposta.ListaNfse"] = field(
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
        }
    )
    lista_mensagem_retorno_lote: Optional[ListaMensagemRetornoLote] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            }
        )
