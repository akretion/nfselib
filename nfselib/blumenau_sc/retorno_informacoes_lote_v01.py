from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.blumenau_sc.tipos_nfe_v01 import (
    TpEvento,
    TpInformacoesLote,
)

__NAMESPACE__ = "http://nfse.blumenau.sc.gov.br"


@dataclass
class RetornoInformacoesLote:
    """Schema utilizado para RETORNO de Pedidos de Informações de Lote.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços o resultado do pedido de informações de
    lote.

    :ivar cabecalho: Cabeçalho do retorno.
    :ivar alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """
    class Meta:
        namespace = "http://nfse.blumenau.sc.gov.br"

    cabecalho: Optional["RetornoInformacoesLote.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    alerta: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "name": "Alerta",
            "type": "Element",
            "namespace": "",
        }
    )
    erro: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "name": "Erro",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar sucesso: Campo indicativo do sucesso do pedido do serviço.
        :ivar informacoes_lote: Informações do lote consultado.
        :ivar versao: Versão do Schema XML utilizado.
        """
        sucesso: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Sucesso",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        informacoes_lote: Optional[TpInformacoesLote] = field(
            default=None,
            metadata={
                "name": "InformacoesLote",
                "type": "Element",
                "namespace": "",
            }
        )
        versao: str = field(
            init=False,
            default="1",
            metadata={
                "name": "Versao",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )
