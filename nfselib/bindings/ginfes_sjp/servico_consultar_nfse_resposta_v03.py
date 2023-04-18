from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.bindings.ginfes_sjp.tipos_v03 import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://nfe.sjp.pr.gov.br/servico_consultar_nfse_resposta_v03.xsd"


@dataclass
class ConsultarNfseResposta:
    class Meta:
        namespace = "http://nfe.sjp.pr.gov.br/servico_consultar_nfse_resposta_v03.xsd"

    ListaNfse: Optional["ConsultarNfseResposta.ListaNfse"] = field(
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

    @dataclass
    class ListaNfse:
        compNfse: List[TcCompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
            }
        )
