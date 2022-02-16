from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.equiplano.tipos_esnfs_v01 import (
    TcPrestador,
    TcRps,
)
from nfselib.equiplano.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        name = "enviarLoteRpsEnvio"
        namespace = "http://www.equiplano.com.br/esnfs"

    lote: Optional["EnviarLoteRpsEnvio.Lote"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )

    @dataclass
    class Lote:
        nr_lote: Optional[int] = field(
            default=None,
            metadata={
                "name": "nrLote",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        qt_rps: Optional[int] = field(
            default=None,
            metadata={
                "name": "qtRps",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        nr_versao_xml: Optional[int] = field(
            default=None,
            metadata={
                "name": "nrVersaoXml",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        prestador: Optional[TcPrestador] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        lista_rps: Optional["EnviarLoteRpsEnvio.Lote.ListaRps"] = field(
            default=None,
            metadata={
                "name": "listaRps",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )

        @dataclass
        class ListaRps:
            rps: List[TcRps] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                }
            )