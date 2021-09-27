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
    dt_cancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtCancelamento",
            "type": "Element",
            "namespace": "",
        }
    )
    mensagem_retorno: Optional[TcMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "mensagemRetorno",
            "type": "Element",
            "namespace": "",
        }
    )
