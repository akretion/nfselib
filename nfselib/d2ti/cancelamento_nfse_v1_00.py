from dataclasses import dataclass, field
from typing import Optional
from nfselib.d2ti.retorno_cancelamento_nfse_v1_00 import Autenticacao

__NAMESPACE__ = "http://www.ctaconsult.com/nfse"


@dataclass
class CancelamentoNfseLote:
    class Meta:
        name = "cancelamentoNfseLote"
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
    dt_emissao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dtEmissao",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",
        }
    )
    autenticacao: Optional[Autenticacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    numero_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroNota",
            "type": "Element",
            "required": True,
        }
    )
    chave_seguranca: Optional[str] = field(
        default=None,
        metadata={
            "name": "chaveSeguranca",
            "type": "Element",
            "required": True,
        }
    )
