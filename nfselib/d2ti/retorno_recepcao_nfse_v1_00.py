from dataclasses import dataclass, field
from typing import Optional
from nfselib.d2ti.retorno_cancelamento_nfse_v1_00 import (
    Autenticacao,
    Erros,
)

__NAMESPACE__ = "http://www.ctaconsult.com/nfse"


@dataclass
class RetornoNfseLote:
    class Meta:
        name = "retornoNfseLote"
        namespace = "http://www.ctaconsult.com/nfse"

    codigo_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoMunicipio",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )
    protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,9}",
        }
    )
    autenticacao: Optional[Autenticacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    codigo_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoStatus",
            "type": "Element",
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    erros: Optional[Erros] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    numero_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroNota",
            "type": "Element",
        }
    )
    chave_seguranca: Optional[str] = field(
        default=None,
        metadata={
            "name": "chaveSeguranca",
            "type": "Element",
        }
    )
