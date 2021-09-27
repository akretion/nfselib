from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConsultaLoteRps:
    cnpj_cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnpjCpf",
            "type": "Element",
            "required": True,
        }
    )
    consulta: Optional["ConsultaLoteRps.Consulta"] = field(
        default=None,
        metadata={
            "name": "Consulta",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Consulta:
        cnpj_cpf_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "CnpjCpfPrestador",
                "type": "Element",
                "required": True,
            }
        )
        numero_lote: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroLote",
                "type": "Element",
                "required": True,
            }
        )
