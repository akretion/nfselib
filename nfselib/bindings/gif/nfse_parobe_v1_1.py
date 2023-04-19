from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.bindings.gif.xmldsig_core_schema_v1_01 import Signature


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
        }
    )
    vISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vBCSTISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vSTISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class Issst:
    class Meta:
        name = "ISSST"

    vBCST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    pISSST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    vISSST: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class id:
    class Meta:
        name = "Id"

    cNFS_e: Optional[int] = field(
        default=None,
        metadata={
            "name": "cNFS-e",
            "type": "Element",
            "required": True,
            "max_inclusive": 999999999,
        }
    )
    mod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 3,
        }
    )
    nNFS_e: Optional[str] = field(
        default=None,
        metadata={
            "name": "nNFS-e",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{0,9}",
        }
    )
    dEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    hEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\d{2}:\d{2}",
        }
    )
    tpNF: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 1,
        }
    )
    refNF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 39,
        }
    )
    tpImp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": 1,
            "max_inclusive": 1,
        }
    )
    tpEmis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[NC]{1}",
        }
    )
    cancelada: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[SN]{1}",
        }
    )
    motCanc: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 999,
            "pattern": r"[0-9]{1}",
        }
    )
    dataCanc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    notaSub: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    canhoto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{1}",
        }
    )


@dataclass
class Ret:
    vRetIR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vRetPISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vRetCOFINS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vRetCSLL: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vRetINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


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
        }
    )
    xComplObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    vNumeroObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
    )
    xBairroObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    xCepObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{8}",
        }
    )
    cCidadeObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{7}",
        }
    )
    xCidadeObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    xUfObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 2,
        }
    )
    cPaisObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        }
    )
    xPaisObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    numeroArt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 12,
        }
    )
    numeroCei: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 12,
        }
    )
    numeroProj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
    )
    numeroMatri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
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
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 6,
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    UF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 2,
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{8}",
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )


@dataclass
class Ender:
    class Meta:
        name = "ender"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 6,
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        }
    )
    UF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 2,
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{8}",
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{1,5}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )


@dataclass
class Fat:
    class Meta:
        name = "fat"

    nItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_inclusive": 999,
        }
    )
    nFat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 12,
        }
    )
    dVenc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    vFat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    tipoVencFat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{1}",
        }
    )
    descTipoVencFat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
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
        }
    )
    cLCServ: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_inclusive": 9999,
        }
    )
    xServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        }
    )
    localTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{7}",
        }
    )
    localVerifResServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{1}",
        }
    )
    uTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 2,
        }
    )
    qTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vUnit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
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
    vBCISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    pISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    vISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vBCINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    pRetINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vRetINSS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vRed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vBCRetIR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    pRetIR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    vRetIR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vBCCOFINS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    pRetCOFINS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    vRetCOFINS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vBCCSLL: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    pRetCSLL: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    vRetCSLL: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vBCPISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    pRetPISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    vRetPISPASEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class Transportadora:
    class Meta:
        name = "transportadora"

    xNomeTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    xCpfCnpjTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
    )
    xInscEstTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
    )
    xPlacaTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[a-zA-Z]{2,4}[0-9]{3,4}",
        }
    )
    xEndTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    cMunTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{7}",
        }
    )
    xMunTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 60,
        }
    )
    xUfTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 2,
        }
    )
    cPaisTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{1,5}",
        }
    )
    xPaisTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    vTipoFreteTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{1}",
        }
    )


@dataclass
class TomS:
    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[0-9]{11}",
        }
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 100,
        }
    )
    ender: Optional[Ender] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    xEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 120,
        }
    )
    IE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
    )
    IM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
    )
    IME: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{10,15}",
        }
    )
    fone2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{10,15}",
        }
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
        }
    )
    dhRecbto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\d{4}-\d{2}-\d{2}(\s\d{2}:\d{2}:\d{2})?",
        }
    )
    sit: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_inclusive": 999,
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
class Det:
    class Meta:
        name = "det"

    nItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_inclusive": 999,
        }
    )
    serv: Optional[Serv] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ISSST: Optional[Issst] = field(
        default=None,
        metadata={
            "type": "Element",
        }
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
        }
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
            "required": True,
            "pattern": r"[0-9]{1}",
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
class PedConsultaTrans:
    class Meta:
        name = "pedConsultaTrans"

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
class PedidoCancelamentoLote:
    class Meta:
        name = "pedidoCancelamentoLote"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    cLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
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
class PedidoLoteNfse:
    class Meta:
        name = "pedidoLoteNFSe"

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
class PedidoNfsePng:
    class Meta:
        name = "pedidoNFSePNG"

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
class PedidoStatusLote:
    class Meta:
        name = "pedidoStatusLote"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    cLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
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
class Prest:
    class Meta:
        name = "prest"

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
            "max_length": 150,
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
    xEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        }
    )
    xSite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        }
    )
    end: Optional[End] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{10,15}",
        }
    )
    fone2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{10,15}",
        }
    )
    IE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 15,
        }
    )
    regimeTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1}",
        }
    )


@dataclass
class Total:
    class Meta:
        name = "total"

    vServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
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
    vtNF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vtLiq: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    ret: Optional[Ret] = field(
        default=None,
        metadata={
            "name": "Ret",
            "type": "Element",
        }
    )
    vtLiqFaturas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    ISS: Optional[Iss] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
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
        }
    )
    prest: Optional[Prest] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tomS: Optional[TomS] = field(
        default=None,
        metadata={
            "name": "TomS",
            "type": "Element",
            "required": True,
        }
    )
    dadosDaObra: Optional[DadosDaObra] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    transportadora: Optional[Transportadora] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    det: List[Det] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    total: Optional[Total] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    faturas: Optional[Faturas] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    infAdicLT: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{7}",
        }
    )
    infAdicES: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[SN]{1}",
        }
    )
    infAdic: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 999,
            "max_length": 256,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
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
        }
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
        }
    )
    dhTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\d{4}-\d{2}-\d{2}(\s\d{2}:\d{2}:\d{2})?",
        }
    )
    NFS_e: List[NfsE] = field(
        default_factory=list,
        metadata={
            "name": "NFS-e",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 500,
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
