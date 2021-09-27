from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nfselib.blumenau_sc.tipos_nfe_v01 import TpCpfcnpj
from nfselib.blumenau_sc.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://nfse.blumenau.sc.gov.br"


@dataclass
class PedidoConsultaNfePeriodo:
    """Schema utilizado para PEDIDO de consulta de NFS-e Emitidas ou Recebidas
    por período.

    Este Schema XML é utilizado pelos Prestadores/Tomadores de serviços
    consultarem NFS-e Emitidas ou Recebidas por eles.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar signature: Assinatura digital do tomador das NFS-e.
    """
    class Meta:
        name = "PedidoConsultaNFePeriodo"
        namespace = "http://nfse.blumenau.sc.gov.br"

    cabecalho: Optional["PedidoConsultaNfePeriodo.Cabecalho"] = field(
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
        :ivar cpfcnpj: Para consulta de NFS-e Recebidas Informe o CNPJ
            do Tomador. Para consulta de NFS-e Emitidas Informe o CNPJ
            do Prestador.
        :ivar inscricao: Para consulta de NFS-e Recebidas Informe a
            Inscrição Municipal do Tomador. Para consulta de NFS-e
            Emitidas Informe a Inscrição Municipal do Prestador. Neste
            caso o preenchimento deste campo se torna obrigatório.
        :ivar dt_inicio: Informe a data de início do período a ser
            consultado (AAAA-MM-DD).
        :ivar dt_fim: Informe a data final do período trasmitido (AAAA-
            MM-DD).
        :ivar numero_pagina: Informe o número da página que deseja
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
        cpfcnpj: Optional[TpCpfcnpj] = field(
            default=None,
            metadata={
                "name": "CPFCNPJ",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        inscricao: Optional[str] = field(
            default=None,
            metadata={
                "name": "Inscricao",
                "type": "Element",
                "namespace": "",
                "pattern": r"[0-9]{1,15}",
            }
        )
        dt_inicio: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dtInicio",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        dt_fim: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dtFim",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        numero_pagina: str = field(
            default="1",
            metadata={
                "name": "NumeroPagina",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,13}",
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
