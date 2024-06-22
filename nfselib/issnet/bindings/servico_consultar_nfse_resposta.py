from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.issnet.bindings.tipos_complexos import (
    TcCompNfse,
    TcMensagemRetorno,
)

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_nfse_resposta.xsd"


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_nfse_resposta.xsd"

    ListaNfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[
        "ConsultarNfseResposta.ListaMensagemRetorno"
    ] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
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

    @dataclass
    class ListaMensagemRetorno:
        MensagemRetorno: List[TcMensagemRetorno] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )
