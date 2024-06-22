from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nfse",
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
