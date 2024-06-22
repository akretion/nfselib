from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Tbnfd:
    class Meta:
        name = "tbnfd"

    nfd: Optional["Tbnfd.Nfd"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class Nfd:
        numeronfd: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        codseriedocumento: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        codnaturezaoperacao: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        codigocidade: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        inscricaomunicipalemissor: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        dataemissao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]{2}/){2}[0-9]{4}",
            },
        )
        razaotomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 150,
            },
        )
        nomefantasiatomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 150,
            },
        )
        enderecotomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 255,
            },
        )
        cidadetomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 60,
            },
        )
        estadotomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 2,
            },
        )
        paistomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 60,
            },
        )
        fonetomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 30,
            },
        )
        faxtomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 20,
            },
        )
        ceptomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 10,
            },
        )
        bairrotomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 60,
            },
        )
        emailtomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 255,
            },
        )
        cpfcnpjtomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 18,
            },
        )
        inscricaoestadualtomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 25,
            },
        )
        inscricaomunicipaltomador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 20,
            },
        )
        observacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 0,
                "max_length": 255,
            },
        )
        tbfatura: Optional["Tbnfd.Nfd.Tbfatura"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        tbservico: Optional["Tbnfd.Nfd.Tbservico"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        razaotransportadora: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 150,
            },
        )
        cpfcnpjtransportadora: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 20,
            },
        )
        enderecotransportadora: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 255,
            },
        )
        tipofrete: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 100,
            },
        )
        quantidade: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        especie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 50,
            },
        )
        pesoliquido: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        pesobruto: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        pis: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        cofins: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        csll: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        irrf: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        inss: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        descdeducoesconstrucao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        totaldeducoesconstrucao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"([0-9]*)([,]?)[0-9]{0,9}",
            },
        )
        tributadonomunicipio: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        numerort: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]*",
            },
        )
        codigoseriert: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]*",
            },
        )
        dataemissaort: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"(([0-9]{2}/){2}[0-9]{4})?",
            },
        )
        numerofatura: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class Tbfatura:
            fatura: List["Tbnfd.Nfd.Tbfatura.Fatura"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class Fatura:
                numfatura: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    },
                )
                vencimentofatura: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "pattern": r"([0-9]{2}/){2}[0-9]{4}",
                    },
                )
                valorfatura: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "pattern": r"[0-9]+([,]?)[0-9]{0,9}",
                    },
                )

        @dataclass
        class Tbservico:
            servico: List["Tbnfd.Nfd.Tbservico.Servico"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class Servico:
                unidade: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "max_length": 5,
                    },
                )
                quantidade: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "pattern": r"[0-9]+([,]?)[0-9]{0,4}",
                    },
                )
                descricao: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "max_length": 255,
                    },
                )
                codatividade: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    },
                )
                valorunitario: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "pattern": r"[0-9]+([,]?)[0-9]{0,9}",
                    },
                )
                aliquota: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "pattern": r"[0-9]+([,]?)[0-9]{0,2}",
                    },
                )
                impostoretido: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                        "max_length": 1,
                    },
                )
