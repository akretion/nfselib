from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import (
    TpEvento,
    TpNfe,
)

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class RetornoConsulta:
    """Schema utilizado para RETORNO de pedidos de consulta de NFS-e/RPS,
    consultade NFS-e recebidas e consulta de lote.

    Este Schema XML é utilizado pelo Web Service para informar aos
    tomadores e/ou prestadores de serviços o resultado de pedidos de
    consulta de NFS-e/RPS, consultade NFS-e recebidas e consulta de
    lote.

    :ivar Cabecalho: Cabeçalho do retorno.
    :ivar Alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar Erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    :ivar NFe: Elemento NFe - Cada item será um NFS-e.
    """

    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["RetornoConsulta.Cabecalho"] = field(
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
    NFe: List[TpNfe] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 50,
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar Sucesso: Campo indicativo do sucesso do pedido do serviço.
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
        Versao: str = field(
            init=False,
            default="1",
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )
