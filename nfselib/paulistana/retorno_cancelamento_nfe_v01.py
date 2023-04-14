from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.paulistana.tipos_nfe_v01 import TpEvento

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class RetornoCancelamentoNfe:
    """Schema utilizado para RETORNO de Pedidos de cancelamento de NFS-e.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços qual o resultado do pedido de cancelamento
    de NFS-e.

    :ivar cabecalho: Cabeçalho do retorno.
    :ivar alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """
    class Meta:
        name = "RetornoCancelamentoNFe"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    cabecalho: Optional["RetornoCancelamentoNfe.Cabecalho"] = field(
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
