from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class IsseconsultaNota:
    class Meta:
        name = "ISSEConsultaNota"

    Header: Optional["IsseconsultaNota.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    Filtro: Optional["IsseconsultaNota.Filtro"] = field(
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
        :ivar Versao: Identifica a versão do layout - Fixo 003
        :ivar CNPJCPFPrestador: CNPJ / CPF do emissor da Nota Fiscal
            (sem máscara)
        :ivar Chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        Versao: str = field(
            init=False,
            default="003",
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
        :ivar NumeroNFInicial: Número da Nota Fiscal inicial (caso o
            filtro não seja por Número, informar o valor "0")
        :ivar NumeroNFFinal: Número da Nota Fiscal final (caso o filtro
            não seja por Número, informar o valor "0")
        :ivar Referencia: Data de Referência (formato: yyyyMM - yyyy =
            ano com 4 digitos e MM = mês com 2 digitos) - (caso o filtro
            não seja por referencia, informar o valor "000000")
        :ivar Lote: Número do Lote (caso o filtro não seja por Lote,
            informar o valor "0")
        :ivar TipoDocumento: Código do Tipo de Nota Fiscal (verificar
            com a Prefeitura a lista de códigos válidos) - (caso o
            filtro não seja por Tipo de Documento, informar o valor
            "000")
        """
        NumeroNFInicial: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        NumeroNFFinal: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Referencia: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{6}",
            }
        )
        Lote: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        TipoDocumento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{3}",
            }
        )
