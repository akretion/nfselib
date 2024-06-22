from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.dueto.bindings.tipos_complexos import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://tempuri.org/servico_consultar_lote_rps_resposta.xsd"


@dataclass
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = (
            "http://tempuri.org/servico_consultar_lote_rps_resposta.xsd"
        )

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
            "namespace": "http://tempuri.org/tipos_complexos.xsd",
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
