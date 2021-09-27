from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.tiplan.tipos_nfse_v01 import (
    CompNfse,
    ListaMensagemRetorno,
    TcRps,
)

__NAMESPACE__ = "http://www.nfe.com.br/WSNacional/XSD/1/nfse_municipal_v01.xsd"


@dataclass
class GerarNfseEnvio:
    class Meta:
        namespace = "http://www.nfe.com.br/WSNacional/XSD/1/nfse_municipal_v01.xsd"

    rps: Optional[TcRps] = field(
        default=None,
        metadata={
            "name": "Rps",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GerarNfseResposta:
    class Meta:
        namespace = "http://www.nfe.com.br/WSNacional/XSD/1/nfse_municipal_v01.xsd"

    comp_nfse: Optional[CompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: List[ListaMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "max_occurs": 2,
        }
    )
