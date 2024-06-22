from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from nfselib.dueto.bindings.tipos_complexos import ListaMensagemRetorno

__NAMESPACE__ = "http://tempuri.org/servico_enviar_lote_rps_resposta.xsd"


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_enviar_lote_rps_resposta.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    DataRecebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        },
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://tempuri.org/tipos_complexos.xsd",
        },
    )
