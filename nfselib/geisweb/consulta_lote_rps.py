from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConsultaLoteRps:
    CnpjCpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    Consulta: Optional["ConsultaLoteRps.Consulta"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Consulta:
        CnpjCpfPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        NumeroLote: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
