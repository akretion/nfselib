from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.issnet.tipos_complexos import (
    TcIdentificacaoPrestador,
    TcMensagemRetorno,
)

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_url_visualizacao_nfse_resposta.xsd"


@dataclass
class ConsultarUrlVisualizacaoNfseResposta:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_url_visualizacao_nfse_resposta.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
        }
    )
    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "total_digits": 15,
        }
    )
    url_visualizacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "UrlVisualizacao",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional["ConsultarUrlVisualizacaoNfseResposta.ListaMensagemRetorno"] = field(
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
