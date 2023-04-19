from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CancelaNfse:
    CnpjCpf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    Cancela: Optional["CancelaNfse.Cancela"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Cancela:
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
