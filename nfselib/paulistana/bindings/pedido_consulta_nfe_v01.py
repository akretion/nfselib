from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import (
    TpChaveNfe,
    TpChaveRps,
    TpCpfcnpj,
)
from nfselib.paulistana.bindings.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoConsultaNfe:
    """Schema utilizado para PEDIDO de consultas de NFS-e.

    Este Schema XML é utilizado pelos prestadores de serviços
    consultarem NFS-e geradas por eles.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar Detalhe: Detalhe do pedido. Cada item de detalhe deverá conter
        a chave de uma NFS-e ou a chave de um RPS.
    :ivar signature: Assinatura digital do contribuinte que gerou as
        NFS-e/RPS.
    """

    class Meta:
        name = "PedidoConsultaNFe"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["PedidoConsultaNfe.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Detalhe: List["PedidoConsultaNfe.Detalhe"] = field(
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
        ChaveRPS: Optional[TpChaveRps] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        ChaveNFe: Optional[TpChaveNfe] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
