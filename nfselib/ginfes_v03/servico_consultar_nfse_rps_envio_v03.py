from dataclasses import dataclass, field
from typing import Optional
from nfselib.ginfes_v03.tipos_v03 import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)
from nfselib.ginfes_v03.xmldsig_core_schema20020212_v03 import Signature

__NAMESPACE__ = "http://www.ginfes.com.br/servico_consultar_nfse_rps_envio_v03.xsd"


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_consultar_nfse_rps_envio_v03.xsd"

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
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
