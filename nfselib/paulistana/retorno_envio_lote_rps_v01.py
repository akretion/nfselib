from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.paulistana.tipos_nfe_v01 import (
    TpChaveNfeRps,
    TpEvento,
    TpInformacoesLote,
)

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class RetornoEnvioLoteRps:
    """Schema utilizado para RETORNO de Pedidos de Envio de lote de RPS.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços o resultado do pedido de envio de lote de
    RPS.

    :ivar cabecalho: Cabeçalho do retorno.
    :ivar alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    :ivar chave_nfe_rps: Chave da NFS-e e Chave do RPS que esta
        substitui.
    """
    class Meta:
        name = "RetornoEnvioLoteRPS"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    cabecalho: Optional["RetornoEnvioLoteRps.Cabecalho"] = field(
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
    chave_nfe_rps: List[TpChaveNfeRps] = field(
        default_factory=list,
        metadata={
            "name": "ChaveNFeRPS",
            "type": "Element",
            "namespace": "",
            "max_occurs": 50,
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar sucesso: Campo indicativo do sucesso do pedido do serviço.
        :ivar informacoes_lote: Informações sobre o lote processado.
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
