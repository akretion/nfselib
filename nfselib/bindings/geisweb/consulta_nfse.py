from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConsultaNfse:
    CnpjCpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    Consulta: Optional["ConsultaNfse.Consulta"] = field(
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
        NumeroNfse: Optional[str] = field(
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
