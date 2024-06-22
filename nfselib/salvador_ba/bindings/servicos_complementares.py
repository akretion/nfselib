from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from nfselib.salvador_ba.bindings.nfse_salvador import (
    ListaMensagemRetorno,
    TcIdentificacaoNfse,
    TcIdentificacaoPrestador,
    TcIdentificacaoTomador,
)
from nfselib.salvador_ba.bindings.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"


@dataclass
class TcSituacaoAceiteNfse:
    class Meta:
        name = "tcSituacaoAceiteNfse"

    StatusAceiteNfse: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 255,
        },
    )


@dataclass
class ConsultarNfsePendenteAceiteEnvio:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    Tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    NumeroNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    Competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultarSituacaoNfseEnvio:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    idNfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsultarSituacaoNfseResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    idNfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    situacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )


@dataclass
class RegistrarAceiteTomadorResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    ListaNfse: Optional["RegistrarAceiteTomadorResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )

    @dataclass
    class ListaNfse:
        SituacaoRegistro: List[TcSituacaoAceiteNfse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )


@dataclass
class TcNfsePendenteAceite:
    class Meta:
        name = "tcNfsePendenteAceite"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        },
    )
    NumeroNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        },
    )
    Competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        },
    )
    ValorServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )


@dataclass
class TcRegistroAceiteNfse:
    class Meta:
        name = "tcRegistroAceiteNFse"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        },
    )
    NumeroNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    RegistroAceite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    JustificativaIndeferimento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "pattern": r"1|2|3",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 255,
        },
    )


@dataclass
class ConsultarNfsePendenteAceiteResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    ListaNfse: Optional["ConsultarNfsePendenteAceiteResposta.ListaNfse"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        },
    )

    @dataclass
    class ListaNfse:
        NfsePendenteAceite: List[TcNfsePendenteAceite] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class RegistrarAceiteTomadorEnvio:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    RegistroAceiteNFse: Optional[TcRegistroAceiteNfse] = field(
        default=None,
        metadata={
            "type": "Element",
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
class TcAceiteNfse:
    class Meta:
        name = "tcAceiteNFse"

    Tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        },
    )
    ListaNfse: Optional["TcAceiteNfse.ListaNfse"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 255,
        },
    )

    @dataclass
    class ListaNfse:
        RegistroAceiteNfse: List[TcRegistroAceiteNfse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
                "min_occurs": 1,
            },
        )
