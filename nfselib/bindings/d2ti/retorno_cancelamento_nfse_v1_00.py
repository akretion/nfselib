from dataclasses import dataclass, field
from typing import Optional
from nfselib.d2ti.retorno_recepcao_nfse_v1_00 import (
    Autenticacao,
    ChaveSeguranca,
    Erros,
    NumeroNota,
)

__NAMESPACE__ = "http://www.ctaconsult.com/nfse"


@dataclass
class RetornoCancelamentoNfseLote:
    class Meta:
        name = "retornoCancelamentoNfseLote"
        namespace = "http://www.ctaconsult.com/nfse"

    codigoMunicipio: Optional[str] = field(
        default=None,
        metadata={
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
    codigoStatus: Optional[str] = field(
        default=None,
        metadata={
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
    numeroNota: Optional[NumeroNota] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    chaveSeguranca: Optional[ChaveSeguranca] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
