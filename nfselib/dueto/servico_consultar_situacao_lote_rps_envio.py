from dataclasses import dataclass, field
from typing import Optional
from nfselib.dueto.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = "http://tempuri.org/servico_consultar_situacao_lote_rps_envio.xsd"


@dataclass
class ConsultarSituacaoLoteRpsEnvio:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_situacao_lote_rps_envio.xsd"

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
