from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    ListaNfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    MensagemRetorno: Optional[str] = field(
        default=None,
        metadata={
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
            },
        )
