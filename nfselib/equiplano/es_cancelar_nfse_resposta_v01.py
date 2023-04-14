from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.equiplano.tipos_esnfs_v01 import TcMensagemRetorno

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsCancelarNfseResposta:
    class Meta:
        name = "esCancelarNfseResposta"
        namespace = "http://www.equiplano.com.br/esnfs"

    sucesso: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dtCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    mensagemRetorno: Optional[TcMensagemRetorno] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
