from dataclasses import dataclass, field
from typing import Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import (
    TpCpfcnpj,
    TpRps,
)
from nfselib.paulistana.bindings.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoEnvioRps:
    """Schema utilizado para PEDIDO de envio de RPS.

    Este Schema XML é utilizado pelos prestadores de serviços para
    substituição online e individual de RPS por NFS-e.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar RPS: Informe o RPS a ser substituido por NFS-e.
    :ivar signature: Assinatura digital do contribuinte que gerou o RPS
        contido da mensagem XML.
    """

    class Meta:
        name = "PedidoEnvioRPS"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["PedidoEnvioRps.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    RPS: Optional[TpRps] = field(
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
