from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConsultaItensAtividade:
    header: Optional["ConsultaItensAtividade.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "required": True,
        }
    )
    parametros_pesquisa: Optional["ConsultaItensAtividade.ParametrosPesquisa"] = field(
        default=None,
        metadata={
            "name": "ParametrosPesquisa",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Header:
        cpfcnpjrequisitante: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPFCNPJRequisitante",
                "type": "Element",
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
                "required": True,
                "length": 48,
            }
        )

    @dataclass
    class ParametrosPesquisa:
        codigo_servico: Optional[str] = field(
            default=None,
            metadata={
                "name": "CodigoServico",
                "type": "Element",
                "required": True,
            }
        )
