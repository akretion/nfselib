from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class IsseconsultaNota:
    class Meta:
        name = "ISSEConsultaNota"

    header: Optional["IsseconsultaNota.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    filtro: Optional["IsseconsultaNota.Filtro"] = field(
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
        :ivar versao: Identifica a versão do layout - Fixo 003
        :ivar cnpjcpfprestador: CNPJ / CPF do emissor da Nota Fiscal
            (sem máscara)
        :ivar chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetrônico
        """
        versao: str = field(
            init=False,
            default="003",
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
        :ivar numero_nfinicial: Número da Nota Fiscal inicial (caso o
            filtro não seja por Número, informar o valor "0")
        :ivar numero_nffinal: Número da Nota Fiscal final (caso o filtro
            não seja por Número, informar o valor "0")
        :ivar referencia: Data de Referência (formato: yyyyMM - yyyy =
            ano com 4 digitos e MM = mês com 2 digitos) - (caso o filtro
            não seja por referencia, informar o valor "000000")
        :ivar lote: Número do Lote (caso o filtro não seja por Lote,
            informar o valor "0")
        :ivar tipo_documento: Código do Tipo de Nota Fiscal (verificar
            com a Prefeitura a lista de códigos válidos) - (caso o
            filtro não seja por Tipo de Documento, informar o valor
            "000")
        """
        numero_nfinicial: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "NumeroNFInicial",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        numero_nffinal: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "NumeroNFFinal",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        referencia: Optional[str] = field(
            default=None,
            metadata={
                "name": "Referencia",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{6}",
            }
        )
        lote: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Lote",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        tipo_documento: Optional[str] = field(
            default=None,
            metadata={
                "name": "TipoDocumento",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{3}",
            }
        )
