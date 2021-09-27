from dataclasses import dataclass, field
from typing import Optional
from nfselib.paulistana.tipos_nfe_v01 import TpCpfcnpj
from nfselib.paulistana.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoConsultaLote:
    """Schema utilizado para PEDIDO de consultas de Lote.

    Este Schema XML é utilizado pelos prestadores de serviços
    consultarem as NFS-e geradas a partir de um lote de RPS.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar signature: Assinatura digital do contribuinte que gerou o lote
        de RPS.
    """
    class Meta:
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    cabecalho: Optional["PedidoConsultaLote.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
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
        :ivar numero_lote: Informe o número do Lote que deseja
            consultar.
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
        numero_lote: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroLote",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,12}",
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
