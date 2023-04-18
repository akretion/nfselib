from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.bindings.d2ti.retorno_recepcao_nfse_v1_00 import (
    Autenticacao,
    NumeroNota,
)
from nfselib.bindings.d2ti.tipos_basicos_cta_v1_00 import (
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

    codigoImposto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    descricaoImposto: Optional[str] = field(
        default=None,
        metadata={
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
    valorImposto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    nItem: Optional[str] = field(
        default=None,
        metadata={
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

    valotTotalNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valorTotalServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valorTotalDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valorTotalISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valorReducaoBC: Optional[str] = field(
        default=None,
        metadata={
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
    codigoMunipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )
    descricaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    codigoEstado: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    descricaoEstado: Optional[str] = field(
        default=None,
        metadata={
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
    valorUnitario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valorTotal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    nItem: Optional[str] = field(
        default=None,
        metadata={
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

    tipoPessoa: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
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
    numeroNota: Optional[NumeroNota] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    codigoTipo: Optional[TtipoItemDeducao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    descricaoTipo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tipoValor: Optional[TtipoValorDeducao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    valorNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valorDecucao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    nItem: Optional[str] = field(
        default=None,
        metadata={
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

    codigoEstado: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    descricaoEstado: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    codigoMunipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )
    descricaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
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

    codigoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{4,5}",
        }
    )
    descricaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    codigoAtividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{9}",
        }
    )
    descricaoAtividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    localPrestacao: Optional[LocalPrestacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tipoTributacao: Optional[TtipoTributacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tipoRecolhimento: Optional[TtipoRecolhimento] = field(
        default=None,
        metadata={
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

    tipoPessoa: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
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
    inscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,11}",
        }
    )
    razaoSocial: Optional[str] = field(
        default=None,
        metadata={
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
    telefoneDdd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )
    telefoneNumero: Optional[str] = field(
        default=None,
        metadata={
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

    itemMapa: List[ItemMapa] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Prestador:
    class Meta:
        name = "prestador"
        namespace = "http://www.ctaconsult.com/nfse"

    tipoPessoa: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
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
    inscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,11}",
        }
    )
    razaoSocial: Optional[str] = field(
        default=None,
        metadata={
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
    telefoneDdd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )
    telefoneNumero: Optional[str] = field(
        default=None,
        metadata={
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

    tomadorIdentificado: Optional[Tboolean] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tipoPessoa: Optional[TtipoPessoa] = field(
        default=None,
        metadata={
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
    inscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,11}",
        }
    )
    razaoSocial: Optional[str] = field(
        default=None,
        metadata={
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
    telefoneDdd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 2,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )
    telefoneNumero: Optional[str] = field(
        default=None,
        metadata={
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

    descricaoNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    itensServico: Optional[ItensServico] = field(
        default=None,
        metadata={
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
    impostosFederais: Optional[ImpostosFederais] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class NfseLote:
    class Meta:
        name = "nfseLote"
        namespace = "http://www.ctaconsult.com/nfse"

    codigoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )
    dtEmissao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",
        }
    )
    notaIntermediada: Optional[Tboolean] = field(
        default=None,
        metadata={
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
    atividadeExecutada: Optional[AtividadeExecutada] = field(
        default=None,
        metadata={
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
    detalhamentoNota: Optional[DetalhamentoNota] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
