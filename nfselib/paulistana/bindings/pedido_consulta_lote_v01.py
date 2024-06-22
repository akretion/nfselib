from dataclasses import dataclass, field
from typing import Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import TpCpfcnpj
from nfselib.paulistana.bindings.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoConsultaLote:
    """Schema utilizado para PEDIDO de consultas de Lote.

    Este Schema XML é utilizado pelos prestadores de serviços
    consultarem as NFS-e geradas a partir de um lote de RPS.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar signature: Assinatura digital do contribuinte que gerou o lote
        de RPS.
    """

    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["PedidoConsultaLote.Cabecalho"] = field(
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
        :ivar NumeroLote: Informe o número do Lote que deseja consultar.
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
