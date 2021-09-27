from dataclasses import dataclass, field
from typing import Optional
from nfselib.dsf.tipos import TpLoteCancelamentoNfse
from nfselib.dsf.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqCancelamentoNfse:
    """Schema utilizado para  Cancelamento de NFSe.

    Este Schema XML é utilizado pelos Prestadores de serviços cancelarem
    NFSe emitidas por eles.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar lote: Detalhe do pedido de cancelamento de NFSe. Cada detalhe
        deverá conter a Chave de uma NFSe e sua respectiva assinatura de
        cancelamento.
    :ivar signature:
    """
    class Meta:
        name = "ReqCancelamentoNFSe"
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["ReqCancelamentoNfse.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    lote: Optional[TpLoteCancelamentoNfse] = field(
        default=None,
        metadata={
            "name": "Lote",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar cod_cidade: Informe o Codigo da Cidade.
        :ivar cpfcnpjremetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar transacao: Informe se as NF-e a serem canceladas farão
            parte de uma mesma transação. True - As NF-e só serão
            canceladas se não ocorrer nenhum evento de erro durante o
            processamento de todo o lote; False - As NF-e aptas a serem
            canceladas serão canceladas, mesmo que ocorram eventos de
            erro durante processamento do cancelamento de outras NF-e
            deste lote.
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
        transacao: bool = field(
            default=True,
            metadata={
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
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )
