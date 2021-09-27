from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class CadastroContasContabeis:
    header: Optional["CadastroContasContabeis.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dados_conta: List["CadastroContasContabeis.DadosConta"] = field(
        default_factory=list,
        metadata={
            "name": "DadosConta",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
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
    class DadosConta:
        """
        :ivar conta_contabil: Númeroo da conta contábil
        :ivar descricao_conta_contabil: Descrição da conta contábil
        :ivar cosif: Número do Cosif
        :ivar servico: Código do Serviço
        """
        conta_contabil: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "ContaContabil",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        descricao_conta_contabil: Optional[str] = field(
            default=None,
            metadata={
                "name": "DescricaoContaContabil",
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 50,
            }
        )
        cosif: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Cosif",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        servico: Optional[str] = field(
            default=None,
            metadata={
                "name": "Servico",
                "type": "Element",
                "namespace": "",
                "required": True,
                "max_length": 7,
            }
        )
