from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class LancamentosInstituicaoFinanceira:
    Header: Optional["LancamentosInstituicaoFinanceira.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    DadosLancamento: List["LancamentosInstituicaoFinanceira.DadosLancamento"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )

    @dataclass
    class Header:
        """
        :ivar CNPJInstituicao: CNPJ da Instituição Financeira
        :ivar Chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        CNPJInstituicao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "length": 14,
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
    class DadosLancamento:
        """
        :ivar NumeroDocumento: Identificador do registro
        :ivar Lote: Número do lote gerado no sistema
        """
        NumeroDocumento: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Lote: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
