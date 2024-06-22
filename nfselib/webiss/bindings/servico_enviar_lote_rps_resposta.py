from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from nfselib.webiss.bindings.tipos_complexos import ListaMensagemRetorno

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

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
        },
    )
