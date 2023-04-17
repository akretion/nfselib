from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class Retorno:
    NotaFiscal: List["Retorno.NotaFiscal"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    Erro: List["Retorno.Erro"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class NotaFiscal:
        """
        :ivar ID: Identificador do Registro
        :ivar NumeroNF: Número da Nota Fiscal
        :ivar ChaveValidacao: Chave de Validação da Nota Fiscal
        :ivar Lote: Número do Lote de Envio da Nota Fiscal
        """
        ID: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
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

    @dataclass
    class Erro:
        """
        :ivar ID: Identificador do Registro (RPS)
        :ivar Erro: Mensagem de Erro do Arquivo
        """
        ID: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Erro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
