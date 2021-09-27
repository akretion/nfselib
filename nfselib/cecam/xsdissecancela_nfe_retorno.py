from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class IssecancelaNfeRetorno:
    class Meta:
        name = "ISSECancelaNFeRetorno"

    nota_fiscal: Optional["IssecancelaNfeRetorno.NotaFiscal"] = field(
        default=None,
        metadata={
            "name": "NotaFiscal",
            "type": "Element",
            "namespace": "",
        }
    )
    erro: List["IssecancelaNfeRetorno.Erro"] = field(
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
        :ivar numero_nf: Número da Nota Fiscal
        :ivar chave_validacao: Chave de Validação da Nota Fiscal
        :ivar codigo_resultado: Código identificador do Resultado (0 =
            Não foi possível Cancelar a NF-e / 1 = Sucesso)
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
            }
        )
        codigo_resultado: Optional[str] = field(
            default=None,
            metadata={
                "name": "CodigoResultado",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )

    @dataclass
    class Erro:
        """
        :ivar id: Identificador do Registro
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
