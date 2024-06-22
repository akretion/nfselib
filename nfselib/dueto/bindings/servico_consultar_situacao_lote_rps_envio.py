from dataclasses import dataclass, field
from typing import Optional

from nfselib.dueto.bindings.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = (
    "http://tempuri.org/servico_consultar_situacao_lote_rps_envio.xsd"
)


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = (
            "http://tempuri.org/servico_consultar_situacao_lote_rps_envio.xsd"
        )

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
