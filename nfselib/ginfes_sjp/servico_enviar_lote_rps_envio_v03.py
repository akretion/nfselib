from dataclasses import dataclass, field
from typing import Optional
from nfselib.ginfes_sjp.tipos_v03 import TcLoteRps
from nfselib.ginfes_sjp.xmldsig_core_schema20020212_v03 import Signature

__NAMESPACE__ = "http://nfe.sjp.pr.gov.br/servico_enviar_lote_rps_envio_v03.xsd"


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://nfe.sjp.pr.gov.br/servico_enviar_lote_rps_envio_v03.xsd"

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