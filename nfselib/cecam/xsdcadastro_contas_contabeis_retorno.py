from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class Retorno:
    header: Optional["Retorno.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dados_conta: List["Retorno.DadosConta"] = field(
        default_factory=list,
        metadata={
            "name": "DadosConta",
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
    class DadosConta:
        """
        :ivar id: Identificador do registro
        :ivar conta_cont_bil: Número da conta Contábil
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
        conta_cont_bil: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Conta Contábil",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
