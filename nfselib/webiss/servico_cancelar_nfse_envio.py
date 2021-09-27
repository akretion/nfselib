from dataclasses import dataclass, field
from typing import Optional
from nfselib.webiss.tipos_complexos import TcPedidoCancelamento

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "required": True,
        }
    )
