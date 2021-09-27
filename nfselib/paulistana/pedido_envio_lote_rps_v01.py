from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nfselib.paulistana.tipos_nfe_v01 import (
    TpCpfcnpj,
    TpRps,
)
from nfselib.paulistana.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoEnvioLoteRps:
    """Schema utilizado para PEDIDO de envio de lote de RPS.

    Este Schema XML é utilizado pelos prestadores de serviços para
    substituição em lote de RPS por NFS-e.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar rps: Informe os RPS a serem substituidos por NFS-e.
    :ivar signature: Assinatura digital do contribuinte que gerou os RPS
        contidos na mensagem XML.
    """
    class Meta:
        name = "PedidoEnvioLoteRPS"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    cabecalho: Optional["PedidoEnvioLoteRps.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    rps: List[TpRps] = field(
        default_factory=list,
        metadata={
            "name": "RPS",
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
        :ivar transacao: Informe se os RPS a serem substituídos por
            NFS-e farão parte de uma mesma transação. True - Os RPS só
            serão substituídos por NFS-e se não ocorrer nenhum evento de
            erro durante o processamento de todo o lote; False - Os RPS
            válidos serão substituídos por NFS-e, mesmo que ocorram
            eventos de erro durante processamento de outros RPS deste
            lote.
        :ivar dt_inicio: Informe a data de início do período transmitido
            (AAAA-MM-DD).
        :ivar dt_fim: Informe a data final do período transmitido (AAAA-
            MM-DD).
        :ivar qtd_rps: Informe o total de RPS contidos na mensagem XML.
        :ivar valor_total_servicos: Informe o valor total dos serviços
            prestados dos RPS contidos na mensagem XML.
        :ivar valor_total_deducoes: Informe o valor total das deduções
            dos RPS contidos na mensagem XML.
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
        transacao: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
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
        qtd_rps: Optional[str] = field(
            default=None,
            metadata={
                "name": "QtdRPS",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,15}",
            }
        )
        valor_total_servicos: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValorTotalServicos",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "total_digits": 15,
                "fraction_digits": 2,
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
            }
        )
        valor_total_deducoes: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValorTotalDeducoes",
                "type": "Element",
                "namespace": "",
                "min_inclusive": "0",
                "total_digits": 15,
                "fraction_digits": 2,
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
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
