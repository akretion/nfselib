from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.blumenau_sc.tipos_nfe_v01 import (
    TpCpfcnpj,
    TpChaveNfe,
    TpChaveRps,
)
from nfselib.blumenau_sc.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://nfse.blumenau.sc.gov.br"


@dataclass
class PedidoConsultaNfe:
    """Schema utilizado para PEDIDO de consultas de NFS-e.

    Este Schema XML é utilizado pelos prestadores de serviços
    consultarem NFS-e geradas por eles.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar detalhe: Detalhe do pedido. Cada item de detalhe deverá conter
        a chave de uma NFS-e ou a chave de um RPS.
    :ivar signature: Assinatura digital do contribuinte que gerou as
        NFS-e/RPS.
    """
    class Meta:
        name = "PedidoConsultaNFe"
        namespace = "http://nfse.blumenau.sc.gov.br"

    cabecalho: Optional["PedidoConsultaNfe.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    detalhe: List["PedidoConsultaNfe.Detalhe"] = field(
        default_factory=list,
        metadata={
            "name": "Detalhe",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar cpfcnpjremetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar versao: Informe a Versão do Schema XML utilizado.
        """
        cpfcnpjremetente: Optional[TpCpfcnpj] = field(
            default=None,
            metadata={
                "name": "CPFCNPJRemetente",
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

    @dataclass
    class Detalhe:
        chave_rps: Optional[TpChaveRps] = field(
            default=None,
            metadata={
                "name": "ChaveRPS",
                "type": "Element",
                "namespace": "",
            }
        )
        chave_nfe: Optional[TpChaveNfe] = field(
            default=None,
            metadata={
                "name": "ChaveNFe",
                "type": "Element",
                "namespace": "",
            }
        )
