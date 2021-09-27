from dataclasses import dataclass, field
from typing import Optional
from nfselib.webiss.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

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
        }
    )
