from dataclasses import dataclass, field
from typing import Optional
from nfselib.dsf.tipos import (
    TpListaAlertas,
    TpListaErros,
    TpRetornoNotasCancelamentoNfse,
)

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class RetornoCancelamentoNfse:
    """Schema utilizado para RETORNO de Pedidos de cancelamento de NFSe.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços qual o resultado do pedido de cancelamento
    de NFSe.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar notas_canceladas: Elemento que representa a ocorrência de
        eventos de erro durante o processamento da mensagem XML.
    :ivar alertas: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """
    class Meta:
        name = "RetornoCancelamentoNFSe"
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["RetornoCancelamentoNfse.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    notas_canceladas: Optional[TpRetornoNotasCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "NotasCanceladas",
            "type": "Element",
            "namespace": "",
        }
    )
    alertas: Optional[TpListaAlertas] = field(
        default=None,
        metadata={
            "name": "Alertas",
            "type": "Element",
            "namespace": "",
        }
    )
    erros: Optional[TpListaErros] = field(
        default=None,
        metadata={
            "name": "Erros",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar cod_cidade: Informe o Codigo da Cidade.
        :ivar sucesso: Notas Canceladas com Sucesso.
        :ivar cpfcnpjremetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar versao: Informe a Versão do Schema XML utilizado.
        """
        cod_cidade: Optional[int] = field(
            default=None,
            metadata={
                "name": "CodCidade",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
            }
        )
        sucesso: bool = field(
            default=True,
            metadata={
                "name": "Sucesso",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        cpfcnpjremetente: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPFCNPJRemetente",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            }
        )
        versao: str = field(
            init=False,
            default="1",
            metadata={
                "name": "Versao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )
