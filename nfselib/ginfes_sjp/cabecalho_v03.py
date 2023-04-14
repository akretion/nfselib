from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nfe.sjp.pr.gov.br/cabecalho_v03.xsd"


@dataclass
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://nfe.sjp.pr.gov.br/cabecalho_v03.xsd"

    versaoDados: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "white_space": "collapse",
            "pattern": r"[0-9]{1,4}",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r"[0-9]{1,4}",
        }
    )
