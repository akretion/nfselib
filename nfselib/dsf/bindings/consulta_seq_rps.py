from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ConsultaSeqRps:
    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["ConsultaSeqRps.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class Cabecalho:
        CodCid: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
            },
        )
        IMPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{6,11}",
            },
        )
        CPFCNPJRemetente: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            },
        )
        SeriePrestacao: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_inclusive": 1,
                "max_inclusive": 99,
            },
        )
        Versao: str = field(
            init=False,
            default="1",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )
