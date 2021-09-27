from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.issnet.tipos_complexos import TcMensagemRetorno

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_enviar_lote_rps_resposta.xsd"


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_enviar_lote_rps_resposta.xsd"

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
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        }
    )
    lista_mensagem_retorno: Optional["EnviarLoteRpsResposta.ListaMensagemRetorno"] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaMensagemRetorno:
        mensagem_retorno: List[TcMensagemRetorno] = field(
            default_factory=list,
            metadata={
                "name": "MensagemRetorno",
                "type": "Element",
                "min_occurs": 1,
            }
        )
