from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nfselib.cecam.xsdisseletronico_arquivo import (
    DadosItensNotaFiscalRetido,
    DadosNotaFiscalSituacaoNf,
)


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
    Header: Optional["NotaTomador.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    DadosNotaFiscal: List["NotaTomador.DadosNotaFiscal"] = field(
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
        :ivar CNPJCPFTomador: CNPJ / CPF do Tomador da Nota Fiscal (sem
            máscara)
        :ivar Chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
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
        :ivar ID: Identificador do Registro
        :ivar NumeroNF: Número da Nota Fiscal
        :ivar SituacaoNF: Situação da Nota Fiscal C - para Nota
            Cancelada N - para Nota Normal
        :ivar Emissao: Data de Emissão da Nota Fiscal
        :ivar CNPJCPFPrestador: CNPJ / CPF do Prestador de Serviço (sem
            máscara)
        :ivar NomePrestador: Nome ou Razão Social do Prestador de
            Serviço
        :ivar UFPrestador: Sigla do Estado do Prestador de Serviço
        :ivar CidadePrestador: Código do Município na Tabela IBGE do
            Prestador de Serviço
        :ivar EnderecoPrestador: Endereço do Prestador de Serviço
        :ivar NumeroPrestador: Número do Prestador de Serviço
        :ivar ComplementoPrestador: Complemento do Prestador de Serviço
        :ivar BairroPrestador: Bairro do Prestador de Serviço
        :ivar CEPPrestador: CEP do Prestador de Serviço
        :ivar EmailPrestador: E-mail do Prestador de Serviço
        :ivar Observacao: Observações da Nota Fiscal
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
        NumeroNF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{10}",
            }
        )
        SituacaoNF: Optional[DadosNotaFiscalSituacaoNf] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Emissao: Optional[XmlDate] = field(
            default=None,
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
        NomePrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        UFPrestador: Optional[DadosNotaFiscalUfprestador] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        CidadePrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{7}",
            }
        )
        EnderecoPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        NumeroPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 10,
            }
        )
        ComplementoPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        BairroPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 40,
            }
        )
        CEPPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{5}-[0-9]{3}",
            }
        )
        EmailPrestador: Optional[str] = field(
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
        MotivoCancelamento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 200,
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
        DadosItensNotaFiscal: Optional["NotaTomador.DadosNotaFiscal.DadosItensNotaFiscal"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        DadosImpostosNotaFiscal: List["NotaTomador.DadosNotaFiscal.DadosImpostosNotaFiscal"] = field(
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
                (Obtido no serviço ConsultaItensAtividade)
            :ivar TextoItem: Texto do Item da Nota Fiscal
            :ivar ValorItem: Valor do Item da Nota Fiscal
            :ivar ValorDeducao: Valor das Deduções da Nota Fiscal
            :ivar Retido: Identifica se o imposto do serviço foi retido
                na fonte pelo Tomador S - para Imposto Retido pelo
                Tomador N - para Imposto Não Retido pelo Tomador
            :ivar Pais:
            """
            ItemAtividade: Optional[str] = field(
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
                    "max_length": 1800,
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
