from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.dueto.tipos_complexos import ListaMensagemRetorno

__NAMESPACE__ = "http://tempuri.org/servico_enviar_lote_rps_resposta.xsd"


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_enviar_lote_rps_resposta.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
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
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://tempuri.org/tipos_complexos.xsd",
        }
    )
