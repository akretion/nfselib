from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.intersol.tipos_v1 import ListaMensagemRetorno

__NAMESPACE__ = "http://ws.speedgov.com.br/enviar_lote_rps_resposta_v1.xsd"


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://ws.speedgov.com.br/enviar_lote_rps_resposta_v1.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
            "white_space": "collapse",
        }
    )
    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
            "white_space": "collapse",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://ws.speedgov.com.br/tipos_v1.xsd",
        }
    )
