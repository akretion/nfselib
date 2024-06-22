from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from nfselib.paulistana.bindings.tipos_nfe_v01 import TpCpfcnpj
from nfselib.paulistana.bindings.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoConsultaNfePeriodo:
    """Schema utilizado para PEDIDO de consulta de NFS-e Emitidas ou Recebidas por
    período.

    Este Schema XML é utilizado pelos Prestadores/Tomadores de serviços
    consultarem NFS-e Emitidas ou Recebidas por eles.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar signature: Assinatura digital do tomador das NFS-e.
    """

    class Meta:
        name = "PedidoConsultaNFePeriodo"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["PedidoConsultaNfePeriodo.Cabecalho"] = field(
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
        :ivar CPFCNPJ: Para consulta de NFS-e Recebidas Informe o CNPJ
            do Tomador. Para consulta de NFS-e Emitidas Informe o CNPJ
            do Prestador.
        :ivar Inscricao: Para consulta de NFS-e Recebidas Informe a
            Inscrição Municipal do Tomador. Para consulta de NFS-e
            Emitidas Informe a Inscrição Municipal do Prestador. Neste
            caso o preenchimento deste campo se torna obrigatório.
        :ivar dtInicio: Informe a data de início do período a ser
            consultado (AAAA-MM-DD).
        :ivar dtFim: Informe a data final do período trasmitido (AAAA-
            MM-DD).
        :ivar NumeroPagina: Informe o número da página que deseja
            consultar.
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
        CPFCNPJ: Optional[TpCpfcnpj] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        Inscricao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "pattern": r"[0-9]{8,8}",
            },
        )
        dtInicio: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        dtFim: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        NumeroPagina: str = field(
            default="1",
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
