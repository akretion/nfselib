from dataclasses import dataclass, field
from typing import Optional
from nfselib.ginfes.tipos_v02 import TcIdentificacaoPrestador
from nfselib.ginfes.xmldsig_core_schema20020212_v03 import Signature

__NAMESPACE__ = "http://www.ginfes.com.br/servico_cancelar_nfse_envio"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_cancelar_nfse_envio"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "required": True,
            "total_digits": 15,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
