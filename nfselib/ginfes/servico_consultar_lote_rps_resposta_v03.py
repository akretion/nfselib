from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.ginfes.tipos_v03 import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://www.ginfes.com.br/servico_consultar_lote_rps_resposta_v03.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_consultar_lote_rps_resposta_v03.xsd"

    lista_nfse: Optional["ConsultarLoteRpsResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
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

    @dataclass
    class ListaNfse:
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            }
        )
