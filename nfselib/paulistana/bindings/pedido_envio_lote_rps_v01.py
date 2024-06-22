from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from nfselib.paulistana.bindings.tipos_nfe_v01 import (
    TpCpfcnpj,
    TpRps,
)
from nfselib.paulistana.bindings.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class PedidoEnvioLoteRps:
    """Schema utilizado para PEDIDO de envio de lote de RPS.

    Este Schema XML é utilizado pelos prestadores de serviços para
    substituição em lote de RPS por NFS-e.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar RPS: Informe os RPS a serem substituidos por NFS-e.
    :ivar signature: Assinatura digital do contribuinte que gerou os RPS
        contidos na mensagem XML.
    """

    class Meta:
        name = "PedidoEnvioLoteRPS"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["PedidoEnvioLoteRps.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    RPS: List[TpRps] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
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
        :ivar transacao: Informe se os RPS a serem substituídos por
            NFS-e farão parte de uma mesma transação. True - Os RPS só
            serão substituídos por NFS-e se não ocorrer nenhum evento de
            erro durante o processamento de todo o lote; False - Os RPS
            válidos serão substituídos por NFS-e, mesmo que ocorram
            eventos de erro durante processamento de outros RPS deste
            lote.
        :ivar dtInicio: Informe a data de início do período transmitido
            (AAAA-MM-DD).
        :ivar dtFim: Informe a data final do período transmitido (AAAA-
            MM-DD).
        :ivar QtdRPS: Informe o total de RPS contidos na mensagem XML.
        :ivar ValorTotalServicos: Informe o valor total dos serviços
            prestados dos RPS contidos na mensagem XML.
        :ivar ValorTotalDeducoes: Informe o valor total das deduções dos
            RPS contidos na mensagem XML.
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
        transacao: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
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
        QtdRPS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,15}",
            },
        )
        ValorTotalServicos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "total_digits": 15,
                "fraction_digits": 2,
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
            },
        )
        ValorTotalDeducoes: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_inclusive": "0",
                "total_digits": 15,
                "fraction_digits": 2,
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
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
