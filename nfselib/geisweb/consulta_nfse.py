from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConsultaNfse:
    cnpj_cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnpjCpf",
            "type": "Element",
            "required": True,
        }
    )
    consulta: Optional["ConsultaNfse.Consulta"] = field(
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
        numero_nfse: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroNfse",
                "type": "Element",
                "required": True,
            }
        )
        dt_inicial: Optional[str] = field(
            default=None,
            metadata={
                "name": "DtInicial",
                "type": "Element",
                "required": True,
            }
        )
        dt_final: Optional[str] = field(
            default=None,
            metadata={
                "name": "DtFinal",
                "type": "Element",
                "required": True,
            }
        )
        numero_inicial: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroInicial",
                "type": "Element",
                "required": True,
            }
        )
        numero_final: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroFinal",
                "type": "Element",
                "required": True,
            }
        )
        pagina: Optional[str] = field(
            default=None,
            metadata={
                "name": "Pagina",
                "type": "Element",
                "required": True,
            }
        )
