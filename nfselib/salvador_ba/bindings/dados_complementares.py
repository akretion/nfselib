from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from nfselib.salvador_ba.bindings.nfse_salvador import (
    ListaMensagemRetorno,
    TcCpfCnpj,
    TcEndereco,
    TcIdentificacaoRps,
)
from nfselib.salvador_ba.bindings.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = (
    "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"
)


@dataclass
class TcAtividadeEducacao:
    class Meta:
        name = "tcAtividadeEducacao"

    FlServicoConveniado: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )


@dataclass
class TcAtividadePortuaria:
    class Meta:
        name = "tcAtividadePortuaria"

    NomeRazaoSocialProprietarioRepresentante: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    CpfCnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    stProprietario: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        },
    )
    NomeEmbarcacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    BandeiraEmbarcacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    NomePorto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    DataEntrada: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        },
    )
    DataSaida: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        },
    )


@dataclass
class TcConstrucaoCivil:
    class Meta:
        name = "tcConstrucaoCivil"

    NomeObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        },
    )
    DeducaoMaterial: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    DeducaoSubempreitada: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )


@dataclass
class TcInfNfseComplementar:
    class Meta:
        name = "tcInfNfseComplementar"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
            "total_digits": 15,
        },
    )
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        },
    )
    AtividadePortuaria: Optional[TcAtividadePortuaria] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    ConstrucaoCivil: Optional[TcConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    AtividadeEducacao: Optional[TcAtividadeEducacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcInfRpscomplementar:
    class Meta:
        name = "tcInfRPSComplementar"

    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        },
    )
    AtividadePortuaria: Optional[TcAtividadePortuaria] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    ConstrucaoCivil: Optional[TcConstrucaoCivil] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    AtividadeEducacao: Optional[TcAtividadeEducacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class TcNfseComplementar:
    class Meta:
        name = "tcNfseComplementar"

    InfNfseComplementar: Optional[TcInfNfseComplementar] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
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
class TcRpscomplementar:
    class Meta:
        name = "tcRPSComplementar"

    InfRPSComplementar: Optional[TcInfRpscomplementar] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
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
class ConsultarLoteRpsComplementarResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"

    ListaNfseComplementar: Optional[
        "ConsultarLoteRpsComplementarResposta.ListaNfseComplementar"
    ] = field(
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
    class ListaNfseComplementar:
        NfseComplementar: List[TcNfseComplementar] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class ConsultarNfseComplementarResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"

    ListaNfseComplementar: Optional[
        "ConsultarNfseComplementarResposta.ListaNfseComplementar"
    ] = field(
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
    class ListaNfseComplementar:
        NfseComplementar: List[TcNfseComplementar] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )


@dataclass
class ConsultarNfseRpscomplementarResposta:
    class Meta:
        name = "ConsultarNfseRPSComplementarResposta"
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"

    NfseComplementar: Optional[TcNfseComplementar] = field(
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
class ListaRpscomplementar:
    class Meta:
        name = "ListaRPSComplementar"

    RPSComplementar: List[TcRpscomplementar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "nillable": True,
        },
    )


@dataclass
class TcDadosComplementares:
    class Meta:
        name = "tcDadosComplementares"

    NumeroLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    ListaRPSComplementar: Optional[ListaRpscomplementar] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        },
    )


@dataclass
class EnvioDadosComplementares:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"

    DadosComplementares: Optional[TcDadosComplementares] = field(
        default=None,
        metadata={
            "type": "Element",
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
