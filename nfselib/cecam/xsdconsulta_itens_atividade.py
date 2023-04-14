from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConsultaItensAtividade:
    Header: Optional["ConsultaItensAtividade.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ParametrosPesquisa: Optional["ConsultaItensAtividade.ParametrosPesquisa"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Header:
        CPFCNPJRequisitante: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 11,
                "max_length": 14,
            }
        )
        Chave: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "length": 48,
            }
        )

    @dataclass
    class ParametrosPesquisa:
        CodigoServico: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
