from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import (
    TpChaveNfe,
    TpCpfcnpj,
)
from nfselib.paulistana.bindings.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoCancelamentoNfe:
    """Schema utilizado para PEDIDO de Cancelamento de NFS-e.

    Este Schema XML é utilizado pelos Prestadores de serviços cancelarem
    NFS-e emitidas por eles.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar Detalhe: Detalhe do pedido de cancelamento de NFS-e. Cada
        detalhe deverá conter a Chave de uma NFS-e e sua respectiva
        assinatura de cancelamento.
    :ivar signature: Assinatura digital do CNPJ emissor das NFS-e
    """

    class Meta:
        name = "PedidoCancelamentoNFe"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["PedidoCancelamentoNfe.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Detalhe: List["PedidoCancelamentoNfe.Detalhe"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar CPFCNPJRemetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar transacao: Informe se as NFS-e a serem canceladas farão
            parte de uma mesma transação. True - As NFS-e só serão
            canceladas se não ocorrer nenhum evento de erro durante o
            processamento de todo o lote; False - As NFS-e aptas a serem
            canceladas serão canceladas, mesmo que ocorram eventos de
            erro durante processamento do cancelamento de outras NFS-e
            deste lote.
        :ivar Versao: Informe a Versão do Schema XML utilizado.
        """

        CPFCNPJRemetente: Optional[TpCpfcnpj] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
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
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )

    @dataclass
    class Detalhe:
        """
        :ivar ChaveNFe: Chave da NFS-e a ser cancelada.
        :ivar AssinaturaCancelamento: Assinatura da NFS-e a ser
            cancelada.
        """

        ChaveNFe: Optional[TpChaveNfe] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        AssinaturaCancelamento: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "format": "base64",
            },
        )
