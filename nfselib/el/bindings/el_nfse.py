from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.el.com.br/nfse/xsd/el-nfse.xsd"


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"

    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        },
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"

    LogradouroTipo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    Logradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 130,
            "white_space": "collapse",
        },
    )
    LogradouroNumero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )
    LogradouroComplemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 70,
            "white_space": "collapse",
        },
    )
    CodigoMunicipio: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 7,
        },
    )
    Municipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        },
    )
    Uf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "length": 2,
        },
    )
    Cep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "total_digits": 10,
        },
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"

    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "collapse",
        },
    )
    CpfCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        },
    )
    IndicacaoCpfCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|9",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"

    CpfCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        },
    )
    IndicacaoCpfCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|9",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"

    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 11,
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 0,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    Tipo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3",
        },
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"

    CpfCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 14,
            "white_space": "collapse",
        },
    )
    IndicacaoCpfCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|9",
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TcRpsSubstituido:
    class Meta:
        name = "tcRpsSubstituido"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 13,
            "max_length": 32,
        },
    )


@dataclass
class TcServico:
    class Meta:
        name = "tcServico"

    CodigoCnae: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "max_length": 10,
        },
    )
    CodigoServico116: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        },
    )
    CodigoServicoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    Quantidade: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0.01"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    Unidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "max_length": 20,
        },
    )
    Descricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        },
    )
    ValorServico: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorIssqn: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorDesconto: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    NumeroAlvara: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"

    ValorServicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorDeducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorPis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorInss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorIr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorCsll: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorOutrasRetencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorLiquidoNfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    ValorIssRetido: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )
    OutrosDescontos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        },
    )


@dataclass
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"

    IdentificacaoPrestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "collapse",
        },
    )
    NomeFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        },
    )
    IncentivadorCultural: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    OptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    NaturezaOperacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 2,
        },
    )
    RegimeEspecialTributacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 2,
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    IdentificacaoTomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    RazaoSocial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "collapse",
        },
    )
    NomeFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 100,
            "white_space": "collapse",
        },
    )
    Endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    Contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )


@dataclass
class TcServicos:
    class Meta:
        name = "tcServicos"

    Servico: List[TcServico] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_occurs": 1,
            "max_occurs": 50,
        },
    )


@dataclass
class TcRps:
    class Meta:
        name = "tcRps"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 13,
            "max_length": 32,
        },
    )
    LocalPrestacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    IssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2",
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    IdentificacaoRps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    DadosPrestador: Optional[TcDadosPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    DadosTomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    IdentificacaoIntermediario: Optional[
        TcIdentificacaoIntermediarioServico
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
        },
    )
    Servicos: Optional[TcServicos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    Valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    RpsSubstituido: Optional[TcRpsSubstituido] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
        },
    )
    Observacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_length": 1,
            "max_length": 1000,
            "white_space": "collapse",
        },
    )
    Status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "pattern": r"1|2|3|4",
        },
    )
    CodigoMunicipioPrestacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "total_digits": 7,
        },
    )


@dataclass
class TcListaRps:
    class Meta:
        name = "tcListaRps"

    Rps: List[TcRps] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )


@dataclass
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "min_length": 13,
            "max_length": 32,
        },
    )
    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 11,
        },
    )
    QuantidadeRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
            "total_digits": 5,
        },
    )
    IdentificacaoPrestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )
    ListaRps: Optional[TcListaRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.el.com.br/nfse/xsd/el-nfse.xsd",
            "required": True,
        },
    )


@dataclass
class LoteRps(TcLoteRps):
    class Meta:
        namespace = "http://www.el.com.br/nfse/xsd/el-nfse.xsd"
