from dataclasses import dataclass, field
from typing import Optional
from nfselib.issnet.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_situacao_lote_rps_envio.xsd"


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_situacao_lote_rps_envio.xsd"

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
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        }
    )
