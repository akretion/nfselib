from dataclasses import dataclass, field
from typing import Optional
from nfselib.dueto.tipos_complexos import (
    ListaMensagemRetorno,
    TcCompNfse,
)

__NAMESPACE__ = "http://tempuri.org/servico_consultar_nfse_rps_resposta.xsd"


@dataclass
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = "http://tempuri.org/servico_consultar_nfse_rps_resposta.xsd"

    comp_nfse: Optional[TcCompNfse] = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://tempuri.org/tipos_complexos.xsd",
        }
    )
