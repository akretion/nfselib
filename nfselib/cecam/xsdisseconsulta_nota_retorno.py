from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class IsseconsultaNotaRetorno:
    class Meta:
        name = "ISSEConsultaNotaRetorno"

    header: Optional["IsseconsultaNotaRetorno.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dados_nota_fiscal: List["IsseconsultaNotaRetorno.DadosNotaFiscal"] = field(
        default_factory=list,
        metadata={
            "name": "DadosNotaFiscal",
            "type": "Element",
            "namespace": "",
        }
    )
    erro: List["IsseconsultaNotaRetorno.Erro"] = field(
        default_factory=list,
        metadata={
            "name": "Erro",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Header:
        """
        :ivar versao: Identifica a versão do layout - Fixo 003
        :ivar cnpjcpfprestador: CNPJ / CPF do emissor da Nota Fiscal
        """
        versao: str = field(
            init=False,
            default="003",
            metadata={
                "name": "Versao",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        cnpjcpfprestador: Optional[object] = field(
            default=None,
            metadata={
                "name": "CNPJCPFPrestador",
                "type": "Element",
                "namespace": "",
            }
        )

    @dataclass
    class DadosNotaFiscal:
        """
        :ivar numero_nf: Número da Nota Fiscal
        :ivar chave_validacao: Chave de Validação da Nota Fiscal
        :ivar lote: Número do Lote de Envio da Nota Fiscal
        :ivar situacao_nf: Situação da Nota Fiscal N - para Nota Normal
            C - para Nota Cancelada
        :ivar tipo_nf: Tipo da Nota Fiscal P - para Serviço Prestado T -
            para Serviço Tomado
        :ivar emissao: Data de Emissão da Nota Fiscal
        :ivar cnpjcpftomador: CNPJ / CPF do Tomador de Serviço
        :ivar nome_tomador: Nome ou Razão Social do Tomador de Serviço
        :ivar inscricao_municipal_tomador: Inscricao municipal do
            Tomador de Serviço
        :ivar inscricao_estadual_tomador: Inscricao Estadual do Tomador
            de Serviço
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
        :ivar inscricao_imovel: Inscrição Cadastral do Imóvel
        :ivar inscri_o_municipal_prestador: Inscrição Municipal do
            Prestador do Serviço
        :ivar inscri_o_estadual_prestador: Inscrição Estadual do
            Prestador do Serviço
        :ivar email_prestador: Email do Prestador do Serviço
        :ivar cep_prestador: Cep do Prestador do Serviço
        :ivar uflocal_prestacao: Sigla do Estado da Prestação do Serviço
        :ivar cidade_local_prestacao: Cidade da Prestação do Serviço
        :ivar endereco_local_prestacao: Endereço da Prestação do Serviço
        :ivar numero_local_prestacao: Número da localização do imóvel da
            Prestação do Serviço
        :ivar complemento_local_prestacao: Complemento do imóvel da
            Prestação do Serviço
        :ivar bairro_local_prestacao: Bairro da Prestação do Serviço
        :ivar ceplocal_prestacao: CEP da Prestação do Serviço
        :ivar motivo_cancelamento: Descrição do Motivo de Cancelamento
            da Nota Fiscal
        :ivar tipo_documento: Código do Tipo de Nota Fiscal
        :ivar valor_total_nota: Valor Total da Nota Fiscal
        :ivar valor_liquido_nota: Valor Liquido da Nota Fiscal
        :ivar dados_itens_nota_fiscal:
        :ivar dados_impostos_nota_fiscal:
        :ivar outras_informacoes:
        """
        numero_nf: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "NumeroNF",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        chave_validacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "ChaveValidacao",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        lote: Optional[object] = field(
            default=None,
            metadata={
                "name": "Lote",
                "type": "Element",
                "namespace": "",
            }
        )
        situacao_nf: Optional[str] = field(
            default=None,
            metadata={
                "name": "SituacaoNF",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        tipo_nf: Optional[str] = field(
            default=None,
            metadata={
                "name": "TipoNF",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        emissao: Optional[object] = field(
            default=None,
            metadata={
                "name": "Emissao",
                "type": "Element",
                "namespace": "",
            }
        )
        cnpjcpftomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "CNPJCPFTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        nome_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "NomeTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        inscricao_municipal_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "InscricaoMunicipalTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        inscricao_estadual_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "InscricaoEstadualTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        uftomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "UFTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        cidade_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "CidadeTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        endereco_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "EnderecoTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        numero_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "NumeroTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        complemento_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "ComplementoTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        bairro_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "BairroTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        ceptomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "CEPTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        email_tomador: Optional[object] = field(
            default=None,
            metadata={
                "name": "EmailTomador",
                "type": "Element",
                "namespace": "",
            }
        )
        observacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "Observacao",
                "type": "Element",
                "namespace": "",
            }
        )
        nfsubstituta: Optional[object] = field(
            default=None,
            metadata={
                "name": "NFSubstituta",
                "type": "Element",
                "namespace": "",
            }
        )
        local_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "LocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        descricao_local_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "DescricaoLocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        descricao_local_prestacao_complementar: Optional[object] = field(
            default=None,
            metadata={
                "name": "DescricaoLocalPrestacaoComplementar",
                "type": "Element",
                "namespace": "",
            }
        )
        inscricao_imovel: Optional[object] = field(
            default=None,
            metadata={
                "name": "InscricaoImovel",
                "type": "Element",
                "namespace": "",
            }
        )
        inscri_o_municipal_prestador: Optional[object] = field(
            default=None,
            metadata={
                "name": "InscriçãoMunicipalPrestador",
                "type": "Element",
                "namespace": "",
            }
        )
        inscri_o_estadual_prestador: Optional[object] = field(
            default=None,
            metadata={
                "name": "InscriçãoEstadualPrestador",
                "type": "Element",
                "namespace": "",
            }
        )
        email_prestador: Optional[object] = field(
            default=None,
            metadata={
                "name": "EmailPrestador",
                "type": "Element",
                "namespace": "",
            }
        )
        cep_prestador: Optional[object] = field(
            default=None,
            metadata={
                "name": "cepPrestador",
                "type": "Element",
                "namespace": "",
            }
        )
        uflocal_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "UFLocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        cidade_local_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "CidadeLocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        endereco_local_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "EnderecoLocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        numero_local_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "NumeroLocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        complemento_local_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "ComplementoLocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        bairro_local_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "BairroLocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        ceplocal_prestacao: Optional[object] = field(
            default=None,
            metadata={
                "name": "CEPLocalPrestacao",
                "type": "Element",
                "namespace": "",
            }
        )
        motivo_cancelamento: Optional[str] = field(
            default=None,
            metadata={
                "name": "MotivoCancelamento",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        tipo_documento: Optional[object] = field(
            default=None,
            metadata={
                "name": "TipoDocumento",
                "type": "Element",
                "namespace": "",
            }
        )
        valor_total_nota: Optional[object] = field(
            default=None,
            metadata={
                "name": "ValorTotalNota",
                "type": "Element",
                "namespace": "",
            }
        )
        valor_liquido_nota: Optional[object] = field(
            default=None,
            metadata={
                "name": "ValorLiquidoNota",
                "type": "Element",
                "namespace": "",
            }
        )
        dados_itens_nota_fiscal: Optional["IsseconsultaNotaRetorno.DadosNotaFiscal.DadosItensNotaFiscal"] = field(
            default=None,
            metadata={
                "name": "DadosItensNotaFiscal",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        dados_impostos_nota_fiscal: List["IsseconsultaNotaRetorno.DadosNotaFiscal.DadosImpostosNotaFiscal"] = field(
            default_factory=list,
            metadata={
                "name": "DadosImpostosNotaFiscal",
                "type": "Element",
                "namespace": "",
            }
        )
        outras_informacoes: List["IsseconsultaNotaRetorno.DadosNotaFiscal.OutrasInformacoes"] = field(
            default_factory=list,
            metadata={
                "name": "OutrasInformacoes",
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class DadosItensNotaFiscal:
            """
            :ivar item_atividade: Código do Item da Atividade prestado
            :ivar texto_item: Texto do Item da Nota Fiscal
            :ivar valor_item: Valor do Item da Nota Fiscal
            :ivar valor_deducao: Valor das Deduções da Nota Fiscal
            :ivar retido: Identifica se o imposto do serviço foi retido
                na fonte pelo Tomador S - para Imposto Retido pelo
                Tomador N - para Imposto Não Retido pelo Tomador
            :ivar pais:
            :ivar codigo_servico: Código do Serviço
            :ivar valor_base_calculo: Valor da Base de Calculo
            :ivar valor_iss: Valor do ISS
            :ivar aliquota: Valor da Aliquota
            """
            item_atividade: Optional[object] = field(
                default=None,
                metadata={
                    "name": "ItemAtividade",
                    "type": "Element",
                    "namespace": "",
                }
            )
            texto_item: Optional[object] = field(
                default=None,
                metadata={
                    "name": "TextoItem",
                    "type": "Element",
                    "namespace": "",
                }
            )
            valor_item: Optional[object] = field(
                default=None,
                metadata={
                    "name": "ValorItem",
                    "type": "Element",
                    "namespace": "",
                }
            )
            valor_deducao: Optional[object] = field(
                default=None,
                metadata={
                    "name": "ValorDeducao",
                    "type": "Element",
                    "namespace": "",
                }
            )
            retido: Optional[object] = field(
                default=None,
                metadata={
                    "name": "Retido",
                    "type": "Element",
                    "namespace": "",
                }
            )
            pais: Optional[object] = field(
                default=None,
                metadata={
                    "name": "Pais",
                    "type": "Element",
                    "namespace": "",
                }
            )
            codigo_servico: Optional[object] = field(
                default=None,
                metadata={
                    "name": "CodigoServico",
                    "type": "Element",
                    "namespace": "",
                }
            )
            valor_base_calculo: Optional[object] = field(
                default=None,
                metadata={
                    "name": "ValorBaseCalculo",
                    "type": "Element",
                    "namespace": "",
                }
            )
            valor_iss: Optional[object] = field(
                default=None,
                metadata={
                    "name": "ValorISS",
                    "type": "Element",
                    "namespace": "",
                }
            )
            aliquota: Optional[object] = field(
                default=None,
                metadata={
                    "name": "Aliquota",
                    "type": "Element",
                    "namespace": "",
                }
            )

        @dataclass
        class DadosImpostosNotaFiscal:
            """
            :ivar imposto: Sigla do Imposto utilizado na Dedução
            :ivar valor_imposto: Valor do Imposto utilizado na Dedução
            """
            imposto: Optional[object] = field(
                default=None,
                metadata={
                    "name": "Imposto",
                    "type": "Element",
                    "namespace": "",
                }
            )
            valor_imposto: Optional[object] = field(
                default=None,
                metadata={
                    "name": "ValorImposto",
                    "type": "Element",
                    "namespace": "",
                }
            )

        @dataclass
        class OutrasInformacoes:
            """
            :ivar informacao: Informações Adicionais, por exemplo:
                “Empresa optante do Simples Nacional.”.
            """
            informacao: Optional[object] = field(
                default=None,
                metadata={
                    "name": "Informacao",
                    "type": "Element",
                    "namespace": "",
                }
            )

    @dataclass
    class Erro:
        """
        :ivar id: Identificador do Registro
        :ivar erro: Mensagem de Erro do Arquivo
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
        erro: Optional[str] = field(
            default=None,
            metadata={
                "name": "Erro",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
