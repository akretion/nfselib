from dataclasses import dataclass, field
from typing import Optional
from nfselib.equiplano.tipos_esnfs_v01 import TcIdentificacaoPrestador
from nfselib.equiplano.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsCancelarNfseEnvio:
    class Meta:
        name = "esCancelarNfseEnvio"
        namespace = "http://www.equiplano.com.br/esnfs"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrNfse",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ds_motivo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsMotivoCancelamento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1024,
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
