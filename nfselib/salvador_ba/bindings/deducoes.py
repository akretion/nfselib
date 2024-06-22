from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"


@dataclass
class Contato:
    telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 8,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 5,
            "max_length": 50,
            "white_space": "collapse",
            "pattern": r"[a-z0-9_\+-]+(\.[a-z0-9_\+-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*\.([a-z]{2,4})",
        },
    )


@dataclass
class CpfouCnpj:
    cpf: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "total_digits": 11,
        },
    )
    cnpj: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "total_digits": 14,
        },
    )


@dataclass
class Endereco:
    logradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 50,
            "white_space": "collapse",
        },
    )
    numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        },
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "min_length": 1,
            "max_length": 50,
            "white_space": "collapse",
        },
    )
    edificio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "min_length": 1,
            "max_length": 28,
            "white_space": "collapse",
        },
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    municipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 3,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "length": 2,
        },
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "total_digits": 8,
        },
    )


@dataclass
class IssRetido:
    issRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "pattern": r"[1|2]{1}",
        },
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        },
    )
    dataRetencao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        },
    )


@dataclass
class MaterialAplicado:
    cnpj: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "total_digits": 14,
        },
    )
    nomeRazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    numeroNotaMateriais: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_exclusive": 1,
            "total_digits": 9,
        },
    )
    valorNota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    valorAplicado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    dataEmissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )


class TipoDocumentoOutrosServicosTomados(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_5 = 5
    VALUE_6 = 6


class TipoDocumentoSubempreitada(Enum):
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_5 = 5
    VALUE_6 = 6


@dataclass
class ListaMaterialAplicado:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    materialAplicado: List[MaterialAplicado] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class OutrosServicosTomados:
    dataEmissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    tipoDocumento: Optional[TipoDocumentoOutrosServicosTomados] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    numeroDocumento: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_exclusive": 0,
            "total_digits": 9,
        },
    )
    nomeRazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 155,
            "white_space": "collapse",
        },
    )
    cpfCnpj: Optional[CpfouCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    cga: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "min_length": 5,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    optanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "pattern": r"[1|2]{1}",
        },
    )
    itemListaServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    valorServico: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    issRetido: Optional[IssRetido] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        },
    )


@dataclass
class SubEmpreitada:
    cpfCnpj: Optional[CpfouCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    nomeRazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    optanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "pattern": r"[1|2]{1}",
        },
    )
    numeroDocumento: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_exclusive": 0,
            "total_digits": 9,
        },
    )
    tipoDocumento: Optional[TipoDocumentoSubempreitada] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    dataEmissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    valorDocumento: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    issRetido: Optional[IssRetido] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        },
    )
    municipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "length": 2,
        },
    )


@dataclass
class ListaOutrosServicosTomados:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    outrosServicosTomados: List[OutrosServicosTomados] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ListaSubEmpreitada:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    subEmpreitada: List[SubEmpreitada] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Cliente:
    nomeRazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    cpfCnpj: Optional[CpfouCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    endereco: Optional[Endereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    contato: Optional[Contato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    listaOutrosServicosTomados: Optional[ListaOutrosServicosTomados] = field(
        default=None,
        metadata={
            "name": "ListaOutrosServicosTomados",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )


@dataclass
class DmseOutrosServicosTomados:
    class Meta:
        name = "DMSeOutrosServicosTomados"
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    declarante: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    listaOutrosServicosTomados: Optional[ListaOutrosServicosTomados] = field(
        default=None,
        metadata={
            "name": "ListaOutrosServicosTomados",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Obra:
    nomeRazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    dataInicio: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    dataTermino: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        },
    )
    nome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        },
    )
    cpfCnpj: Optional[CpfouCnpj] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    endereco: Optional[Endereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    contato: Optional[Contato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        },
    )
    listaSubEmpreitada: Optional[ListaSubEmpreitada] = field(
        default=None,
        metadata={
            "name": "ListaSubEmpreitada",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        },
    )
    listaMaterialAplicado: Optional[ListaMaterialAplicado] = field(
        default=None,
        metadata={
            "name": "ListaMaterialAplicado",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        },
    )


@dataclass
class ListaClientes:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    cliente: List[Cliente] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ListaObras:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    obra: List[Obra] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class DmseClientes:
    class Meta:
        name = "DMSeClientes"
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    declarante: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    listaClientes: Optional[ListaClientes] = field(
        default=None,
        metadata={
            "name": "ListaClientes",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DmseObras:
    class Meta:
        name = "DMSeObras"
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    declarante: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 11,
            "white_space": "collapse",
        },
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    listaObras: Optional[ListaObras] = field(
        default=None,
        metadata={
            "name": "ListaObras",
            "type": "Element",
            "required": True,
        },
    )
