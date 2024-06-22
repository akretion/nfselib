from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.tiplan.bindings.tipos_nfse_v01 import (
    CompNfse,
    ListaMensagemRetorno,
    TcRps,
)

__NAMESPACE__ = "http://www.nfe.com.br/WSNacional/XSD/1/nfse_municipal_v01.xsd"


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = (
            "http://www.nfe.com.br/WSNacional/XSD/1/nfse_municipal_v01.xsd"
        )

    Rps: Optional[TcRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = (
            "http://www.nfe.com.br/WSNacional/XSD/1/nfse_municipal_v01.xsd"
        )

    compNfse: Optional[CompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
            "required": True,
        },
    )
    listaMensagemRetorno: List[ListaMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
