from dataclasses import dataclass, field
from typing import Optional

from nfselib.dsf.bindings.tipos import (
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

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar NotasCanceladas: Elemento que representa a ocorrência de
        eventos de erro durante o processamento da mensagem XML.
    :ivar Alertas: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar Erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """

    class Meta:
        name = "RetornoCancelamentoNFSe"
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["RetornoCancelamentoNfse.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    NotasCanceladas: Optional[TpRetornoNotasCancelamentoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Alertas: Optional[TpListaAlertas] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Erros: Optional[TpListaErros] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar CodCidade: Informe o Codigo da Cidade.
        :ivar Sucesso: Notas Canceladas com Sucesso.
        :ivar CPFCNPJRemetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar Versao: Informe a Versão do Schema XML utilizado.
        """

        CodCidade: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
            },
        )
        Sucesso: bool = field(
            default=True,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        CPFCNPJRemetente: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            },
        )
        Versao: str = field(
            init=False,
            default="1",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )
