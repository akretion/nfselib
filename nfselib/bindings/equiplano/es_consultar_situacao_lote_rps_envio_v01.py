from dataclasses import dataclass, field
from typing import Optional
from nfselib.equiplano.tipos_esnfs_v01 import TcIdentificacaoPrestador
from nfselib.equiplano.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsConsultarSituacaoLoteRpsEnvio:
    class Meta:
        name = "esConsultarSituacaoLoteRpsEnvio"
        namespace = "http://www.equiplano.com.br/esnfs"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrLoteRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    nrProtocolo: Optional[int] = field(
        default=None,
        metadata={
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
