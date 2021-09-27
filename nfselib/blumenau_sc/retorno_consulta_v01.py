from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.blumenau_sc.tipos_nfe_v01 import (
    TpEvento,
    TpNfe,
)

__NAMESPACE__ = "http://nfse.blumenau.sc.gov.br"


@dataclass
class RetornoConsulta:
    """Schema utilizado para RETORNO de pedidos de consulta de NFS-e/RPS,
    consultade NFS-e recebidas e consulta de lote.

    Este Schema XML é utilizado pelo Web Service para informar aos
    tomadores e/ou prestadores de serviços o resultado de pedidos de
    consulta de NFS-e/RPS, consultade NFS-e recebidas e consulta de
    lote.

    :ivar cabecalho: Cabeçalho do retorno.
    :ivar alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    :ivar nfe: Elemento NFe - Cada item será um NFS-e.
    """
    class Meta:
        namespace = "http://nfse.blumenau.sc.gov.br"

    cabecalho: Optional["RetornoConsulta.Cabecalho"] = field(
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
    nfe: List[TpNfe] = field(
        default_factory=list,
        metadata={
            "name": "NFe",
            "type": "Element",
            "namespace": "",
            "max_occurs": 50,
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar sucesso: Campo indicativo do sucesso do pedido do serviço.
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
