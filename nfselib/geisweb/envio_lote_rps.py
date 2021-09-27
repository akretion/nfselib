from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.geisweb.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.geisweb.com.br/xsd/envio_lote_rps.xsd"


@dataclass
class EnviaLoteRps:
    class Meta:
        namespace = "http://www.geisweb.com.br/xsd/envio_lote_rps.xsd"

    cnpj_cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnpjCpf",
            "type": "Element",
            "required": True,
        }
    )
    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "required": True,
        }
    )
    rps: List["EnviaLoteRps.Rps"] = field(
        default_factory=list,
        metadata={
            "name": "Rps",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Rps:
        identificacao_rps: Optional["EnviaLoteRps.Rps.IdentificacaoRps"] = field(
            default=None,
            metadata={
                "name": "IdentificacaoRps",
                "type": "Element",
                "required": True,
            }
        )
        data_emissao: Optional[str] = field(
            default=None,
            metadata={
                "name": "DataEmissao",
                "type": "Element",
                "required": True,
            }
        )
        servico: Optional["EnviaLoteRps.Rps.Servico"] = field(
            default=None,
            metadata={
                "name": "Servico",
                "type": "Element",
                "required": True,
            }
        )
        prestador_servico: Optional["EnviaLoteRps.Rps.PrestadorServico"] = field(
            default=None,
            metadata={
                "name": "PrestadorServico",
                "type": "Element",
                "required": True,
            }
        )
        tomador_servico: Optional["EnviaLoteRps.Rps.TomadorServico"] = field(
            default=None,
            metadata={
                "name": "TomadorServico",
                "type": "Element",
                "required": True,
            }
        )
        orgao_gerador: Optional["EnviaLoteRps.Rps.OrgaoGerador"] = field(
            default=None,
            metadata={
                "name": "OrgaoGerador",
                "type": "Element",
                "required": True,
            }
        )
        outros_impostos: Optional["EnviaLoteRps.Rps.OutrosImpostos"] = field(
            default=None,
            metadata={
                "name": "OutrosImpostos",
                "type": "Element",
                "required": True,
            }
        )
        signature: Optional[Signature] = field(
            default=None,
            metadata={
                "name": "Signature",
                "type": "Element",
                "namespace": "http://www.w3.org/2000/09/xmldsig#",
            }
        )

        @dataclass
        class IdentificacaoRps:
            numero_rps: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NumeroRps",
                    "type": "Element",
                    "required": True,
                }
            )

        @dataclass
        class Servico:
            valores: Optional["EnviaLoteRps.Rps.Servico.Valores"] = field(
                default=None,
                metadata={
                    "name": "Valores",
                    "type": "Element",
                    "required": True,
                }
            )
            codigo_servico: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CodigoServico",
                    "type": "Element",
                    "required": True,
                }
            )
            tipo_lancamento: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TipoLancamento",
                    "type": "Element",
                    "required": True,
                }
            )
            discriminacao: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Discriminacao",
                    "type": "Element",
                    "required": True,
                }
            )
            municipio_prestacao_servico: Optional[str] = field(
                default=None,
                metadata={
                    "name": "MunicipioPrestacaoServico",
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class Valores:
                valor_servicos: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ValorServicos",
                        "type": "Element",
                        "required": True,
                    }
                )
                base_calculo: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BaseCalculo",
                        "type": "Element",
                        "required": True,
                    }
                )
                aliquota: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Aliquota",
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass
        class PrestadorServico:
            identificacao_prestador: Optional["EnviaLoteRps.Rps.PrestadorServico.IdentificacaoPrestador"] = field(
                default=None,
                metadata={
                    "name": "IdentificacaoPrestador",
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class IdentificacaoPrestador:
                cnpj_cpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CnpjCpf",
                        "type": "Element",
                        "required": True,
                    }
                )
                inscricao_municipal: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "InscricaoMunicipal",
                        "type": "Element",
                        "required": True,
                    }
                )
                regime: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Regime",
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass
        class TomadorServico:
            identificacao_tomador: Optional["EnviaLoteRps.Rps.TomadorServico.IdentificacaoTomador"] = field(
                default=None,
                metadata={
                    "name": "IdentificacaoTomador",
                    "type": "Element",
                    "required": True,
                }
            )
            razao_social: Optional[str] = field(
                default=None,
                metadata={
                    "name": "RazaoSocial",
                    "type": "Element",
                    "required": True,
                }
            )
            endereco: Optional["EnviaLoteRps.Rps.TomadorServico.Endereco"] = field(
                default=None,
                metadata={
                    "name": "Endereco",
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class IdentificacaoTomador:
                cnpj_cpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CnpjCpf",
                        "type": "Element",
                        "required": True,
                    }
                )

            @dataclass
            class Endereco:
                rua: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Rua",
                        "type": "Element",
                        "required": True,
                    }
                )
                numero: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Numero",
                        "type": "Element",
                        "required": True,
                    }
                )
                bairro: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Bairro",
                        "type": "Element",
                        "required": True,
                    }
                )
                cidade: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Cidade",
                        "type": "Element",
                        "required": True,
                    }
                )
                estado: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Estado",
                        "type": "Element",
                        "required": True,
                    }
                )
                cep: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Cep",
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass
        class OrgaoGerador:
            codigo_municipio: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CodigoMunicipio",
                    "type": "Element",
                    "required": True,
                }
            )
            uf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Uf",
                    "type": "Element",
                    "required": True,
                }
            )

        @dataclass
        class OutrosImpostos:
            pis: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Pis",
                    "type": "Element",
                    "required": True,
                }
            )
            cofins: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Cofins",
                    "type": "Element",
                    "required": True,
                }
            )
            csll: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Csll",
                    "type": "Element",
                    "required": True,
                }
            )
            irrf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Irrf",
                    "type": "Element",
                    "required": True,
                }
            )
            inss: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Inss",
                    "type": "Element",
                    "required": True,
                }
            )
