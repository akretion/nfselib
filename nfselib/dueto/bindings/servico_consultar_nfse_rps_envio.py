from dataclasses import dataclass, field
from typing import Optional

from nfselib.dueto.bindings.tipos_complexos import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)

__NAMESPACE__ = "http://tempuri.org/servico_consultar_nfse_rps_envio.xsd"


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_nfse_rps_envio.xsd"

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
