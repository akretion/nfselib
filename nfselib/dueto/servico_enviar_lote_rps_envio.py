from dataclasses import dataclass, field
from typing import Optional
from nfselib.dueto.core_schema import Signature
from nfselib.dueto.tipos_complexos import TcLoteRps

__NAMESPACE__ = "http://tempuri.org/servico_enviar_lote_rps_envio.xsd"


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://tempuri.org/servico_enviar_lote_rps_envio.xsd"

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
