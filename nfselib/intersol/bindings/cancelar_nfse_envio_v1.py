from dataclasses import dataclass, field
from typing import Optional

from nfselib.intersol.bindings.tipos_v1 import TcPedidoCancelamento

__NAMESPACE__ = "http://ws.speedgov.com.br/cancelar_nfse_envio_v1.xsd"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://ws.speedgov.com.br/cancelar_nfse_envio_v1.xsd"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
