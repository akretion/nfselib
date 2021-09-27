from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class IssecancelaNfe:
    class Meta:
        name = "ISSECancelaNFe"

    header: Optional["IssecancelaNfe.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    filtro: Optional["IssecancelaNfe.Filtro"] = field(
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
        :ivar versao: Identifica a versão do layout - Fixo 004
        :ivar cnpjcpfprestador: CNPJ / CPF do emissor da Nota Fiscal
            (sem máscara)
        :ivar chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        versao: str = field(
            init=False,
            default="004",
            metadata={
                "name": "Versao",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        cnpjcpfprestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJCPFPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 11,
                "max_length": 14,
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
        :ivar numero_nf: Número da Nota Fiscal
        :ivar chave_validacao: Chave de Validação da Nota Fiscal
        :ivar motivo_cancelamento: Descrição do Motivo de Cancelamento
            da Nota Fiscal
        """
        numero_nf: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "NumeroNF",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        chave_validacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "ChaveValidacao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9A-Z]{4}-[0-9A-Z]{5}",
            }
        )
        motivo_cancelamento: Optional[str] = field(
            default=None,
            metadata={
                "name": "MotivoCancelamento",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 10,
                "max_length": 200,
            }
        )
