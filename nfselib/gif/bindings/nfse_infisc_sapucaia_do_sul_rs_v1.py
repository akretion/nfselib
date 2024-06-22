from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.gif.bindings.nfse_infisc_v1 import (
    End,
    Fat,
)
from nfselib.gif.bindings.xmldsig_core_schema_v1_01 import Signature


@dataclass
class DadosDaObra:
    class Meta:
        name = "dadosDaObra"

    xLogObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    xComplObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    vNumeroObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    xBairroObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    xCepObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{8}",
        },
    )
    cCidadeObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]*",
        },
    )
    xCidadeObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 60,
        },
    )
    xUfObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 2,
        },
    )
    cPaisObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1,4}",
        },
    )
    xPaisObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    numeroArt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 12,
        },
    )
    numeroCei: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 12,
        },
    )
    numeroProj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    numeroMatri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )


@dataclass
class ConfirmaLote:
    class Meta:
        name = "confirmaLote"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    dhRecbto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\d{4}-\d{2}-\d{2}(\s\d{2}:\d{2}:\d{2})?",
        },
    )
    sit: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_inclusive": 999,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    versao: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Faturas:
    class Meta:
        name = "faturas"

    fat: List[Fat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )


@dataclass
class PedCancelaNfse:
    class Meta:
        name = "pedCancelaNFSe"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    chvAcessoNFS_e: Optional[str] = field(
        default=None,
        metadata={
            "name": "chvAcessoNFS-e",
            "type": "Element",
            "required": True,
            "max_length": 39,
        },
    )
    motivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1}",
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    versao: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PedidoNfsePng:
    class Meta:
        name = "pedidoNFSePNG"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    chvAcessoNFS_e: Optional[str] = field(
        default=None,
        metadata={
            "name": "chvAcessoNFS-e",
            "type": "Element",
            "required": True,
            "max_length": 39,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    versao: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Prest:
    class Meta:
        name = "prest"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 150,
        },
    )
    xFant: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        },
    )
    IM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
        },
    )
    xEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        },
    )
    xSite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        },
    )
    end: Optional[End] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{1,13}",
        },
    )
    fone2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{1,13}",
        },
    )
    IE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    regimeTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1}",
        },
    )
