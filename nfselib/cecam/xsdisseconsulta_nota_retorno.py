from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class IsseconsultaNotaRetorno:
    class Meta:
        name = "ISSEConsultaNotaRetorno"

    Header: Optional["IsseconsultaNotaRetorno.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    DadosNotaFiscal: List["IsseconsultaNotaRetorno.DadosNotaFiscal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    Erro: List["IsseconsultaNotaRetorno.Erro"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Header:
        """
        :ivar Versao: Identifica a versão do layout - Fixo 003
        :ivar CNPJCPFPrestador: CNPJ / CPF do emissor da Nota Fiscal
        """
        Versao: str = field(
            init=False,
            default="003",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        CNPJCPFPrestador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )

    @dataclass
    class DadosNotaFiscal:
        """
        :ivar NumeroNF: Número da Nota Fiscal
        :ivar ChaveValidacao: Chave de Validação da Nota Fiscal
        :ivar Lote: Número do Lote de Envio da Nota Fiscal
        :ivar SituacaoNF: Situação da Nota Fiscal N - para Nota Normal C
            - para Nota Cancelada
        :ivar TipoNF: Tipo da Nota Fiscal P - para Serviço Prestado T -
            para Serviço Tomado
        :ivar Emissao: Data de Emissão da Nota Fiscal
        :ivar CNPJCPFTomador: CNPJ / CPF do Tomador de Serviço
        :ivar NomeTomador: Nome ou Razão Social do Tomador de Serviço
        :ivar InscricaoMunicipalTomador: Inscricao municipal do Tomador
            de Serviço
        :ivar InscricaoEstadualTomador: Inscricao Estadual do Tomador de
            Serviço
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
        :ivar InscricaoImovel: Inscrição Cadastral do Imóvel
        :ivar InscriçãoMunicipalPrestador: Inscrição Municipal do
            Prestador do Serviço
        :ivar InscriçãoEstadualPrestador: Inscrição Estadual do
            Prestador do Serviço
        :ivar EmailPrestador: Email do Prestador do Serviço
        :ivar cepPrestador: Cep do Prestador do Serviço
        :ivar UFLocalPrestacao: Sigla do Estado da Prestação do Serviço
        :ivar CidadeLocalPrestacao: Cidade da Prestação do Serviço
        :ivar EnderecoLocalPrestacao: Endereço da Prestação do Serviço
        :ivar NumeroLocalPrestacao: Número da localização do imóvel da
            Prestação do Serviço
        :ivar ComplementoLocalPrestacao: Complemento do imóvel da
            Prestação do Serviço
        :ivar BairroLocalPrestacao: Bairro da Prestação do Serviço
        :ivar CEPLocalPrestacao: CEP da Prestação do Serviço
        :ivar MotivoCancelamento: Descrição do Motivo de Cancelamento da
            Nota Fiscal
        :ivar TipoDocumento: Código do Tipo de Nota Fiscal
        :ivar ValorTotalNota: Valor Total da Nota Fiscal
        :ivar ValorLiquidoNota: Valor Liquido da Nota Fiscal
        :ivar DadosItensNotaFiscal:
        :ivar DadosImpostosNotaFiscal:
        :ivar OutrasInformacoes:
        """
        NumeroNF: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        ChaveValidacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Lote: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        SituacaoNF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        TipoNF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Emissao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        CNPJCPFTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        NomeTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        InscricaoMunicipalTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        InscricaoEstadualTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        UFTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        CidadeTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        EnderecoTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        NumeroTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        ComplementoTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        BairroTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        CEPTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        EmailTomador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        Observacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        NFSubstituta: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        LocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        DescricaoLocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        DescricaoLocalPrestacaoComplementar: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        InscricaoImovel: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        InscriçãoMunicipalPrestador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        InscriçãoEstadualPrestador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        EmailPrestador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        cepPrestador: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        UFLocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        CidadeLocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        EnderecoLocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        NumeroLocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        ComplementoLocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        BairroLocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        CEPLocalPrestacao: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        MotivoCancelamento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        TipoDocumento: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        ValorTotalNota: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        ValorLiquidoNota: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        DadosItensNotaFiscal: Optional["IsseconsultaNotaRetorno.DadosNotaFiscal.DadosItensNotaFiscal"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        DadosImpostosNotaFiscal: List["IsseconsultaNotaRetorno.DadosNotaFiscal.DadosImpostosNotaFiscal"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        OutrasInformacoes: List["IsseconsultaNotaRetorno.DadosNotaFiscal.OutrasInformacoes"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class DadosItensNotaFiscal:
            """
            :ivar ItemAtividade: Código do Item da Atividade prestado
            :ivar TextoItem: Texto do Item da Nota Fiscal
            :ivar ValorItem: Valor do Item da Nota Fiscal
            :ivar ValorDeducao: Valor das Deduções da Nota Fiscal
            :ivar Retido: Identifica se o imposto do serviço foi retido
                na fonte pelo Tomador S - para Imposto Retido pelo
                Tomador N - para Imposto Não Retido pelo Tomador
            :ivar Pais:
            :ivar CodigoServico: Código do Serviço
            :ivar ValorBaseCalculo: Valor da Base de Calculo
            :ivar ValorISS: Valor do ISS
            :ivar Aliquota: Valor da Aliquota
            """
            ItemAtividade: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            TextoItem: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ValorItem: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ValorDeducao: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            Retido: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            Pais: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            CodigoServico: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ValorBaseCalculo: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ValorISS: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            Aliquota: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

        @dataclass
        class DadosImpostosNotaFiscal:
            """
            :ivar Imposto: Sigla do Imposto utilizado na Dedução
            :ivar ValorImposto: Valor do Imposto utilizado na Dedução
            """
            Imposto: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ValorImposto: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

        @dataclass
        class OutrasInformacoes:
            """
            :ivar Informacao: Informações Adicionais, por exemplo:
                “Empresa optante do Simples Nacional.”.
            """
            Informacao: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

    @dataclass
    class Erro:
        """
        :ivar ID: Identificador do Registro
        :ivar Erro: Mensagem de Erro do Arquivo
        """
        ID: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Erro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
