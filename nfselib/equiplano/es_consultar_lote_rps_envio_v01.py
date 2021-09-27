from dataclasses import dataclass, field
from typing import Optional
from nfselib.equiplano.tipos_esnfs_v01 import TcIdentificacaoPrestador
from nfselib.equiplano.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsConsultarLoteRpsEnvio:
    class Meta:
        name = "esConsultarLoteRpsEnvio"
        namespace = "http://www.equiplano.com.br/esnfs"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_lote_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrLoteRps",
            "type": "Element",
            "namespace": "",
        }
    )
    nr_protocolo: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrProtocolo",
            "type": "Element",
            "namespace": "",
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
