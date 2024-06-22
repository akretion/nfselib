from dataclasses import dataclass, field
from typing import Optional

from nfselib.dueto.bindings.tipos_complexos import ListaMensagemRetorno

__NAMESPACE__ = (
    "http://tempuri.org/servico_consultar_situacao_lote_rps_resposta.xsd"
)


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_situacao_lote_rps_resposta.xsd"

    NumeroLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
        },
    )
    Situacao: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
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
