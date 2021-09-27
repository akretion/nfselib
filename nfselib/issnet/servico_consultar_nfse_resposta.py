from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.issnet.tipos_complexos import (
    TcCompNfse,
    TcMensagemRetorno,
)

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_nfse_resposta.xsd"


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_nfse_resposta.xsd"

    lista_nfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional["ConsultarNfseResposta.ListaMensagemRetorno"] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )

    @dataclass
    class ListaNfse:
        comp_nfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
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
