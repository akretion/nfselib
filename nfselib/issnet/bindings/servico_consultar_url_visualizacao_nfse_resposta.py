from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.issnet.bindings.tipos_complexos import (
    TcIdentificacaoPrestador,
    TcMensagemRetorno,
)

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_url_visualizacao_nfse_resposta.xsd"


@dataclass
class ConsultarUrlVisualizacaoNfseResposta:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_url_visualizacao_nfse_resposta.xsd"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    UrlVisualizacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[
        "ConsultarUrlVisualizacaoNfseResposta.ListaMensagemRetorno"
    ] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
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
