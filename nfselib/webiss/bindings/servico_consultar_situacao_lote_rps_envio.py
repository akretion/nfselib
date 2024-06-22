from dataclasses import dataclass, field
from typing import Optional

from nfselib.webiss.bindings.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 50,
        },
    )
