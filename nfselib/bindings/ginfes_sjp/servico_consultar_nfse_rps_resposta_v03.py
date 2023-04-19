from dataclasses import dataclass, field
from typing import Optional
from nfselib.bindings.ginfes_sjp.tipos_v03 import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://nfe.sjp.pr.gov.br/servico_consultar_nfse_rps_resposta_v03.xsd"


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://nfe.sjp.pr.gov.br/servico_consultar_nfse_rps_resposta_v03.xsd"

    compNfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        }
    )
    listaMensagemRetorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://nfe.sjp.pr.gov.br/tipos_v03.xsd",
        }
    )
