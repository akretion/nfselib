from dataclasses import dataclass, field
from typing import Optional
from nfselib.webiss.tipos_complexos import ListaMensagemRetorno

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class ConsultarSituacaoLoteRpsResposta:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        }
    )
    situacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Situacao",
            "type": "Element",
            "pattern": r"1|2|3|4",
        }
    )
    lista_mensagem_retorno: Optional[ListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
        }
    )
