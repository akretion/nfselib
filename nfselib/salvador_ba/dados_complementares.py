from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.salvador_ba.nfse_salvador import (
    ListaMensagemRetorno,
    TcCpfCnpj,
    TcEndereco,
    TcIdentificacaoRps,
)
from nfselib.salvador_ba.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"


@dataclass
class TcAtividadeEducacao:
    class Meta:
        name = "tcAtividadeEducacao"

    fl_servico_conveniado: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlServicoConveniado",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
            "pattern": r"1|2",
        }
    )


@dataclass
class TcAtividadePortuaria:
    class Meta:
        name = "tcAtividadePortuaria"

    nome_razao_social_proprietario_representante: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeRazaoSocialProprietarioRepresentante",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    st_proprietario: Optional[int] = field(
        default=None,
        metadata={
            "name": "stProprietario",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        }
    )
    nome_embarcacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeEmbarcacao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    bandeira_embarcacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "BandeiraEmbarcacao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    nome_porto: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomePorto",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    data_entrada: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEntrada",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        }
    )
    data_saida: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataSaida",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        }
    )


@dataclass
class TcConstrucaoCivil:
    class Meta:
        name = "tcConstrucaoCivil"

    nome_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeObra",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        }
    )
    deducao_material: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DeducaoMaterial",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    deducao_subempreitada: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DeducaoSubempreitada",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass
class TcInfNfseComplementar:
    class Meta:
        name = "tcInfNfseComplementar"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
            "total_digits": 15,
        }
    )
    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        }
    )
    atividade_portuaria: Optional[TcAtividadePortuaria] = field(
        default=None,
        metadata={
            "name": "AtividadePortuaria",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    construcao_civil: Optional[TcConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    atividade_educacao: Optional[TcAtividadeEducacao] = field(
        default=None,
        metadata={
            "name": "AtividadeEducacao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcInfRpscomplementar:
    class Meta:
        name = "tcInfRPSComplementar"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "required": True,
        }
    )
    atividade_portuaria: Optional[TcAtividadePortuaria] = field(
        default=None,
        metadata={
            "name": "AtividadePortuaria",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    construcao_civil: Optional[TcConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    atividade_educacao: Optional[TcAtividadeEducacao] = field(
        default=None,
        metadata={
            "name": "AtividadeEducacao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class TcNfseComplementar:
    class Meta:
        name = "tcNfseComplementar"

    inf_nfse_complementar: Optional[TcInfNfseComplementar] = field(
        default=None,
        metadata={
            "name": "InfNfseComplementar",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class TcRpscomplementar:
    class Meta:
        name = "tcRPSComplementar"

    inf_rpscomplementar: Optional[TcInfRpscomplementar] = field(
        default=None,
        metadata={
            "name": "InfRPSComplementar",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class ConsultarLoteRpsComplementarResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"

    lista_nfse_complementar: Optional["ConsultarLoteRpsComplementarResposta.ListaNfseComplementar"] = field(
        default=None,
        metadata={
            "name": "ListaNfseComplementar",
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
    class ListaNfseComplementar:
        nfse_complementar: List[TcNfseComplementar] = field(
            default_factory=list,
            metadata={
                "name": "NfseComplementar",
                "type": "Element",
            }
        )


@dataclass
class ConsultarNfseComplementarResposta:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"

    lista_nfse_complementar: Optional["ConsultarNfseComplementarResposta.ListaNfseComplementar"] = field(
        default=None,
        metadata={
            "name": "ListaNfseComplementar",
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
    class ListaNfseComplementar:
        nfse_complementar: List[TcNfseComplementar] = field(
            default_factory=list,
            metadata={
                "name": "NfseComplementar",
                "type": "Element",
            }
        )


@dataclass
class ConsultarNfseRpscomplementarResposta:
    class Meta:
        name = "ConsultarNfseRPSComplementarResposta"
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"

    nfse_complementar: Optional[TcNfseComplementar] = field(
        default=None,
        metadata={
            "name": "NfseComplementar",
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
class ListaRpscomplementar:
    class Meta:
        name = "ListaRPSComplementar"

    rpscomplementar: List[TcRpscomplementar] = field(
        default_factory=list,
        metadata={
            "name": "RPSComplementar",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
            "nillable": True,
        }
    )


@dataclass
class TcDadosComplementares:
    class Meta:
        name = "tcDadosComplementares"

    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    lista_rpscomplementar: Optional[ListaRpscomplementar] = field(
        default=None,
        metadata={
            "name": "ListaRPSComplementar",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 255,
        }
    )


@dataclass
class EnvioDadosComplementares:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/OnLine/XSD/DadosComplementares.xsd"

    dados_complementares: Optional[TcDadosComplementares] = field(
        default=None,
        metadata={
            "name": "DadosComplementares",
            "type": "Element",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
