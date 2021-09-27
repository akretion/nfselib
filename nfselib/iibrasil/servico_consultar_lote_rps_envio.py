from dataclasses import dataclass, field
from typing import Optional
from nfselib.iibrasil.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = "http://tempuri.org/servico_consultar_lote_rps_envio.xsd"


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_lote_rps_envio.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
        }
    )
