from dataclasses import dataclass, field
from typing import Optional
from nfselib.issnet.tipos_complexos import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_nfse_rps_envio.xsd"


@dataclass
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_nfse_rps_envio.xsd"

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
