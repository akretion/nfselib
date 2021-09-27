from dataclasses import dataclass, field
from typing import Optional
from nfselib.ginfes.tipos_v03 import ListaMensagemRetorno

__NAMESPACE__ = "http://www.ginfes.com.br/servico_consultar_situacao_lote_rps_resposta_v03.xsd"


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_consultar_situacao_lote_rps_resposta_v03.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
            "white_space": "collapse",
        }
    )
    situacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
            "white_space": "collapse",
            "pattern": r"1|2|3|4",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        }
    )
