from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.issnet.tipos_complexos import TcMensagemRetorno

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_situacao_lote_rps_resposta.xsd"


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_situacao_lote_rps_resposta.xsd"

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
    lista_mensagem_retorno: Optional["ConsultarSituacaoLoteRpsResposta.ListaMensagemRetorno"] = field(
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
