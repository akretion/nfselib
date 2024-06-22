from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from nfselib.betha.bindings.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class TcCondicaoPagamento:
    class Meta:
        name = "tcCondicaoPagamento"

    condicao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Condicao",
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        },
    )
    QtdParcela: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        },
    )
    Parcelas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        },
    )


@dataclass
class TcParcelas:
    class Meta:
        name = "tcParcelas"

    Parcela: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        },
    )
    DataVencimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        },
    )
    Valor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        },
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"

    ValorServicos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        },
    )
    ValorDeducoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    ValorPis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    ValorCofins: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    ValorInss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    ValorIr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    ValorCsll: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    IssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            "required": True,
        },
    )
    ValorIss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    ValorIssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    OutrasRetencoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    BaseCalculo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    Aliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    ValorLiquidoNfse: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    DescontoIncondicionado: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )
    DescontoCondicionado: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
        },
    )


@dataclass
class TcRps:
    class Meta:
        name = "tcRps"

    InfRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
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
