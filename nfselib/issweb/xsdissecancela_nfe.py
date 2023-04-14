from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class IssecancelaNfe:
    class Meta:
        name = "ISSECancelaNFe"

    Header: Optional["IssecancelaNfe.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    Filtro: Optional["IssecancelaNfe.Filtro"] = field(
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
        :ivar Versao: Identifica a versão do layout - Fixo 004
        :ivar CNPJCPFPrestador: CNPJ / CPF do emissor da Nota Fiscal
            (sem máscara)
        :ivar Chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        Versao: str = field(
            init=False,
            default="004",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        CNPJCPFPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 11,
                "max_length": 14,
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
        :ivar NumeroNF: Número da Nota Fiscal
        :ivar ChaveValidacao: Chave de Validação da Nota Fiscal
        :ivar MotivoCancelamento: Descrição do Motivo de Cancelamento da
            Nota Fiscal
        """
        NumeroNF: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        ChaveValidacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9A-Z]{4}-[0-9A-Z]{5}",
            }
        )
        MotivoCancelamento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 10,
                "max_length": 200,
            }
        )
