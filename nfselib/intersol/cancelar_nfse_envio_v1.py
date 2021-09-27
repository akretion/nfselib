from dataclasses import dataclass, field
from typing import Optional
from nfselib.intersol.tipos_v1 import TcPedidoCancelamento

__NAMESPACE__ = "http://ws.speedgov.com.br/cancelar_nfse_envio_v1.xsd"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://ws.speedgov.com.br/cancelar_nfse_envio_v1.xsd"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
