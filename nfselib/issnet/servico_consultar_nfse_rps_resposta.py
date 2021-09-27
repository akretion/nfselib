from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.issnet.tipos_complexos import (
    TcCompNfse,
    TcMensagemRetorno,
)

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_nfse_rps_resposta.xsd"


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_nfse_rps_resposta.xsd"

    comp_nfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional["ConsultarNfseRpsResposta.ListaMensagemRetorno"] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
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
