from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class CadastroContasContabeis:
    Header: Optional["CadastroContasContabeis.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    DadosConta: List["CadastroContasContabeis.DadosConta"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
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
    class DadosConta:
        """
        :ivar ContaContabil: Númeroo da conta contábil
        :ivar DescricaoContaContabil: Descrição da conta contábil
        :ivar Cosif: Número do Cosif
        :ivar Servico: Código do Serviço
        """
        ContaContabil: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        DescricaoContaContabil: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 50,
            }
        )
        Cosif: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Servico: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 7,
            }
        )
