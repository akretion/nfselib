from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.bindings.geisweb.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.geisweb.com.br/xsd/envio_lote_rps.xsd"


@dataclass
class EnviaLoteRps:
    class Meta:
        namespace = "http://www.geisweb.com.br/xsd/envio_lote_rps.xsd"

    CnpjCpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    NumeroLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    Rps: List["EnviaLoteRps.Rps"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Rps:
        IdentificacaoRps: Optional["EnviaLoteRps.Rps.IdentificacaoRps"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        DataEmissao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        Servico: Optional["EnviaLoteRps.Rps.Servico"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        PrestadorServico: Optional["EnviaLoteRps.Rps.PrestadorServico"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        TomadorServico: Optional["EnviaLoteRps.Rps.TomadorServico"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        OrgaoGerador: Optional["EnviaLoteRps.Rps.OrgaoGerador"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        OutrosImpostos: Optional["EnviaLoteRps.Rps.OutrosImpostos"] = field(
            default=None,
            metadata={
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
            NumeroRps: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )

        @dataclass
        class Servico:
            Valores: Optional["EnviaLoteRps.Rps.Servico.Valores"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            CodigoServico: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            TipoLancamento: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            Discriminacao: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            MunicipioPrestacaoServico: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class Valores:
                ValorServicos: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                BaseCalculo: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                Aliquota: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass
        class PrestadorServico:
            IdentificacaoPrestador: Optional["EnviaLoteRps.Rps.PrestadorServico.IdentificacaoPrestador"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class IdentificacaoPrestador:
                CnpjCpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                InscricaoMunicipal: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                Regime: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass
        class TomadorServico:
            IdentificacaoTomador: Optional["EnviaLoteRps.Rps.TomadorServico.IdentificacaoTomador"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            RazaoSocial: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            Endereco: Optional["EnviaLoteRps.Rps.TomadorServico.Endereco"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class IdentificacaoTomador:
                CnpjCpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

            @dataclass
            class Endereco:
                Rua: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                Numero: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                Bairro: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                Cidade: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                Estado: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                Cep: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass
        class OrgaoGerador:
            CodigoMunicipio: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            Uf: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )

        @dataclass
        class OutrosImpostos:
            Pis: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            Cofins: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            Csll: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            Irrf: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            Inss: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
