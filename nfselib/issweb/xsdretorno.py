from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class Retorno:
    nota_fiscal: List["Retorno.NotaFiscal"] = field(
        default_factory=list,
        metadata={
            "name": "NotaFiscal",
            "type": "Element",
            "namespace": "",
        }
    )
    erro: List["Retorno.Erro"] = field(
        default_factory=list,
        metadata={
            "name": "Erro",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class NotaFiscal:
        """
        :ivar id: Identificador do Registro
        :ivar numero_nf: Número da Nota Fiscal
        :ivar chave_validacao: Chave de Validação da Nota Fiscal
        :ivar lote: Número do Lote de Envio da Nota Fiscal
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

    @dataclass
    class Erro:
        """
        :ivar id: Identificador do Registro (RPS)
        :ivar erro: Mensagem de Erro do Arquivo
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
        erro: Optional[str] = field(
            default=None,
            metadata={
                "name": "Erro",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
