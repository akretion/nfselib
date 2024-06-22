from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from nfselib.dsf.bindings.tipos import (
    TpLote,
    TpMetodoEnvio,
)
from nfselib.dsf.bindings.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqEnvioLoteRps:
    """Schema utilizado para envio de lote de RPS.

    Este Schema XML é utilizado pelos prestadores de serviços para
    substituição em lote de RPS por NFS-e.

    :ivar Cabecalho: Cabeçalho do Lote.
    :ivar Lote: Informe os RPS a serem substituidos por NF-e.
    :ivar signature:
    """

    class Meta:
        name = "ReqEnvioLoteRPS"
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["ReqEnvioLoteRps.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Lote: Optional[TpLote] = field(
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
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar CodCidade: Informe o Codigo da Cidade no Padrão SIAFI.
        :ivar CPFCNPJRemetente: CNPJ do contribuinte ou CPF do
            Responsável Legal autorizado a entregar o lote.
        :ivar RazaoSocialRemetente: Informe o Nome do Contribuinte ou do
            Responsável Legal
        :ivar transacao: Informe se os RPS a serem substituídos por NF-e
            farão parte de uma mesma transação. True - Os RPS só serão
            substituídos por NF-e se não ocorrer nenhum evento de erro
            durante o processamento de todo o lote; False - Os RPS
            válidos serão substituídos por NF-e, mesmo que ocorram
            eventos de erro durante processamento de outros RPS deste
            lote. Por definição estão sendo aceitos apenas lotes com RPS
            válidos, o lote é recusado caso haja algum RPS inválido.
        :ivar dtInicio: Informe a data de início do período transmitido
            (AAAA-MM-DD).
        :ivar dtFim: Informe a data final do período transmitido (AAAA-
            MM-DD).
        :ivar QtdRPS: Informe o total de RPS contidos na mensagem XML.
            OBS: O xml não pode ultrapassar o tamanho maximo de 500kb.
        :ivar ValorTotalServicos: Informe o valor total dos serviços
            prestados dos RPS contidos na mensagem XML.
        :ivar ValorTotalDeducoes: Informe o valor total das deduções dos
            RPS contidos na mensagem XML.
        :ivar Versao: Informe a Versão do Schema XML utilizado.
        :ivar MetodoEnvio: Informe o Método de Envio
        :ivar VersaoComponente: Versão da DLL de envio de lote. Não é
            necessário informar esse campo caso não utilize a DLL.
        """

        CodCidade: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
            },
        )
        CPFCNPJRemetente: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            },
        )
        RazaoSocialRemetente: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "max_length": 120,
                "white_space": "preserve",
            },
        )
        transacao: bool = field(
            default=True,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
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
        QtdRPS: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 250,
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
                "required": True,
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
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )
        MetodoEnvio: Optional[TpMetodoEnvio] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        VersaoComponente: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 0,
                "max_length": 10,
                "white_space": "collapse",
            },
        )
