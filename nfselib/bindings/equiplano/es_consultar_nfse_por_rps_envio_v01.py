from dataclasses import dataclass, field
from typing import Optional
from nfselib.equiplano.tipos_esnfs_v01 import (
    TcIdentificacaoPrestador,
    TcIdentificacaoRps,
)
from nfselib.equiplano.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsConsultarNfsePorRpsEnvio:
    class Meta:
        name = "esConsultarNfsePorRpsEnvio"
        namespace = "http://www.equiplano.com.br/esnfs"

    rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
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
