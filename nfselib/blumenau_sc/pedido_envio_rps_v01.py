from dataclasses import dataclass, field
from typing import Optional
from nfselib.blumenau_sc.tipos_nfe_v01 import (
    TpCpfcnpj,
    TpRps,
)
from nfselib.blumenau_sc.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://nfse.blumenau.sc.gov.br"


@dataclass
class PedidoEnvioRps:
    """Schema utilizado para PEDIDO de envio de RPS.

    Este Schema XML é utilizado pelos prestadores de serviços para
    substituição online e individual de RPS por NFS-e.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar rps: Informe o RPS a ser substituido por NFS-e.
    :ivar signature: Assinatura digital do contribuinte que gerou o RPS
        contido da mensagem XML.
    """
    class Meta:
        name = "PedidoEnvioRPS"
        namespace = "http://nfse.blumenau.sc.gov.br"

    cabecalho: Optional["PedidoEnvioRps.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    rps: Optional[TpRps] = field(
        default=None,
        metadata={
            "name": "RPS",
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
