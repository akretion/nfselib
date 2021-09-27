from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class ConsultaContasPendentes:
    header: Optional["ConsultaContasPendentes.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    filtro: Optional["ConsultaContasPendentes.Filtro"] = field(
        default=None,
        metadata={
            "name": "Filtro",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Header:
        """
        :ivar cnpjinstituicao: CNPJ da Instituicao Financeira (sem
            mascara)
        :ivar chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetronico
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
    class Filtro:
        """
        :ivar conta_contabil: Número da conta contábil
        :ivar descricao_conta_contabil: Descrição da conta contábil
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
