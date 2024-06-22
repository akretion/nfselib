from dataclasses import dataclass, field
from typing import Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import TpCpfcnpj
from nfselib.paulistana.bindings.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoCancelamentoLote:
    """Schema utilizado para PEDIDO de cancelamento de lote.

    Este Schema XML é utilizado pelos prestadores de serviços cancelarem
    as NFS-e geradas a partir de um lote de RPS.

    :ivar Cabecalho: Cabeçalho do pedido de cancelamento de lote.
    :ivar signature: Assinatura digital do CNPJ emissor dos RPS.
    """

    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["PedidoCancelamentoLote.Cabecalho"] = field(
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
        :ivar NumeroLote: Informe o número do Lote a ser cancelado.
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
        NumeroLote: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,12}",
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
