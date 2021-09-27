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
        }
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
        }
    )


@dataclass
class CpfouCnpj:
    cpf: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "total_digits": 11,
        }
    )
    cnpj: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "total_digits": 14,
        }
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
        }
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
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "min_length": 1,
            "max_length": 50,
            "white_space": "collapse",
        }
    )
    edificio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "min_length": 1,
            "max_length": 28,
            "white_space": "collapse",
        }
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
        }
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
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "length": 2,
        }
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "total_digits": 8,
        }
    )


@dataclass
class IssRetido:
    iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "issRetido",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "pattern": r"[1|2]{1}",
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        }
    )
    data_retencao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataRetencao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        }
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
        }
    )
    nome_razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeRazaoSocial",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    numero_nota_materiais: Optional[int] = field(
        default=None,
        metadata={
            "name": "numeroNotaMateriais",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_exclusive": 1,
            "total_digits": 9,
        }
    )
    valor_nota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorNota",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_aplicado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorAplicado",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    data_emissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEmissao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
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

    material_aplicado: List[MaterialAplicado] = field(
        default_factory=list,
        metadata={
            "name": "materialAplicado",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OutrosServicosTomados:
    data_emissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEmissao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    tipo_documento: Optional[TipoDocumentoOutrosServicosTomados] = field(
        default=None,
        metadata={
            "name": "tipoDocumento",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    numero_documento: Optional[int] = field(
        default=None,
        metadata={
            "name": "numeroDocumento",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_exclusive": 0,
            "total_digits": 9,
        }
    )
    nome_razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeRazaoSocial",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 155,
            "white_space": "collapse",
        }
    )
    cpf_cnpj: Optional[CpfouCnpj] = field(
        default=None,
        metadata={
            "name": "cpfCnpj",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    cga: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "min_length": 5,
            "max_length": 11,
            "white_space": "collapse",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "optanteSimplesNacional",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "pattern": r"[1|2]{1}",
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemListaServico",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    valor_servico: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorServico",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    iss_retido: Optional[IssRetido] = field(
        default=None,
        metadata={
            "name": "issRetido",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        }
    )


@dataclass
class SubEmpreitada:
    cpf_cnpj: Optional[CpfouCnpj] = field(
        default=None,
        metadata={
            "name": "cpfCnpj",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    nome_razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeRazaoSocial",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "optanteSimplesNacional",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "pattern": r"[1|2]{1}",
        }
    )
    numero_documento: Optional[int] = field(
        default=None,
        metadata={
            "name": "numeroDocumento",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_exclusive": 0,
            "total_digits": 9,
        }
    )
    tipo_documento: Optional[TipoDocumentoSubempreitada] = field(
        default=None,
        metadata={
            "name": "tipoDocumento",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEmissao",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    valor_documento: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorDocumento",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    iss_retido: Optional[IssRetido] = field(
        default=None,
        metadata={
            "name": "issRetido",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        }
    )
    municipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "total_digits": 7,
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "length": 2,
        }
    )


@dataclass
class ListaOutrosServicosTomados:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    outros_servicos_tomados: List[OutrosServicosTomados] = field(
        default_factory=list,
        metadata={
            "name": "outrosServicosTomados",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListaSubEmpreitada:
    class Meta:
        namespace = "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd"

    sub_empreitada: List[SubEmpreitada] = field(
        default_factory=list,
        metadata={
            "name": "subEmpreitada",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Cliente:
    nome_razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeRazaoSocial",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    cpf_cnpj: Optional[CpfouCnpj] = field(
        default=None,
        metadata={
            "name": "cpfCnpj",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    endereco: Optional[Endereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    contato: Optional[Contato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    lista_outros_servicos_tomados: Optional[ListaOutrosServicosTomados] = field(
        default=None,
        metadata={
            "name": "ListaOutrosServicosTomados",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
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
        }
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    lista_outros_servicos_tomados: Optional[ListaOutrosServicosTomados] = field(
        default=None,
        metadata={
            "name": "ListaOutrosServicosTomados",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Obra:
    nome_razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeRazaoSocial",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    data_inicio: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataInicio",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    data_termino: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataTermino",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        }
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
        }
    )
    cpf_cnpj: Optional[CpfouCnpj] = field(
        default=None,
        metadata={
            "name": "cpfCnpj",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    endereco: Optional[Endereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    contato: Optional[Contato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
            "required": True,
        }
    )
    lista_sub_empreitada: Optional[ListaSubEmpreitada] = field(
        default=None,
        metadata={
            "name": "ListaSubEmpreitada",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        }
    )
    lista_material_aplicado: Optional[ListaMaterialAplicado] = field(
        default=None,
        metadata={
            "name": "ListaMaterialAplicado",
            "type": "Element",
            "namespace": "https://nfse.sefaz.salvador.ba.gov.br/Deducoes.xsd",
        }
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
        }
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
        }
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
        }
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    lista_clientes: Optional[ListaClientes] = field(
        default=None,
        metadata={
            "name": "ListaClientes",
            "type": "Element",
            "required": True,
        }
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
        }
    )
    competencia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    lista_obras: Optional[ListaObras] = field(
        default=None,
        metadata={
            "name": "ListaObras",
            "type": "Element",
            "required": True,
        }
    )
