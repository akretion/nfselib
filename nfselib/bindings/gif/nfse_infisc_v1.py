from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfselib.bindings.gif.nfse_parobe_v1_1 import End
from nfselib.bindings.gif.xmldsig_core_schema_v1_01 import Signature


@dataclass
class Observacoes:
    xinf: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
            "max_length": 100,
        }
    )


class Tuf(Enum):
    """
    Tipo Sigla da UF.
    """
    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"
    EX = "EX"


@dataclass
class Dup:
    class Meta:
        name = "dup"

    nDup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    dVenc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    vDup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    urlBol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        }
    )
    bBol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[1-2]{1}",
        }
    )


@dataclass
class Reemb:
    class Meta:
        name = "reemb"

    nItemReemb: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_inclusive": 999,
        }
    )
    nTit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    cReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 6,
        }
    )
    xReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 120,
        }
    )
    uReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 6,
        }
    )
    qReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vRepass: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vLiquid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    tPagto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        }
    )
    nLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    dPagto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    vDesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class Cobr:
    class Meta:
        name = "cobr"

    dup: List[Dup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 99,
        }
    )


@dataclass
class Emit:
    class Meta:
        name = "emit"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    xFant: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        }
    )
    IM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
        }
    )
    end: Optional[End] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LocalEntrega:
    class Meta:
        name = "localEntrega"

    xLogEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    xComplEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    vNumeroEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
        }
    )
    xBairroEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    xCepEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{8}",
        }
    )
    xCidadeEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    xUFEntr: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PedAnulaNfse:
    class Meta:
        name = "pedAnulaNFSe"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    chvAcessoNFS_e: Optional[str] = field(
        default=None,
        metadata={
            "name": "chvAcessoNFS-e",
            "type": "Element",
            "required": True,
            "max_length": 39,
        }
    )
    motivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PedidoLoteNfsePng:
    class Meta:
        name = "pedidoLoteNFSePNG"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    notaInicial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    notaFinal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    emissaoInicial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    emissaoFinal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    serieNotaFiscal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 3,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
