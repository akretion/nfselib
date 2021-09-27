from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ConsultaSeqRps:
    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["ConsultaSeqRps.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Cabecalho:
        cod_cid: Optional[int] = field(
            default=None,
            metadata={
                "name": "CodCid",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
            }
        )
        imprestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "IMPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{6,11}",
            }
        )
        cpfcnpjremetente: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPFCNPJRemetente",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            }
        )
        serie_prestacao: Optional[int] = field(
            default=None,
            metadata={
                "name": "SeriePrestacao",
                "type": "Element",
                "namespace": "",
                "min_inclusive": 1,
                "max_inclusive": 99,
            }
        )
        versao: str = field(
            init=False,
            default="1",
            metadata={
                "name": "Versao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )
