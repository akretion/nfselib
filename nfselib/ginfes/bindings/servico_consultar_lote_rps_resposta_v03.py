from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.ginfes.bindings.tipos_v03 import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = (
    "http://www.ginfes.com.br/servico_consultar_lote_rps_resposta_v03.xsd"
)


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_consultar_lote_rps_resposta_v03.xsd"

    ListaNfse: Optional["ConsultarLoteRpsResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.ginfes.com.br/tipos_v03.xsd",
        },
    )

    @dataclass
    class ListaNfse:
        compNfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "min_occurs": 1,
            },
        )
