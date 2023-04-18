from dataclasses import dataclass, field
from typing import Optional
from nfselib.ginfes_sjp.tipos_v03 import TcPedidoCancelamento
from nfselib.ginfes_sjp.xmldsig_core_schema20020212_v03 import Signature

__NAMESPACE__ = "http://nfe.sjp.pr.gov.br/servico_cancelar_nfse_envio_v03.xsd"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://nfe.sjp.pr.gov.br/servico_cancelar_nfse_envio_v03.xsd"

    Pedido: Optional[TcPedidoCancelamento] = field(
        default=None,
        metadata={
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
