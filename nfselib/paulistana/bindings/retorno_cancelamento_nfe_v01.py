from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import TpEvento

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class RetornoCancelamentoNfe:
    """Schema utilizado para RETORNO de Pedidos de cancelamento de NFS-e.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços qual o resultado do pedido de cancelamento
    de NFS-e.

    :ivar Cabecalho: Cabeçalho do retorno.
    :ivar Alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar Erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """

    class Meta:
        name = "RetornoCancelamentoNFe"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["RetornoCancelamentoNfe.Cabecalho"] = field(
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
