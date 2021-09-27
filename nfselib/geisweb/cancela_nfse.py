from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CancelaNfse:
    cnpj_cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnpjCpf",
            "type": "Element",
            "required": True,
        }
    )
    cancela: Optional["CancelaNfse.Cancela"] = field(
        default=None,
        metadata={
            "name": "Cancela",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Cancela:
        cnpj_cpf_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CnpjCpfPrestador",
                "type": "Element",
                "required": True,
            }
        )
        numero_nfse: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroNfse",
                "type": "Element",
                "required": True,
            }
        )
