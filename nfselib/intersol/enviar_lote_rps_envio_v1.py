from dataclasses import dataclass, field
from typing import Optional
from nfselib.intersol.tipos_v1 import TcLoteRps
from nfselib.intersol.xmldsig_core_schema20020212_v1 import Signature

__NAMESPACE__ = "http://ws.speedgov.com.br/enviar_lote_rps_envio_v1.xsd"


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://ws.speedgov.com.br/enviar_lote_rps_envio_v1.xsd"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
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
