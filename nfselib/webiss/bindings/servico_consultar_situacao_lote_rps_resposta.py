from dataclasses import dataclass, field
from typing import Optional

from nfselib.webiss.bindings.tipos_complexos import ListaMensagemRetorno

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    Situacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"1|2|3|4",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        },
    )
