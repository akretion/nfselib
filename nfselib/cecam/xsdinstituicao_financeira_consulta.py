from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class ConsultaLancamentoInstituicaoFinanceira:
    header: Optional["ConsultaLancamentoInstituicaoFinanceira.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    filtro: Optional["ConsultaLancamentoInstituicaoFinanceira.Filtro"] = field(
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
        :ivar numero_documento_inicial: Numero inicial do documento
            (caso o filtro nao seja por Numero, informar o valor "0")
        :ivar numero_documento_final: Numero final do documento (caso o
            filtro nao seja por Numero, informar o valor "0")
        :ivar referencia: Data de Referencia (formato: yyyyMM - yyyy =
            ano com 4 digitos e MM = mes com 2 digitos) - (caso o filtro
            nao seja por referencia, informar o valor "000000")
        :ivar lote: Numero do Lote (caso o filtro nao seja por Lote,
            informar o valor "0")
        """
        numero_documento_inicial: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "NumeroDocumentoInicial",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        numero_documento_final: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "NumeroDocumentoFinal",
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
