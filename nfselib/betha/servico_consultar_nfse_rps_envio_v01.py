from dataclasses import dataclass, field
from typing import Optional
from nfselib.betha.tipos_nfe_v01 import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class ConsultarNfsePorRpsEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
