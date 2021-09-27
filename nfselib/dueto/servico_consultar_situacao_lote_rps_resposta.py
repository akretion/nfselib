from dataclasses import dataclass, field
from typing import Optional
from nfselib.dueto.tipos_complexos import ListaMensagemRetorno

__NAMESPACE__ = "http://tempuri.org/servico_consultar_situacao_lote_rps_resposta.xsd"


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_situacao_lote_rps_resposta.xsd"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        }
    )
    situacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
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
