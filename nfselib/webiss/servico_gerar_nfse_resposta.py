from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.webiss.tipos_complexos import (
    ListaMensagemRetorno,
    ListaMensagemRetornoLote,
    TcCompNfse,
)

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        }
    )
    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
        }
    )
    lista_nfse: Optional["GerarNfseResposta.ListaNfse"] = field(
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
