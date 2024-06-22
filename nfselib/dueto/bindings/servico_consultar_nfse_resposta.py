from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.dueto.bindings.tipos_complexos import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://tempuri.org/servico_consultar_nfse_resposta.xsd"


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_nfse_resposta.xsd"

    ListaNfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
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
            },
        )
