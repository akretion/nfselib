from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.dueto.tipos_complexos import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://tempuri.org/servico_consultar_lote_rps_resposta.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_lote_rps_resposta.xsd"

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
            "namespace": "http://tempuri.org/tipos_complexos.xsd",
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
