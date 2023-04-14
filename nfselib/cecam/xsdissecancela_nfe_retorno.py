from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class IssecancelaNfeRetorno:
    class Meta:
        name = "ISSECancelaNFeRetorno"

    NotaFiscal: Optional["IssecancelaNfeRetorno.NotaFiscal"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    Erro: List["IssecancelaNfeRetorno.Erro"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class NotaFiscal:
        """
        :ivar NumeroNF: Número da Nota Fiscal
        :ivar ChaveValidacao: Chave de Validação da Nota Fiscal
        :ivar CodigoResultado: Código identificador do Resultado (0 =
            Não foi possível Cancelar a NF-e / 1 = Sucesso)
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
            }
        )
        CodigoResultado: Optional[str] = field(
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
        :ivar ID: Identificador do Registro
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
