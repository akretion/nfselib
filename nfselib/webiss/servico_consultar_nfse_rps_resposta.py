from dataclasses import dataclass, field
from typing import Optional
from nfselib.webiss.tipos_complexos import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    comp_nfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )
