from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class LancamentosInstituicaoFinanceira:
    header: Optional["LancamentosInstituicaoFinanceira.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dados_lancamento: List["LancamentosInstituicaoFinanceira.DadosLancamento"] = field(
        default_factory=list,
        metadata={
            "name": "DadosLancamento",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )

    @dataclass
    class Header:
        """
        :ivar cnpjinstituicao: CNPJ da Instituição Financeira
        :ivar chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        cnpjinstituicao: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJInstituicao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "length": 14,
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
    class DadosLancamento:
        """
        :ivar numero_documento: Identificador do registro
        :ivar lote: Número do lote gerado no sistema
        """
        numero_documento: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumeroDocumento",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        lote: Optional[int] = field(
            default=None,
            metadata={
                "name": "Lote",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
