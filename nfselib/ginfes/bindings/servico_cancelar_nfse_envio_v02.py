from dataclasses import dataclass, field
from typing import Optional

from nfselib.ginfes.bindings.tipos_v02 import TcIdentificacaoPrestador
from nfselib.ginfes.bindings.xmldsig_core_schema_v02 import Signature

__NAMESPACE__ = "http://www.ginfes.com.br/servico_cancelar_nfse_envio"


@dataclass
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_cancelar_nfse_envio"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "total_digits": 15,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )
