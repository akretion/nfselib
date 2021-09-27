from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.equiplano.tipos_esnfs_v01 import (
    TcMensagemRetorno,
    TcNfse,
)

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsConsultarLoteRpsResposta:
    class Meta:
        name = "esConsultarLoteRpsResposta"
        namespace = "http://www.equiplano.com.br/esnfs"

    lista_nfse: Optional["EsConsultarLoteRpsResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "listaNfse",
            "type": "Element",
            "namespace": "",
        }
    )
    mensagem_retorno: Optional[TcMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "mensagemRetorno",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ListaNfse:
        nfse: List[TcNfse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
