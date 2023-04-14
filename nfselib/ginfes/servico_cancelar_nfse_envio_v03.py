from dataclasses import dataclass, field
from typing import Optional
from nfselib.ginfes.tipos_v03 import TcPedidoCancelamento
from nfselib.ginfes.xmldsig_core_schema20020212_v03 import Signature

__NAMESPACE__ = "http://www.ginfes.com.br/servico_cancelar_nfse_envio_v03.xsd"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_cancelar_nfse_envio_v03.xsd"

    pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
