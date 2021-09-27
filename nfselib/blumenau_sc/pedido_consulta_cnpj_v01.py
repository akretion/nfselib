from dataclasses import dataclass, field
from typing import Optional
from nfselib.blumenau_sc.tipos_nfe_v01 import TpCpfcnpj
from nfselib.blumenau_sc.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://nfse.blumenau.sc.gov.br"


@dataclass
class PedidoConsultaCnpj:
    """Schema utilizado para PEDIDO de consultas de CNPJ.

    Este Schema XML é utilizado pelos tomadores e/ou prestadores de
    serviços consultarem quais Inscrições estão vinculadas a um
    determinado CNPJ e se estas Inscrições emitem NFS-e ou não.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar cnpjcontribuinte: Informe o CNPJ do Contribuinte que se deseja
        consultar.
    :ivar signature: Assinatura digital do CNPJ tomador/prestador que
        gerou a mensagem XML.
    """
    class Meta:
        name = "PedidoConsultaCNPJ"
        namespace = "http://nfse.blumenau.sc.gov.br"

    cabecalho: Optional["PedidoConsultaCnpj.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cnpjcontribuinte: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "name": "CNPJContribuinte",
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
