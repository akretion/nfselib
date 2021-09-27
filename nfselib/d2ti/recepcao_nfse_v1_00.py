from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.d2ti.retorno_cancelamento_nfse_v1_00 import Autenticacao
from nfselib.d2ti.tipos_basicos_cta_v1_00 import (
    Tboolean,
    TtipoDeducao,
    TtipoItemDeducao,
    TtipoPessoa,
    TtipoRecolhimento,
    TtipoTributacao,
    TtipoValorDeducao,
    Tuf,
)

__NAMESPACE__ = "http://www.ctaconsult.com/nfse"


@dataclass
class Aliquota:
    class Meta:
        name = "aliquota"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{1,4}|[0-9]{1}[0-9]{0,1}(\.[0-9]{1,4})?",
        }
    )


@dataclass
class Apelido:
    class Meta:
        name = "apelido"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Bairro:
    class Meta:
        name = "bairro"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Cep:
    class Meta:
        name = "cep"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]{8,8}",
        }
    )


@dataclass
class Cnpj:
    class Meta:
        name = "cnpj"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )


@dataclass
class CodigoAtividade:
    class Meta:
        name = "codigoAtividade"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]{9}",
        }
    )


@dataclass
class CodigoImposto:
    class Meta:
        name = "codigoImposto"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )


@dataclass
class CodigoMunipio:
    class Meta:
        name = "codigoMunipio"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )


@dataclass
class CodigoServico:
    class Meta:
        name = "codigoServico"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]{4,5}",
        }
    )


@dataclass
class Complemento:
    class Meta:
        name = "complemento"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Cpf:
    class Meta:
        name = "cpf"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )


@dataclass
class DescricaoAtividade:
    class Meta:
        name = "descricaoAtividade"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DescricaoEstado:
    class Meta:
        name = "descricaoEstado"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DescricaoImposto:
    class Meta:
        name = "descricaoImposto"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DescricaoMunicipio:
    class Meta:
        name = "descricaoMunicipio"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DescricaoNota:
    class Meta:
        name = "descricaoNota"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DescricaoServico:
    class Meta:
        name = "descricaoServico"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DescricaoTipo:
    class Meta:
        name = "descricaoTipo"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DtEmissao:
    class Meta:
        name = "dtEmissao"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",
        }
    )


@dataclass
class Email:
    class Meta:
        name = "email"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Imposto:
    class Meta:
        name = "imposto"
        namespace = "http://www.ctaconsult.com/nfse"

    codigo_imposto: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoImposto",
            "type": "Element",
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    descricao_imposto: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoImposto",
            "type": "Element",
            "required": True,
        }
    )
    aliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{1,4}|[0-9]{1}[0-9]{0,1}(\.[0-9]{1,4})?",
        }
    )
    valor_imposto: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorImposto",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    n_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "nItem",
            "type": "Attribute",
            "required": True,
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )


@dataclass
class InscricaoMunicipal:
    class Meta:
        name = "inscricaoMunicipal"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,11}",
        }
    )


@dataclass
class Logradouro:
    class Meta:
        name = "logradouro"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Percentual:
    class Meta:
        name = "percentual"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{1,4}|[0-9]{1}[0-9]{0,1}(\.[0-9]{1,4})?",
        }
    )


@dataclass
class Quantidade:
    class Meta:
        name = "quantidade"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )


@dataclass
class RazaoSocial:
    class Meta:
        name = "razaoSocial"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class TelefoneDdd:
    class Meta:
        name = "telefoneDdd"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )


@dataclass
class TelefoneNumero:
    class Meta:
        name = "telefoneNumero"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,9}",
        }
    )


@dataclass
class Totais:
    class Meta:
        name = "totais"
        namespace = "http://www.ctaconsult.com/nfse"

    valot_total_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "valotTotalNota",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_total_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorTotalServico",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_total_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorTotalDeducao",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_total_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorTotalISS",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_reducao_bc: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorReducaoBC",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class Valor:
    class Meta:
        name = "valor"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorDecucao:
    class Meta:
        name = "valorDecucao"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorImposto:
    class Meta:
        name = "valorImposto"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorNota:
    class Meta:
        name = "valorNota"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorReducaoBc:
    class Meta:
        name = "valorReducaoBC"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorTotal:
    class Meta:
        name = "valorTotal"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorTotalDeducao:
    class Meta:
        name = "valorTotalDeducao"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorTotalIss:
    class Meta:
        name = "valorTotalISS"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorTotalServico:
    class Meta:
        name = "valorTotalServico"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValorUnitario:
    class Meta:
        name = "valorUnitario"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class ValotTotalNota:
    class Meta:
        name = "valotTotalNota"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class CodigoEstado:
    class Meta:
        name = "codigoEstado"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[Tuf] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CodigoTipo:
    class Meta:
        name = "codigoTipo"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[TtipoItemDeducao] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Endereco:
    class Meta:
        name = "endereco"
        namespace = "http://www.ctaconsult.com/nfse"

    logradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{8,8}",
        }
    )
    codigo_munipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoMunipio",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )
    descricao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoMunicipio",
            "type": "Element",
            "required": True,
        }
    )
    codigo_estado: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "codigoEstado",
            "type": "Element",
            "required": True,
        }
    )
    descricao_estado: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoEstado",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Exterior:
    class Meta:
        name = "exterior"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[Tboolean] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ImpostosFederais:
    class Meta:
        name = "impostosFederais"
        namespace = "http://www.ctaconsult.com/nfse"

    imposto: List[Imposto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Item:
    class Meta:
        name = "item"
        namespace = "http://www.ctaconsult.com/nfse"

    tributavel: Optional[Tboolean] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    descricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    quantidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    valor_unitario: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorUnitario",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_total: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorTotal",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    n_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "nItem",
            "type": "Attribute",
            "required": True,
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )


@dataclass
class ItemMapa:
    class Meta:
        name = "itemMapa"
        namespace = "http://www.ctaconsult.com/nfse"

    tipo_pessoa: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
            "name": "tipoPessoa",
            "type": "Element",
            "required": True,
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    numero_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroNota",
            "type": "Element",
            "required": True,
        }
    )
    codigo_tipo: Optional[TtipoItemDeducao] = field(
        default=None,
        metadata={
            "name": "codigoTipo",
            "type": "Element",
            "required": True,
        }
    )
    descricao_tipo: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoTipo",
            "type": "Element",
            "required": True,
        }
    )
    tipo_valor: Optional[TtipoValorDeducao] = field(
        default=None,
        metadata={
            "name": "tipoValor",
            "type": "Element",
            "required": True,
        }
    )
    valor_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorNota",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_decucao: Optional[str] = field(
        default=None,
        metadata={
            "name": "valorDecucao",
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    n_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "nItem",
            "type": "Attribute",
            "required": True,
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )


@dataclass
class LocalPrestacao:
    class Meta:
        name = "localPrestacao"
        namespace = "http://www.ctaconsult.com/nfse"

    codigo_estado: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "codigoEstado",
            "type": "Element",
            "required": True,
        }
    )
    descricao_estado: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoEstado",
            "type": "Element",
            "required": True,
        }
    )
    codigo_munipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoMunipio",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )
    descricao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoMunicipio",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class NotaIntermediada:
    class Meta:
        name = "notaIntermediada"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[Tboolean] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Tipo:
    class Meta:
        name = "tipo"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[TtipoDeducao] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TipoPessoa:
    class Meta:
        name = "tipoPessoa"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TipoRecolhimento:
    class Meta:
        name = "tipoRecolhimento"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[TtipoRecolhimento] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TipoTributacao:
    class Meta:
        name = "tipoTributacao"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[TtipoTributacao] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TipoValor:
    class Meta:
        name = "tipoValor"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[TtipoValorDeducao] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TomadorIdentificado:
    class Meta:
        name = "tomadorIdentificado"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[Tboolean] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Tributavel:
    class Meta:
        name = "tributavel"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[Tboolean] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AtividadeExecutada:
    class Meta:
        name = "atividadeExecutada"
        namespace = "http://www.ctaconsult.com/nfse"

    codigo_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoServico",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{4,5}",
        }
    )
    descricao_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoServico",
            "type": "Element",
            "required": True,
        }
    )
    codigo_atividade: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoAtividade",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{9}",
        }
    )
    descricao_atividade: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoAtividade",
            "type": "Element",
            "required": True,
        }
    )
    local_prestacao: Optional[LocalPrestacao] = field(
        default=None,
        metadata={
            "name": "localPrestacao",
            "type": "Element",
            "required": True,
        }
    )
    tipo_tributacao: Optional[TtipoTributacao] = field(
        default=None,
        metadata={
            "name": "tipoTributacao",
            "type": "Element",
            "required": True,
        }
    )
    tipo_recolhimento: Optional[TtipoRecolhimento] = field(
        default=None,
        metadata={
            "name": "tipoRecolhimento",
            "type": "Element",
            "required": True,
        }
    )
    aliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{1,4}|[0-9]{1}[0-9]{0,1}(\.[0-9]{1,4})?",
        }
    )


@dataclass
class Intermediador:
    class Meta:
        name = "intermediador"
        namespace = "http://www.ctaconsult.com/nfse"

    tipo_pessoa: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
            "name": "tipoPessoa",
            "type": "Element",
            "required": True,
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "inscricaoMunicipal",
            "type": "Element",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,11}",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "razaoSocial",
            "type": "Element",
            "required": True,
        }
    )
    endereco: Optional[Endereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    telefone_ddd: Optional[str] = field(
        default=None,
        metadata={
            "name": "telefoneDdd",
            "type": "Element",
            "required": True,
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )
    telefone_numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "telefoneNumero",
            "type": "Element",
            "required": True,
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,9}",
        }
    )


@dataclass
class ItensServico:
    class Meta:
        name = "itensServico"
        namespace = "http://www.ctaconsult.com/nfse"

    item: List[Item] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Mapa:
    class Meta:
        name = "mapa"
        namespace = "http://www.ctaconsult.com/nfse"

    item_mapa: List[ItemMapa] = field(
        default_factory=list,
        metadata={
            "name": "itemMapa",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Prestador:
    class Meta:
        name = "prestador"
        namespace = "http://www.ctaconsult.com/nfse"

    tipo_pessoa: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
            "name": "tipoPessoa",
            "type": "Element",
            "required": True,
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "inscricaoMunicipal",
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,11}",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "razaoSocial",
            "type": "Element",
            "required": True,
        }
    )
    endereco: Optional[Endereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    telefone_ddd: Optional[str] = field(
        default=None,
        metadata={
            "name": "telefoneDdd",
            "type": "Element",
            "required": True,
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )
    telefone_numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "telefoneNumero",
            "type": "Element",
            "required": True,
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,9}",
        }
    )


@dataclass
class Tomador:
    class Meta:
        name = "tomador"
        namespace = "http://www.ctaconsult.com/nfse"

    tomador_identificado: Optional[Tboolean] = field(
        default=None,
        metadata={
            "name": "tomadorIdentificado",
            "type": "Element",
            "required": True,
        }
    )
    tipo_pessoa: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
            "name": "tipoPessoa",
            "type": "Element",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "inscricaoMunicipal",
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,11}",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "razaoSocial",
            "type": "Element",
        }
    )
    exterior: Optional[Tboolean] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    endereco: Optional[Endereco] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    telefone_ddd: Optional[str] = field(
        default=None,
        metadata={
            "name": "telefoneDdd",
            "type": "Element",
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )
    telefone_numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "telefoneNumero",
            "type": "Element",
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,9}",
        }
    )
    apelido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Deducoes:
    class Meta:
        name = "deducoes"
        namespace = "http://www.ctaconsult.com/nfse"

    tipo: Optional[TtipoDeducao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    mapa: Optional[Mapa] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    percentual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{1,4}|[0-9]{1}[0-9]{0,1}(\.[0-9]{1,4})?",
        }
    )
    valor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class DetalhamentoNota:
    class Meta:
        name = "detalhamentoNota"
        namespace = "http://www.ctaconsult.com/nfse"

    descricao_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoNota",
            "type": "Element",
            "required": True,
        }
    )
    itens_servico: Optional[ItensServico] = field(
        default=None,
        metadata={
            "name": "itensServico",
            "type": "Element",
            "required": True,
        }
    )
    totais: Optional[Totais] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    impostos_federais: Optional[ImpostosFederais] = field(
        default=None,
        metadata={
            "name": "impostosFederais",
            "type": "Element",
        }
    )


@dataclass
class NfseLote:
    class Meta:
        name = "nfseLote"
        namespace = "http://www.ctaconsult.com/nfse"

    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoMunicipio",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )
    dt_emissao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dtEmissao",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",
        }
    )
    nota_intermediada: Optional[Tboolean] = field(
        default=None,
        metadata={
            "name": "notaIntermediada",
            "type": "Element",
            "required": True,
        }
    )
    autenticacao: Optional[Autenticacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    prestador: Optional[Prestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tomador: Optional[Tomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    intermediador: Optional[Intermediador] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    atividade_executada: Optional[AtividadeExecutada] = field(
        default=None,
        metadata={
            "name": "atividadeExecutada",
            "type": "Element",
            "required": True,
        }
    )
    deducoes: Optional[Deducoes] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    detalhamento_nota: Optional[DetalhamentoNota] = field(
        default=None,
        metadata={
            "name": "detalhamentoNota",
            "type": "Element",
            "required": True,
        }
    )
