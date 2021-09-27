from dataclasses import dataclass, field
from typing import Optional
from nfselib.webiss.tipos_complexos import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

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
