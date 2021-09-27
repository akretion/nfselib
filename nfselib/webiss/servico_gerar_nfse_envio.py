from dataclasses import dataclass, field
from typing import Optional
from nfselib.webiss.tipos_complexos import TcLoteRps3
from nfselib.webiss.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    lote_rps: Optional[TcLoteRps3] = field(
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
