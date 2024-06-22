from dataclasses import dataclass, field
from typing import Optional

from nfselib.intersol.bindings.tipos_v1 import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)

__NAMESPACE__ = "http://ws.speedgov.com.br/consultar_nfse_rps_envio_v1.xsd"


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://ws.speedgov.com.br/consultar_nfse_rps_envio_v1.xsd"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
