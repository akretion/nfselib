from dataclasses import dataclass, field
from typing import Optional

from nfselib.dsf.bindings.tipos import TpLoteCancelamentoNfse
from nfselib.dsf.bindings.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqCancelamentoNfse:
    """Schema utilizado para  Cancelamento de NFSe.

    Este Schema XML é utilizado pelos Prestadores de serviços cancelarem
    NFSe emitidas por eles.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar Lote: Detalhe do pedido de cancelamento de NFSe. Cada detalhe
        deverá conter a Chave de uma NFSe e sua respectiva assinatura de
        cancelamento.
    :ivar signature:
    """

    class Meta:
        name = "ReqCancelamentoNFSe"
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["ReqCancelamentoNfse.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Lote: Optional[TpLoteCancelamentoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar CodCidade: Informe o Codigo da Cidade.
        :ivar CPFCNPJRemetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar transacao: Informe se as NF-e a serem canceladas farão
            parte de uma mesma transação. True - As NF-e só serão
            canceladas se não ocorrer nenhum evento de erro durante o
            processamento de todo o lote; False - As NF-e aptas a serem
            canceladas serão canceladas, mesmo que ocorram eventos de
            erro durante processamento do cancelamento de outras NF-e
            deste lote.
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
        CPFCNPJRemetente: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            },
        )
        transacao: bool = field(
            default=True,
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
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )
