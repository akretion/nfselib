from dataclasses import dataclass, field
from typing import Optional

from nfselib.ginfes.bindings.tipos_v03 import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = (
    "http://www.ginfes.com.br/servico_consultar_nfse_rps_resposta_v03.xsd"
)


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.ginfes.com.br/servico_consultar_nfse_rps_resposta_v03.xsd"

    compNfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
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
