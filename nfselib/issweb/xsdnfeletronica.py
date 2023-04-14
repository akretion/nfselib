from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate


class DadosItensNotaFiscalRetido(Enum):
    S = "S"
    N = "N"


class DadosNotaFiscalLocalPrestacao(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class DadosNotaFiscalUflocalPrestacao(Enum):
    VALUE = ""
    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"


class DadosNotaFiscalUftomador(Enum):
    VALUE = ""
    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"


@dataclass
class Nfeeletronica:
    class Meta:
        name = "NFEEletronica"

    Header: Optional["Nfeeletronica.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    DadosNotaFiscal: List["Nfeeletronica.DadosNotaFiscal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 20,
        }
    )

    @dataclass
    class Header:
        """
        :ivar Versao: Identifica a versão do layout - Fixo 002
        :ivar CNPJCPFPrestador: CNPJ / CPF do emissor da Nota Fiscal
            (sem máscara)
        :ivar Chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        Versao: str = field(
            init=False,
            default="002",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        CNPJCPFPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 11,
                "max_length": 14,
            }
        )
        Chave: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "length": 48,
            }
        )

    @dataclass
    class DadosNotaFiscal:
        """
        :ivar ID: Identificador do Registro (RPS)
        :ivar NumeroNF:
        :ivar SituacaoNF: Situação da Nota Fiscal N - para Nota Normal
        :ivar TipoNF: Tipo da Nota Fiscal P - para Serviço Prestado
        :ivar Emissao: Data de Emissão da Nota Fiscal (*não informar)
        :ivar CNPJCPFTomador: CNPJ / CPF do Tomador de Serviço (sem
            máscara)
        :ivar NomeTomador: Nome ou Razão Social do Tomador de Serviço
        :ivar UFTomador: Sigla do Estado do Tomador de Serviço
        :ivar CidadeTomador: Código do Município na Tabela IBGE do
            Tomador de Serviço
        :ivar EnderecoTomador: Endereço do Tomador de Serviço
        :ivar NumeroTomador: Número do Tomador de Serviço
        :ivar ComplementoTomador: Complemento do Tomador de Serviço
        :ivar BairroTomador: Bairro do Tomador de Serviço
        :ivar CEPTomador: CEP do Tomador de Serviço
        :ivar EmailTomador: E-mail do Tomador de Serviço
        :ivar Observacao: Observações da Nota Fiscal
        :ivar NFSubstituta: Informar o número da Nota Fiscal Substituta
            de uma Nota Fiscal Cancelada.
        :ivar LocalPrestacao: Local da Prestação do Serviço 1 - para
            serviço na sede do prestador 2 - para serviço para imóvel
            (Construção Civil) 3 - para serviço em via pública 4 - para
            serviço fora do município
        :ivar DescricaoLocalPrestacao: Dados do Local de Prestação do
            Serviço
        :ivar DescricaoLocalPrestacaoComplementar: Dados complementares
            do Local de Prestação do Serviço
        :ivar InscricaoImovel: Inscrição Cadastral do Imóvel (usar
            quando o Local de Prestação for do tipo 2)
        :ivar UFLocalPrestacao: Sigla do Estado da Prestação do Serviço
            (usar quando o Local de Prestação for do tipo 4)
        :ivar CidadeLocalPrestacao: Cidade da Prestação do Serviço (usar
            quando o Local de Prestação for do tipo 4)
        :ivar EnderecoLocalPrestacao: Endereço da Prestação do Serviço
            (usar quando o Local de Prestação for do tipo 3 ou 4)
        :ivar NumeroLocalPrestacao: Número da localização do imóvel da
            Prestação do Serviço (usar quando o Local de Prestação for
            do tipo 4)
        :ivar ComplementoLocalPrestacao: Complemento do imóvel da
            Prestação do Serviço (usar quando o Local de Prestação for
            do tipo 4)
        :ivar BairroLocalPrestacao: Bairro da Prestação do Serviço (usar
            quando o Local de Prestação for do tipo 4)
        :ivar CEPLocalPrestacao: CEP da Prestação do Serviço (usar
            quando o Local de Prestação for do tipo 4)
        :ivar MotivoCancelamento: Descrição do Motivo de Cancelamento da
            Nota Fiscal
        :ivar TipoDocumento: Código do Tipo de Nota Fiscal (verificar
            com a Prefeitura a lista de códigos válidos)
        :ivar DadosItensNotaFiscal:
        :ivar DadosImpostosNotaFiscal:
        """
        ID: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        NumeroNF: str = field(
            init=False,
            default="0000000000",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        SituacaoNF: str = field(
            init=False,
            default="N",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        TipoNF: str = field(
            init=False,
            default="P",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Emissao: XmlDate = field(
            init=False,
            default=XmlDate(1900, 1, 1),
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        CNPJCPFTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 11,
                "max_length": 14,
            }
        )
        NomeTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        UFTomador: Optional[DadosNotaFiscalUftomador] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        CidadeTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{7}",
            }
        )
        EnderecoTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        NumeroTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 10,
            }
        )
        ComplementoTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        BairroTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 40,
            }
        )
        CEPTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{5}-[0-9]{3}",
            }
        )
        EmailTomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )
        Observacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 200,
            }
        )
        NFSubstituta: str = field(
            init=False,
            default="0000000000",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        LocalPrestacao: Optional[DadosNotaFiscalLocalPrestacao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        DescricaoLocalPrestacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        DescricaoLocalPrestacaoComplementar: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )
        InscricaoImovel: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        UFLocalPrestacao: Optional[DadosNotaFiscalUflocalPrestacao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        CidadeLocalPrestacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{7}",
            }
        )
        EnderecoLocalPrestacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        NumeroLocalPrestacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 10,
            }
        )
        ComplementoLocalPrestacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 30,
            }
        )
        BairroLocalPrestacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 40,
            }
        )
        CEPLocalPrestacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{5}-[0-9]{3}",
            }
        )
        MotivoCancelamento: str = field(
            init=False,
            default="",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        TipoDocumento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{3}",
            }
        )
        DadosItensNotaFiscal: Optional["Nfeeletronica.DadosNotaFiscal.DadosItensNotaFiscal"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        DadosImpostosNotaFiscal: List["Nfeeletronica.DadosNotaFiscal.DadosImpostosNotaFiscal"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "max_occurs": 5,
            }
        )

        @dataclass
        class DadosItensNotaFiscal:
            """
            :ivar ItemAtividade: Código do Item da Atividade prestado
                (de acordo com lista informada pela Prefeitura)
            :ivar TextoItem: Texto do Item da Nota Fiscal
            :ivar ValorItem: Valor do Item da Nota Fiscal
            :ivar ValorDeducao: Valor das Deduções da Nota Fiscal
            :ivar Retido: Identifica se o imposto do serviço foi retido
                na fonte pelo Tomador S - para Imposto Retido pelo
                Tomador N - para Imposto Não Retido pelo Tomador
            :ivar Pais:
            """
            ItemAtividade: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            TextoItem: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 10,
                    "max_length": 1000,
                }
            )
            ValorItem: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            ValorDeducao: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            Retido: Optional[DadosItensNotaFiscalRetido] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            Pais: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 0,
                    "max_length": 50,
                }
            )

        @dataclass
        class DadosImpostosNotaFiscal:
            """
            :ivar Imposto: Sigla do Imposto utilizado na Dedução
            :ivar ValorImposto: Valor do Imposto utilizado na Dedução
            """
            Imposto: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 3,
                    "max_length": 6,
                }
            )
            ValorImposto: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
