from dataclasses import dataclass, field
from typing import Optional
from nfselib.ginfes_v03.tipos_v03 import TcLoteRps
from nfselib.ginfes_v03.xmldsig_core_schema20020212_v03 import Signature

__NAMESPACE__ = "http://www.ginfes.com.br/servico_enviar_lote_rps_envio_v03.xsd"


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_enviar_lote_rps_envio_v03.xsd"

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
