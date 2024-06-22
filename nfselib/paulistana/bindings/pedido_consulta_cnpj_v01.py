from dataclasses import dataclass, field
from typing import Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import TpCpfcnpj
from nfselib.paulistana.bindings.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoConsultaCnpj:
    """Schema utilizado para PEDIDO de consultas de CNPJ.

    Este Schema XML é utilizado pelos tomadores e/ou prestadores de
    serviços consultarem quais Inscrições Municipais (CCM) estão
    vinculadas a um determinado CNPJ e se estes CCM emitem NFS-e ou não.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar CNPJContribuinte: Informe o CNPJ do Contribuinte que se deseja
        consultar.
    :ivar signature: Assinatura digital do CNPJ tomador/prestador que
        gerou a mensagem XML.
    """

    class Meta:
        name = "PedidoConsultaCNPJ"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["PedidoConsultaCnpj.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    CNPJContribuinte: Optional[TpCpfcnpj] = field(
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
