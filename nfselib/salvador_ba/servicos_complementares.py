from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nfselib.salvador_ba.nfse_salvador import (
    ListaMensagemRetorno,
    TcIdentificacaoNfse,
    TcIdentificacaoPrestador,
    TcIdentificacaoTomador,
)
from nfselib.salvador_ba.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"


@dataclass
class TcSituacaoAceiteNfse:
    class Meta:
        name = "tcSituacaoAceiteNfse"

    status_aceite_nfse: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusAceiteNfse",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "pattern": r"1|2|3|4|5",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 255,
        }
    )


@dataclass
class ConsultarNfsePendenteAceiteEnvio:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "total_digits": 15,
        }
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
        }
    )


@dataclass
class ConsultarSituacaoNfseEnvio:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    id_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "idNfse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ConsultarSituacaoNfseResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    id_nfse: Optional[TcIdentificacaoNfse] = field(
        default=None,
        metadata={
            "name": "idNfse",
            "type": "Element",
        }
    )
    situacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        }
    )


@dataclass
class RegistrarAceiteTomadorResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    lista_nfse: Optional["RegistrarAceiteTomadorResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        }
    )

    @dataclass
    class ListaNfse:
        situacao_registro: List[TcSituacaoAceiteNfse] = field(
            default_factory=list,
            metadata={
                "name": "SituacaoRegistro",
                "type": "Element",
                "min_occurs": 1,
            }
        )


@dataclass
class TcNfsePendenteAceite:
    class Meta:
        name = "tcNfsePendenteAceite"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        }
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        }
    )
    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class TcRegistroAceiteNfse:
    class Meta:
        name = "tcRegistroAceiteNFse"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    registro_aceite: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistroAceite",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )
    justificativa_indeferimento: Optional[str] = field(
        default=None,
        metadata={
            "name": "JustificativaIndeferimento",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "pattern": r"1|2|3",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 255,
        }
    )


@dataclass
class ConsultarNfsePendenteAceiteResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    lista_nfse: Optional["ConsultarNfsePendenteAceiteResposta.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd",
        }
    )

    @dataclass
    class ListaNfse:
        nfse_pendente_aceite: List[TcNfsePendenteAceite] = field(
            default_factory=list,
            metadata={
                "name": "NfsePendenteAceite",
                "type": "Element",
            }
        )


@dataclass
class RegistrarAceiteTomadorEnvio:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd"

    registro_aceite_nfse: Optional[TcRegistroAceiteNfse] = field(
        default=None,
        metadata={
            "name": "RegistroAceiteNFse",
            "type": "Element",
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
class TcAceiteNfse:
    class Meta:
        name = "tcAceiteNFse"

    tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        }
    )
    lista_nfse: Optional["TcAceiteNfse.ListaNfse"] = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 255,
        }
    )

    @dataclass
    class ListaNfse:
        registro_aceite_nfse: List[TcRegistroAceiteNfse] = field(
            default_factory=list,
            metadata={
                "name": "RegistroAceiteNfse",
                "type": "Element",
                "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/ServicosComplementares.xsd",
                "min_occurs": 1,
            }
        )
