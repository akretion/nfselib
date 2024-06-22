from dataclasses import dataclass, field
from typing import Optional

from nfselib.intersol.bindings.tipos_v1 import ListaMensagemRetorno

__NAMESPACE__ = (
    "http://ws.speedgov.com.br/consultar_situacao_lote_rps_resposta_v1.xsd"
)


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://ws.speedgov.com.br/consultar_situacao_lote_rps_resposta_v1.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
            "white_space": "collapse",
        },
    )
    Situacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "collapse",
            "pattern": r"1|2|3|4",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://ws.speedgov.com.br/tipos_v1.xsd",
        },
    )
