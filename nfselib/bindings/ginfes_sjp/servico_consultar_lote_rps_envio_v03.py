from dataclasses import dataclass, field
from typing import Optional
from nfselib.bindings.ginfes_sjp.tipos_v03 import TcIdentificacaoPrestador
from nfselib.bindings.ginfes_sjp.xmldsig_core_schema20020212_v03 import Signature

__NAMESPACE__ = "http://nfe.sjp.pr.gov.br/servico_consultar_lote_rps_envio_v03.xsd"


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://nfe.sjp.pr.gov.br/servico_consultar_lote_rps_envio_v03.xsd"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
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
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
            "white_space": "collapse",
        }
    )
