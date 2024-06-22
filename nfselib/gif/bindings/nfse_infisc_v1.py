from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from nfselib.gif.bindings.xmldsig_core_schema_v1_01 import Signature


@dataclass
class Iss:
    class Meta:
        name = "ISS"

    vBCISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vBCSTISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vSTISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )


@dataclass
class Issst:
    class Meta:
        name = "ISSST"

    pRedBCST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRedBCST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vBCST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    pISSST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vISSST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )


@dataclass
class id:
    class Meta:
        name = "Id"

    cNFS_e: Optional[str] = field(
        default=None,
        metadata={
            "name": "cNFS-e",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{0,9}",
        },
    )
    natOp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    mod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        },
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 3,
        },
    )
    nNFS_e: Optional[str] = field(
        default=None,
        metadata={
            "name": "nNFS-e",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{0,9}",
        },
    )
    dEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    hEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 5,
        },
    )
    dSaiEnt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    tpNF: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 1,
        },
    )
    cMunFG: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]*",
        },
    )
    refNF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 39,
        },
    )
    tpImp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    tpEmis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[NC]{1}",
        },
    )
    anulada: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[SN]{1}",
        },
    )
    notadebito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[SN]{1}",
        },
    )
    motAnul: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    dataAnul: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    notaSub: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        },
    )
    serieSub: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 3,
        },
    )
    descDesconto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    descCondEsp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    numeroArt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    numeroCei: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
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
class Observacoes:
    xinf: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
            "max_length": 100,
        },
    )


@dataclass
class Ret:
    xRetIRF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        },
    )
    pRetIRF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRetIRF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    xRetLei10833PISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-PIS-PASEP",
            "type": "Element",
            "max_length": 60,
        },
    )
    pRetLei10833PISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-PIS-PASEP",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRetLei10833PISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-PIS-PASEP",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    xRetLei10833COFINS: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-COFINS",
            "type": "Element",
            "max_length": 60,
        },
    )
    pRetLei10833COFINS: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-COFINS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRetLei10833COFINS: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-COFINS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    xRetLei10833CSLL: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-CSLL",
            "type": "Element",
            "max_length": 60,
        },
    )
    pRetLei10833CSLL: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-CSLL",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRetLei10833CSLL: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-CSLL",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    xRetINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        },
    )
    vtRetINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
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
        },
    )
    dVenc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    vDup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    urlBol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )
    bBol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[1-2]{1}",
        },
    )


@dataclass
class Fat:
    class Meta:
        name = "fat"

    nFat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        },
    )
    vOrig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vDesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vLiq: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
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
        },
    )
    nTit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        },
    )
    cReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 6,
        },
    )
    xReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 120,
        },
    )
    uReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 6,
        },
    )
    qReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vRepass: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vLiquid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    tPagto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        },
    )
    nLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        },
    )
    dPagto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    vDesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )


@dataclass
class Serv:
    class Meta:
        name = "serv"

    cServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 60,
        },
    )
    xServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 120,
        },
    )
    uTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 6,
        },
    )
    qTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vUnit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2,3})?",
        },
    )
    vServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vDesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vBCISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    pISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    pRetINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vRetINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    pRed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    xRetIRF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        },
    )
    pRetIRF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRetIRF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    xRetLei10833COFINS: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-COFINS",
            "type": "Element",
            "max_length": 60,
        },
    )
    pRetLei10833COFINS: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-COFINS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRetLei10833COFINS: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-COFINS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    xRetLei10833CSLL: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-CSLL",
            "type": "Element",
            "max_length": 60,
        },
    )
    pRetLei10833CSLL: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-CSLL",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRetLei10833CSLL: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-CSLL",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    xRetLei10833PISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-PIS-PASEP",
            "type": "Element",
            "max_length": 60,
        },
    )
    pRetLei10833PISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-PIS-PASEP",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )
    vRetLei10833PISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-PIS-PASEP",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    totalAproxTribServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
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
        },
    )


@dataclass
class Det:
    class Meta:
        name = "det"

    nItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_inclusive": 999,
        },
    )
    serv: Optional[Serv] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ISSST: Optional[Issst] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class End:
    class Meta:
        name = "end"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
        },
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]*",
        },
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 60,
        },
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{8}",
        },
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{1,4}",
        },
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    fone: Optional[str] = field(
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
    IEST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    IMSTS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )


@dataclass
class Ender:
    class Meta:
        name = "ender"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
        },
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]*",
        },
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 60,
        },
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{8}",
        },
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{1,4}",
        },
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{1,13}",
        },
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
        },
    )
    xComplEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    vNumeroEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
        },
    )
    xBairroEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    xCepEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{8}",
        },
    )
    xCidadeEntr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 60,
        },
    )
    xUFEntr: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
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
            "max_length": 100,
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
class PedConsultaTrans:
    class Meta:
        name = "pedConsultaTrans"

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
class PedidoCancelamentoLote:
    class Meta:
        name = "pedidoCancelamentoLote"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    cLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
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
class PedidoLoteNfse:
    class Meta:
        name = "pedidoLoteNFSe"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    notaInicial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        },
    )
    notaFinal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        },
    )
    emissaoInicial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    emissaoFinal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    serieNotaFiscal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 3,
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
class PedidoLoteNfsePng:
    class Meta:
        name = "pedidoLoteNFSePNG"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    notaInicial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        },
    )
    notaFinal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        },
    )
    emissaoInicial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    emissaoFinal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        },
    )
    serieNotaFiscal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 3,
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
class PedidoNfse:
    class Meta:
        name = "pedidoNFSe"

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
class PedidoStatusLote:
    class Meta:
        name = "pedidoStatusLote"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    cLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
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
class Total:
    class Meta:
        name = "total"

    vReemb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vDesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vOutro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vtNF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    vtLiq: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    totalAproxTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    ret: Optional[Ret] = field(
        default=None,
        metadata={
            "name": "Ret",
            "type": "Element",
        },
    )
    fat: Optional[Fat] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ISS: Optional[Iss] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Transportadora:
    class Meta:
        name = "transportadora"

    xNomeTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    xCpfCnpjTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    xInscEstTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    xPlacaTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    xEndTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
    )
    xMunTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        },
    )
    xUFTrans: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vTipoFreteTrans: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": 0,
            "max_inclusive": 1,
        },
    )


@dataclass
class TomS:
    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{14}",
        },
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{11}",
        },
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        },
    )
    ender: Optional[Ender] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    xEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 120,
        },
    )
    IE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    IM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    IMSTS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        },
    )
    Praca: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        },
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
        },
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
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
    end: Optional[End] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class InfNfse:
    class Meta:
        name = "infNFSe"

    Id: Optional[id] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    emit: Optional[Emit] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    tomS: Optional[TomS] = field(
        default=None,
        metadata={
            "name": "TomS",
            "type": "Element",
            "required": True,
        },
    )
    localEntrega: Optional[LocalEntrega] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    transportadora: Optional[Transportadora] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    det: List[Det] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    total: Optional[Total] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    cobr: List[Cobr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 999,
        },
    )
    infAdic: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 999,
            "max_length": 256,
        },
    )
    Observacoes: List[Observacoes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 999,
        },
    )
    reemb: List[Reemb] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 999,
        },
    )
    versao: str = field(
        init=False,
        default="1.00",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class NfsE:
    class Meta:
        name = "NFS-e"

    infNFSe: Optional[InfNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EnvioLote:
    class Meta:
        name = "envioLote"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    dhTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\d{4}-\d{2}-\d{2}(\s\d{2}:\d{2}:\d{2})?",
        },
    )
    NFS_e: Optional[NfsE] = field(
        default=None,
        metadata={
            "name": "NFS-e",
            "type": "Element",
            "required": True,
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
