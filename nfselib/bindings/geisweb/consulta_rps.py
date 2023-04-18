from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConsultaRps:
    CnpjCpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    Consulta: Optional["ConsultaRps.Consulta"] = field(
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
        NumeroRps: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        DtInicial: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        DtFinal: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        NumeroInicial: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        NumeroFinal: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        Pagina: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
