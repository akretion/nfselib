from dataclasses import dataclass, field
from typing import Optional

from nfselib.dueto.bindings.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = "http://tempuri.org/servico_consultar_lote_rps_envio.xsd"


@dataclass
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_lote_rps_envio.xsd"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        },
    )
