from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nfselib.cecam.xsdnfeletronica import (
    DadosNotaFiscalLocalPrestacao1,
    DadosNotaFiscalUflocalPrestacao1,
    DadosNotaFiscalUftomador1,
)
from nfselib.cecam.xsdnota_tomador import (
    DadosItensNotaFiscalRetido1,
    DadosNotaFiscalSituacaoNf1,
)


class DadosItensNotaFiscalRetido3(Enum):
    S = "S"
    N = "N"


class DadosNotaFiscalLocalPrestacao2(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class DadosNotaFiscalSituacaoNf2(Enum):
    C = "C"
    N = "N"


class DadosNotaFiscalTipoNf(Enum):
    P = "P"
    T = "T"


class DadosNotaFiscalUflocalPrestacao2(Enum):
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


class DadosNotaFiscalUftomador2(Enum):
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
class Isseletronico:
    class Meta:
        name = "ISSEletronico"

    header: Optional["Isseletronico.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dados_nota_fiscal: List["Isseletronico.DadosNotaFiscal"] = field(
        default_factory=list,
        metadata={
            "name": "DadosNotaFiscal",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 500,
        }
    )

    @dataclass
    class Header:
        """
        :ivar versao: Identifica a versão do layout - Fixo 001
        :ivar cnpjcpfprestador: CNPJ / CPF do emissor da Nota Fiscal
            (sem máscara)
        :ivar chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        versao: str = field(
            init=False,
            default="001",
            metadata={
                "name": "Versao",
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
        :ivar tipo_nf: Tipo da Nota Fiscal P - para Serviço Prestado
        :ivar emissao: Data de Emissão da Nota Fiscal
        :ivar cnpjcpftomador: CNPJ / CPF do Tomador de Serviço (sem
            máscara)
        :ivar nome_tomador: Nome ou Razão Social do Tomador de Serviço
        :ivar uftomador: Sigla do Estado do Tomador de Serviço
        :ivar cidade_tomador: Código do Município na Tabela IBGE do
            Tomador de Serviço
        :ivar endereco_tomador: Endereço do Tomador de Serviço
        :ivar numero_tomador: Número do Tomador de Serviço
        :ivar complemento_tomador: Complemento do Tomador de Serviço
        :ivar bairro_tomador: Bairro do Tomador de Serviço
        :ivar ceptomador: CEP do Tomador de Serviço
        :ivar email_tomador: E-mail do Tomador de Serviço
        :ivar observacao: Observações da Nota Fiscal
        :ivar nfsubstituta: Informar o número da Nota Fiscal Substituta
            de uma Nota Fiscal Cancelada.
        :ivar local_prestacao: Local da Prestação do Serviço 1 - para
            serviço na sede do prestador 2 - para serviço para imóvel
            (Construção Civil) 3 - para serviço em via pública 4 - para
            serviço fora do município
        :ivar descricao_local_prestacao: Dados do Local de Prestação do
            Serviço
        :ivar descricao_local_prestacao_complementar: Dados
            complementares do Local de Prestação do Serviço
        :ivar inscricao_imovel: Inscrição Cadastral do Imóvel (usar
            quando o Local de Prestação for do tipo 2)
        :ivar uflocal_prestacao: Sigla do Estado da Prestação do Serviço
            (usar quando o Local de Prestação for do tipo 4)
        :ivar cidade_local_prestacao: Cidade da Prestação do Serviço
            (usar quando o Local de Prestação for do tipo 4)
        :ivar endereco_local_prestacao: Endereço da Prestação do Serviço
            (usar quando o Local de Prestação for do tipo 3 ou 4)
        :ivar numero_local_prestacao: Número da localização do imóvel da
            Prestação do Serviço (usar quando o Local de Prestação for
            do tipo 4)
        :ivar complemento_local_prestacao: Complemento do imóvel da
            Prestação do Serviço (usar quando o Local de Prestação for
            do tipo 4)
        :ivar bairro_local_prestacao: Bairro da Prestação do Serviço
            (usar quando o Local de Prestação for do tipo 4)
        :ivar ceplocal_prestacao: CEP da Prestação do Serviço (usar
            quando o Local de Prestação for do tipo 4)
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
        tipo_nf: Optional[DadosNotaFiscalTipoNf] = field(
            default=None,
            metadata={
                "name": "TipoNF",
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
        nome_tomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "NomeTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        uftomador: Optional[DadosNotaFiscalUftomador1] = field(
            default=None,
            metadata={
                "name": "UFTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        cidade_tomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CidadeTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{7}",
            }
        )
        endereco_tomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "EnderecoTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        numero_tomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 10,
            }
        )
        complemento_tomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "ComplementoTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        bairro_tomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "BairroTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 40,
            }
        )
        ceptomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CEPTomador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{5}-[0-9]{3}",
            }
        )
        email_tomador: Optional[str] = field(
            default=None,
            metadata={
                "name": "EmailTomador",
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
        nfsubstituta: Optional[str] = field(
            default=None,
            metadata={
                "name": "NFSubstituta",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{10}",
            }
        )
        local_prestacao: Optional[DadosNotaFiscalLocalPrestacao1] = field(
            default=None,
            metadata={
                "name": "LocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        descricao_local_prestacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "DescricaoLocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        descricao_local_prestacao_complementar: Optional[str] = field(
            default=None,
            metadata={
                "name": "DescricaoLocalPrestacaoComplementar",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )
        inscricao_imovel: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "InscricaoImovel",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        uflocal_prestacao: Optional[DadosNotaFiscalUflocalPrestacao1] = field(
            default=None,
            metadata={
                "name": "UFLocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        cidade_local_prestacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "CidadeLocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{7}",
            }
        )
        endereco_local_prestacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "EnderecoLocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 60,
            }
        )
        numero_local_prestacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroLocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 10,
            }
        )
        complemento_local_prestacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "ComplementoLocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 30,
            }
        )
        bairro_local_prestacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "BairroLocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 40,
            }
        )
        ceplocal_prestacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "CEPLocalPrestacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{5}-[0-9]{3}",
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
        dados_itens_nota_fiscal: Optional["Isseletronico.DadosNotaFiscal.DadosItensNotaFiscal"] = field(
            default=None,
            metadata={
                "name": "DadosItensNotaFiscal",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        dados_impostos_nota_fiscal: List["Isseletronico.DadosNotaFiscal.DadosImpostosNotaFiscal"] = field(
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
                (de acordo com lista informada pela Prefeitura)
            :ivar texto_item: Texto do Item da Nota Fiscal
            :ivar valor_item: Valor do Item da Nota Fiscal
            :ivar valor_deducao: Valor das Deduções da Nota Fiscal
            :ivar retido: Identifica se o imposto do serviço foi retido
                na fonte pelo Tomador S - para Imposto Retido pelo
                Tomador N - para Imposto Não Retido pelo Tomador
            :ivar pais:
            """
            item_atividade: Optional[int] = field(
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
