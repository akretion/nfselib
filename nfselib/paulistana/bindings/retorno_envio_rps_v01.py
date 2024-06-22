from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import (
    TpChaveNfeRps,
    TpEvento,
)

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class RetornoEnvioRps:
    """Schema utilizado para RETORNO de Pedidos de Envio de RPS.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços o resultado do pedido de envio de RPS.

    :ivar Cabecalho: Cabeçalho do retorno.
    :ivar Alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar Erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    :ivar ChaveNFeRPS: Chave da NFS-e e Chave do RPS que esta substitui.
    """

    class Meta:
        name = "RetornoEnvioRPS"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["RetornoEnvioRps.Cabecalho"] = field(
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
    ChaveNFeRPS: Optional[TpChaveNfeRps] = field(
        default=None,
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
