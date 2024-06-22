from dataclasses import dataclass, field
from typing import Optional

from nfselib.dueto.bindings.tipos_complexos import TcPedidoCancelamento

__NAMESPACE__ = "http://tempuri.org/servico_enviar_lote_rps_envio.xsd"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://tempuri.org/servico_enviar_lote_rps_envio.xsd"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
