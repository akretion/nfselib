from dataclasses import dataclass, field
from typing import Optional
from nfselib.bindings.ginfes_sjp.tipos_v03 import (
    ListaMensagemRetorno,
    TcCancelamentoNfse,
)

__NAMESPACE__ = "http://nfe.sjp.pr.gov.br/servico_cancelar_nfse_resposta_v03.xsd"


@dataclass
class CancelarNfseResposta:
    class Meta:
        namespace = "http://nfe.sjp.pr.gov.br/servico_cancelar_nfse_resposta_v03.xsd"

    Cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
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
