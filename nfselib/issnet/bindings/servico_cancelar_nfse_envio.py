from dataclasses import dataclass, field
from typing import Optional

from nfselib.issnet.bindings.tipos_complexos import TcPedidoCancelamento

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_cancelar_nfse_envio.xsd"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_cancelar_nfse_envio.xsd"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
