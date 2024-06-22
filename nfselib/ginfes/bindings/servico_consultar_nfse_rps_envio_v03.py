from dataclasses import dataclass, field
from typing import Optional

from nfselib.ginfes.bindings.tipos_v03 import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)
from nfselib.ginfes.bindings.xmldsig_core_schema_v02 import Signature

__NAMESPACE__ = (
    "http://www.ginfes.com.br/servico_consultar_nfse_rps_envio_v03.xsd"
)


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = (
            "http://www.ginfes.com.br/servico_consultar_nfse_rps_envio_v03.xsd"
        )

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
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
