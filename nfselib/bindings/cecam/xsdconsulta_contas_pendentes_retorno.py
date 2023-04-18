from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class ConsultaContasPendentes:
    Header: Optional["ConsultaContasPendentes.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    Filtro: Optional["ConsultaContasPendentes.Filtro"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Header:
        """
        :ivar CNPJInstituicao: CNPJ da Instituicao Financeira (sem
            mascara)
        :ivar Chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetronico
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
    class Filtro:
        """
        :ivar ContaContabil: Número da conta contábil
        :ivar DescricaoContaContabil: Descrição da conta contábil
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
