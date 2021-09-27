from dataclasses import dataclass, field
from typing import Optional
from nfselib.intersol.tipos_v1 import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)

__NAMESPACE__ = "http://ws.speedgov.com.br/consultar_nfse_rps_envio_v1.xsd"


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://ws.speedgov.com.br/consultar_nfse_rps_envio_v1.xsd"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
