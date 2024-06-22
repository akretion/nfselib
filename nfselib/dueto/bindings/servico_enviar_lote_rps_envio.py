from dataclasses import dataclass, field
from typing import Optional

from nfselib.dueto.bindings.tipos_complexos import TcLoteRps
from nfselib.dueto.bindings.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://tempuri.org/servico_enviar_lote_rps_envio.xsd"


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://tempuri.org/servico_enviar_lote_rps_envio.xsd"

    LoteRps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
