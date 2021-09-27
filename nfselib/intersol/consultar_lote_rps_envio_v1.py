from dataclasses import dataclass, field
from typing import Optional
from nfselib.intersol.tipos_v1 import TcIdentificacaoPrestador
from nfselib.intersol.xmldsig_core_schema20020212_v1 import Signature

__NAMESPACE__ = "http://ws.speedgov.com.br/consultar_lote_rps_envio_v1.xsd"


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://ws.speedgov.com.br/consultar_lote_rps_envio_v1.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "required": True,
            "max_length": 50,
            "white_space": "collapse",
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "max_length": 255,
            "white_space": "collapse",
        }
    )
