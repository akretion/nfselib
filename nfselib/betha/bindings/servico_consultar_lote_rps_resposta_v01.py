from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    ListaNfse: Optional["ConsultarLoteRpsResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    listaMensagemRetorno: Optional[
        "ConsultarLoteRpsResposta.ListaMensagemRetorno"
    ] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class ListaNfse:
        nfse: List[str] = field(
            default_factory=list,
            metadata={
                "name": "Nfse",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )

    @dataclass
    class ListaMensagemRetorno:
        MensagemRetorno: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
