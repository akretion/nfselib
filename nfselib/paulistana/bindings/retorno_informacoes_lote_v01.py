from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import (
    TpEvento,
    TpInformacoesLote,
)

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class RetornoInformacoesLote:
    """Schema utilizado para RETORNO de Pedidos de Informações de Lote.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços o resultado do pedido de informações de
    lote.

    :ivar Cabecalho: Cabeçalho do retorno.
    :ivar Alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar Erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """

    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["RetornoInformacoesLote.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Alerta: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Erro: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar Sucesso: Campo indicativo do sucesso do pedido do serviço.
        :ivar InformacoesLote: Informações do lote consultado.
        :ivar Versao: Versão do Schema XML utilizado.
        """

        Sucesso: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        InformacoesLote: Optional[TpInformacoesLote] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        Versao: str = field(
            init=False,
            default="1",
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )
