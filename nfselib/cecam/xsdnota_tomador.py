from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate


class DadosItensNotaFiscalRetido1(Enum):
    S = "S"
    N = "N"


class DadosNotaFiscalSituacaoNf1(Enum):
    C = "C"
    N = "N"


class DadosNotaFiscalUfprestador(Enum):
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
class NotaTomador:
    header: Optional["NotaTomador.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dados_nota_fiscal: List["NotaTomador.DadosNotaFiscal"] = field(
        default_factory=list,
        metadata={
            "name": "DadosNotaFiscal",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 20,
        }
    )

    @dataclass
    class Header:
        """
        :ivar cnpjcpftomador: CNPJ / CPF do Tomador da Nota Fiscal (sem
            máscara)
        :ivar chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        cnpjcpftomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJCPFTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 11,
                "max_length": 14,
            }
        )
        chave: Optional[str] = field(
            default=None,
            metadata={
                "name": "Chave",
                "type": "Element",
                "namespace": "",
                "required": True,
                "length": 48,
            }
        )

    @dataclass
    class DadosNotaFiscal:
        """
        :ivar id: Identificador do Registro
        :ivar numero_nf: Número da Nota Fiscal
        :ivar situacao_nf: Situação da Nota Fiscal C - para Nota
            Cancelada N - para Nota Normal
        :ivar emissao: Data de Emissão da Nota Fiscal
        :ivar cnpjcpfprestador: CNPJ / CPF do Prestador de Serviço (sem
            máscara)
        :ivar nome_prestador: Nome ou Razão Social do Prestador de
            Serviço
        :ivar ufprestador: Sigla do Estado do Prestador de Serviço
        :ivar cidade_prestador: Código do Município na Tabela IBGE do
            Prestador de Serviço
        :ivar endereco_prestador: Endereço do Prestador de Serviço
        :ivar numero_prestador: Número do Prestador de Serviço
        :ivar complemento_prestador: Complemento do Prestador de Serviço
        :ivar bairro_prestador: Bairro do Prestador de Serviço
        :ivar cepprestador: CEP do Prestador de Serviço
        :ivar email_prestador: E-mail do Prestador de Serviço
        :ivar observacao: Observações da Nota Fiscal
        :ivar motivo_cancelamento: Descrição do Motivo de Cancelamento
            da Nota Fiscal
        :ivar tipo_documento: Código do Tipo de Nota Fiscal (verificar
            com a Prefeitura a lista de códigos válidos)
        :ivar dados_itens_nota_fiscal:
        :ivar dados_impostos_nota_fiscal:
        """
        id: Optional[int] = field(
            default=None,
            metadata={
                "name": "ID",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        numero_nf: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroNF",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{10}",
            }
        )
        situacao_nf: Optional[DadosNotaFiscalSituacaoNf1] = field(
            default=None,
            metadata={
                "name": "SituacaoNF",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        emissao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "Emissao",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        cnpjcpfprestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJCPFPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 11,
                "max_length": 14,
            }
        )
        nome_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "NomePrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        ufprestador: Optional[DadosNotaFiscalUfprestador] = field(
            default=None,
            metadata={
                "name": "UFPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        cidade_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CidadePrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{7}",
            }
        )
        endereco_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "EnderecoPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        numero_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 10,
            }
        )
        complemento_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "ComplementoPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        bairro_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "BairroPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 40,
            }
        )
        cepprestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CEPPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{5}-[0-9]{3}",
            }
        )
        email_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "EmailPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )
        observacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "Observacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 200,
            }
        )
        motivo_cancelamento: Optional[str] = field(
            default=None,
            metadata={
                "name": "MotivoCancelamento",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 200,
            }
        )
        tipo_documento: Optional[str] = field(
            default=None,
            metadata={
                "name": "TipoDocumento",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{3}",
            }
        )
        dados_itens_nota_fiscal: Optional["NotaTomador.DadosNotaFiscal.DadosItensNotaFiscal"] = field(
            default=None,
            metadata={
                "name": "DadosItensNotaFiscal",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        dados_impostos_nota_fiscal: List["NotaTomador.DadosNotaFiscal.DadosImpostosNotaFiscal"] = field(
            default_factory=list,
            metadata={
                "name": "DadosImpostosNotaFiscal",
                "type": "Element",
                "namespace": "",
                "max_occurs": 5,
            }
        )

        @dataclass
        class DadosItensNotaFiscal:
            """
            :ivar item_atividade: Código do Item da Atividade prestado
                (Obtido no serviço ConsultaItensAtividade)
            :ivar texto_item: Texto do Item da Nota Fiscal
            :ivar valor_item: Valor do Item da Nota Fiscal
            :ivar valor_deducao: Valor das Deduções da Nota Fiscal
            :ivar retido: Identifica se o imposto do serviço foi retido
                na fonte pelo Tomador S - para Imposto Retido pelo
                Tomador N - para Imposto Não Retido pelo Tomador
            :ivar pais:
            """
            item_atividade: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ItemAtividade",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            texto_item: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TextoItem",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 10,
                    "max_length": 1800,
                }
            )
            valor_item: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "ValorItem",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            valor_deducao: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "ValorDeducao",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            retido: Optional[DadosItensNotaFiscalRetido1] = field(
                default=None,
                metadata={
                    "name": "Retido",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            pais: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Pais",
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
            :ivar imposto: Sigla do Imposto utilizado na Dedução
            :ivar valor_imposto: Valor do Imposto utilizado na Dedução
            """
            imposto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Imposto",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 3,
                    "max_length": 6,
                }
            )
            valor_imposto: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "ValorImposto",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
