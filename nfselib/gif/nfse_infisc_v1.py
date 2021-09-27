from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfselib.gif.xmldsig_core_schema_v1_01 import Signature


@dataclass
class Iss:
    class Meta:
        name = "ISS"

    v_bciss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vBCISS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vISS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_bcstiss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vBCSTISS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_stiss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vSTISS",
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

    p_red_bcst: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRedBCST",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_red_bcst: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRedBCST",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_bcst: Optional[str] = field(
        default=None,
        metadata={
            "name": "vBCST",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    p_issst: Optional[str] = field(
        default=None,
        metadata={
            "name": "pISSST",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_issst: Optional[str] = field(
        default=None,
        metadata={
            "name": "vISSST",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class Id:
    c_nfs_e: Optional[str] = field(
        default=None,
        metadata={
            "name": "cNFS-e",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{0,9}",
        }
    )
    nat_op: Optional[str] = field(
        default=None,
        metadata={
            "name": "natOp",
            "type": "Element",
            "required": True,
            "max_length": 100,
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
    n_nfs_e: Optional[str] = field(
        default=None,
        metadata={
            "name": "nNFS-e",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{0,9}",
        }
    )
    d_emi: Optional[str] = field(
        default=None,
        metadata={
            "name": "dEmi",
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    h_emi: Optional[str] = field(
        default=None,
        metadata={
            "name": "hEmi",
            "type": "Element",
            "required": True,
            "max_length": 5,
        }
    )
    d_sai_ent: Optional[str] = field(
        default=None,
        metadata={
            "name": "dSaiEnt",
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    tp_nf: Optional[int] = field(
        default=None,
        metadata={
            "name": "tpNF",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 1,
        }
    )
    c_mun_fg: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMunFG",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]*",
        }
    )
    ref_nf: Optional[str] = field(
        default=None,
        metadata={
            "name": "refNF",
            "type": "Element",
            "max_length": 39,
        }
    )
    tp_imp: Optional[int] = field(
        default=None,
        metadata={
            "name": "tpImp",
            "type": "Element",
            "min_inclusive": 1,
            "max_inclusive": 2,
        }
    )
    tp_emis: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpEmis",
            "type": "Element",
            "required": True,
            "pattern": r"[NC]{1}",
        }
    )
    anulada: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[SN]{1}",
        }
    )
    notadebito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[SN]{1}",
        }
    )
    mot_anul: Optional[str] = field(
        default=None,
        metadata={
            "name": "motAnul",
            "type": "Element",
            "max_length": 100,
        }
    )
    data_anul: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataAnul",
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    nota_sub: Optional[str] = field(
        default=None,
        metadata={
            "name": "notaSub",
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    serie_sub: Optional[str] = field(
        default=None,
        metadata={
            "name": "serieSub",
            "type": "Element",
            "max_length": 3,
        }
    )
    desc_desconto: Optional[str] = field(
        default=None,
        metadata={
            "name": "descDesconto",
            "type": "Element",
            "max_length": 100,
        }
    )
    desc_cond_esp: Optional[str] = field(
        default=None,
        metadata={
            "name": "descCondEsp",
            "type": "Element",
            "max_length": 100,
        }
    )
    numero_art: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroArt",
            "type": "Element",
            "max_length": 15,
        }
    )
    numero_cei: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroCei",
            "type": "Element",
            "max_length": 15,
        }
    )
    numero_proj: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroProj",
            "type": "Element",
            "max_length": 15,
        }
    )
    numero_matri: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroMatri",
            "type": "Element",
            "max_length": 15,
        }
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
        }
    )


@dataclass
class Ret:
    x_ret_irf: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetIRF",
            "type": "Element",
            "max_length": 60,
        }
    )
    p_ret_irf: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetIRF",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_ret_irf: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetIRF",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_ret_lei10833_pis_pasep: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-PIS-PASEP",
            "type": "Element",
            "max_length": 60,
        }
    )
    p_ret_lei10833_pis_pasep: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-PIS-PASEP",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_ret_lei10833_pis_pasep: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-PIS-PASEP",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_ret_lei10833_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-COFINS",
            "type": "Element",
            "max_length": 60,
        }
    )
    p_ret_lei10833_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-COFINS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_ret_lei10833_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-COFINS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_ret_lei10833_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-CSLL",
            "type": "Element",
            "max_length": 60,
        }
    )
    p_ret_lei10833_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-CSLL",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_ret_lei10833_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-CSLL",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_ret_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetINSS",
            "type": "Element",
            "max_length": 60,
        }
    )
    vt_ret_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtRetINSS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
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

    n_dup: Optional[str] = field(
        default=None,
        metadata={
            "name": "nDup",
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    d_venc: Optional[str] = field(
        default=None,
        metadata={
            "name": "dVenc",
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    v_dup: Optional[str] = field(
        default=None,
        metadata={
            "name": "vDup",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    url_bol: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlBol",
            "type": "Element",
            "max_length": 256,
        }
    )
    b_bol: Optional[str] = field(
        default=None,
        metadata={
            "name": "bBol",
            "type": "Element",
            "pattern": r"[1-2]{1}",
        }
    )


@dataclass
class Fat:
    class Meta:
        name = "fat"

    n_fat: Optional[str] = field(
        default=None,
        metadata={
            "name": "nFat",
            "type": "Element",
            "max_length": 60,
        }
    )
    v_orig: Optional[str] = field(
        default=None,
        metadata={
            "name": "vOrig",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "vDesc",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_liq: Optional[str] = field(
        default=None,
        metadata={
            "name": "vLiq",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class Reemb:
    class Meta:
        name = "reemb"

    n_item_reemb: Optional[int] = field(
        default=None,
        metadata={
            "name": "nItemReemb",
            "type": "Element",
            "max_inclusive": 999,
        }
    )
    n_tit: Optional[str] = field(
        default=None,
        metadata={
            "name": "nTit",
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    c_reemb: Optional[str] = field(
        default=None,
        metadata={
            "name": "cReemb",
            "type": "Element",
            "max_length": 6,
        }
    )
    x_reemb: Optional[str] = field(
        default=None,
        metadata={
            "name": "xReemb",
            "type": "Element",
            "max_length": 120,
        }
    )
    u_reemb: Optional[str] = field(
        default=None,
        metadata={
            "name": "uReemb",
            "type": "Element",
            "max_length": 6,
        }
    )
    q_reemb: Optional[str] = field(
        default=None,
        metadata={
            "name": "qReemb",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_reemb: Optional[str] = field(
        default=None,
        metadata={
            "name": "vReemb",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_repass: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRepass",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_liquid: Optional[str] = field(
        default=None,
        metadata={
            "name": "vLiquid",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    t_pagto: Optional[str] = field(
        default=None,
        metadata={
            "name": "tPagto",
            "type": "Element",
            "max_length": 60,
        }
    )
    n_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "nLote",
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    d_pagto: Optional[str] = field(
        default=None,
        metadata={
            "name": "dPagto",
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    v_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "vDesc",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class Serv:
    class Meta:
        name = "serv"

    c_serv: Optional[str] = field(
        default=None,
        metadata={
            "name": "cServ",
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    x_serv: Optional[str] = field(
        default=None,
        metadata={
            "name": "xServ",
            "type": "Element",
            "required": True,
            "max_length": 120,
        }
    )
    u_trib: Optional[str] = field(
        default=None,
        metadata={
            "name": "uTrib",
            "type": "Element",
            "max_length": 6,
        }
    )
    q_trib: Optional[str] = field(
        default=None,
        metadata={
            "name": "qTrib",
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "vUnit",
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2,3})?",
        }
    )
    v_serv: Optional[str] = field(
        default=None,
        metadata={
            "name": "vServ",
            "type": "Element",
            "required": True,
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "vDesc",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_bciss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vBCISS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    p_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "pISS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vISS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    p_ret_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetINSS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_ret_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetINSS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    p_red: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRed",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_red: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRed",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_ret_irf: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetIRF",
            "type": "Element",
            "max_length": 60,
        }
    )
    p_ret_irf: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetIRF",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_ret_irf: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetIRF",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_ret_lei10833_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-COFINS",
            "type": "Element",
            "max_length": 60,
        }
    )
    p_ret_lei10833_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-COFINS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_ret_lei10833_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-COFINS",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_ret_lei10833_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-CSLL",
            "type": "Element",
            "max_length": 60,
        }
    )
    p_ret_lei10833_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-CSLL",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_ret_lei10833_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-CSLL",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_ret_lei10833_pis_pasep: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRetLei10833-PIS-PASEP",
            "type": "Element",
            "max_length": 60,
        }
    )
    p_ret_lei10833_pis_pasep: Optional[str] = field(
        default=None,
        metadata={
            "name": "pRetLei10833-PIS-PASEP",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    v_ret_lei10833_pis_pasep: Optional[str] = field(
        default=None,
        metadata={
            "name": "vRetLei10833-PIS-PASEP",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    total_aprox_trib_serv: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalAproxTribServ",
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
class Det:
    class Meta:
        name = "det"

    n_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "nItem",
            "type": "Element",
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
    issst: Optional[Issst] = field(
        default=None,
        metadata={
            "name": "ISSST",
            "type": "Element",
        }
    )


@dataclass
class End:
    class Meta:
        name = "end"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
            "max_length": 15,
        }
    )
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "max_length": 100,
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]*",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "required": True,
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "pattern": r"[0-9]{8}",
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
            "type": "Element",
            "max_length": 100,
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{1,13}",
        }
    )
    ie: Optional[str] = field(
        default=None,
        metadata={
            "name": "IE",
            "type": "Element",
            "max_length": 15,
        }
    )
    iest: Optional[str] = field(
        default=None,
        metadata={
            "name": "IEST",
            "type": "Element",
            "max_length": 15,
        }
    )
    imsts: Optional[str] = field(
        default=None,
        metadata={
            "name": "IMSTS",
            "type": "Element",
            "max_length": 15,
        }
    )


@dataclass
class Ender:
    class Meta:
        name = "ender"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
            "max_length": 15,
        }
    )
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "max_length": 100,
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]*",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "required": True,
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "pattern": r"[0-9]{8}",
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
            "type": "Element",
            "max_length": 100,
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"|[0-9]{1,13}",
        }
    )


@dataclass
class LocalEntrega:
    class Meta:
        name = "localEntrega"

    x_log_entr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLogEntr",
            "type": "Element",
            "max_length": 100,
        }
    )
    x_compl_entr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xComplEntr",
            "type": "Element",
            "max_length": 100,
        }
    )
    v_numero_entr: Optional[str] = field(
        default=None,
        metadata={
            "name": "vNumeroEntr",
            "type": "Element",
            "required": True,
            "max_length": 15,
        }
    )
    x_bairro_entr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairroEntr",
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    x_cep_entr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCepEntr",
            "type": "Element",
            "pattern": r"[0-9]{8}",
        }
    )
    x_cidade_entr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCidadeEntr",
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    x_ufentr: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "xUFEntr",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PedAnulaNfse:
    class Meta:
        name = "pedAnulaNFSe"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    chv_acesso_nfs_e: Optional[str] = field(
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
class PedConsultaTrans:
    class Meta:
        name = "pedConsultaTrans"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    chv_acesso_nfs_e: Optional[str] = field(
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

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    c_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "cLote",
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

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    nota_inicial: Optional[str] = field(
        default=None,
        metadata={
            "name": "notaInicial",
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    nota_final: Optional[str] = field(
        default=None,
        metadata={
            "name": "notaFinal",
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    emissao_inicial: Optional[str] = field(
        default=None,
        metadata={
            "name": "emissaoInicial",
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    emissao_final: Optional[str] = field(
        default=None,
        metadata={
            "name": "emissaoFinal",
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    serie_nota_fiscal: Optional[str] = field(
        default=None,
        metadata={
            "name": "serieNotaFiscal",
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
class PedidoLoteNfsePng:
    class Meta:
        name = "pedidoLoteNFSePNG"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    nota_inicial: Optional[str] = field(
        default=None,
        metadata={
            "name": "notaInicial",
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    nota_final: Optional[str] = field(
        default=None,
        metadata={
            "name": "notaFinal",
            "type": "Element",
            "pattern": r"[0-9]{0,9}",
        }
    )
    emissao_inicial: Optional[str] = field(
        default=None,
        metadata={
            "name": "emissaoInicial",
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    emissao_final: Optional[str] = field(
        default=None,
        metadata={
            "name": "emissaoFinal",
            "type": "Element",
            "pattern": r"\d{4}-\d{2}-\d{2}",
        }
    )
    serie_nota_fiscal: Optional[str] = field(
        default=None,
        metadata={
            "name": "serieNotaFiscal",
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

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    chv_acesso_nfs_e: Optional[str] = field(
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

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    c_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "cLote",
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
class Total:
    class Meta:
        name = "total"

    v_reemb: Optional[str] = field(
        default=None,
        metadata={
            "name": "vReemb",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_serv: Optional[str] = field(
        default=None,
        metadata={
            "name": "vServ",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "vDesc",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_outro: Optional[str] = field(
        default=None,
        metadata={
            "name": "vOutro",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vt_nf: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtNF",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vt_liq: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtLiq",
            "type": "Element",
            "min_length": 0,
            "white_space": "preserve",
            "pattern": r"|0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    total_aprox_trib: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalAproxTrib",
            "type": "Element",
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
    fat: Optional[Fat] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    iss: Optional[Iss] = field(
        default=None,
        metadata={
            "name": "ISS",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Transportadora:
    class Meta:
        name = "transportadora"

    x_nome_trans: Optional[str] = field(
        default=None,
        metadata={
            "name": "xNomeTrans",
            "type": "Element",
            "max_length": 100,
        }
    )
    x_cpf_cnpj_trans: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpfCnpjTrans",
            "type": "Element",
            "max_length": 15,
        }
    )
    x_insc_est_trans: Optional[str] = field(
        default=None,
        metadata={
            "name": "xInscEstTrans",
            "type": "Element",
            "max_length": 15,
        }
    )
    x_placa_trans: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPlacaTrans",
            "type": "Element",
            "max_length": 15,
        }
    )
    x_end_trans: Optional[str] = field(
        default=None,
        metadata={
            "name": "xEndTrans",
            "type": "Element",
            "max_length": 100,
        }
    )
    x_mun_trans: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMunTrans",
            "type": "Element",
            "max_length": 60,
        }
    )
    x_uftrans: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "xUFTrans",
            "type": "Element",
        }
    )
    v_tipo_frete_trans: Optional[int] = field(
        default=None,
        metadata={
            "name": "vTipoFreteTrans",
            "type": "Element",
            "min_inclusive": 0,
            "max_inclusive": 1,
        }
    )


@dataclass
class TomS:
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "pattern": r"[0-9]{14}",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "pattern": r"[0-9]{11}",
        }
    )
    x_nome: Optional[str] = field(
        default=None,
        metadata={
            "name": "xNome",
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    ender: Optional[Ender] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    x_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "xEmail",
            "type": "Element",
            "max_length": 120,
        }
    )
    ie: Optional[str] = field(
        default=None,
        metadata={
            "name": "IE",
            "type": "Element",
            "max_length": 15,
        }
    )
    im: Optional[str] = field(
        default=None,
        metadata={
            "name": "IM",
            "type": "Element",
            "max_length": 15,
        }
    )
    imsts: Optional[str] = field(
        default=None,
        metadata={
            "name": "IMSTS",
            "type": "Element",
            "max_length": 15,
        }
    )
    praca: Optional[str] = field(
        default=None,
        metadata={
            "name": "Praca",
            "type": "Element",
            "max_length": 100,
        }
    )


@dataclass
class Emit:
    class Meta:
        name = "emit"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    x_nome: Optional[str] = field(
        default=None,
        metadata={
            "name": "xNome",
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    x_fant: Optional[str] = field(
        default=None,
        metadata={
            "name": "xFant",
            "type": "Element",
            "max_length": 60,
        }
    )
    im: Optional[str] = field(
        default=None,
        metadata={
            "name": "IM",
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
class InfNfse:
    class Meta:
        name = "infNFSe"

    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )
    emit: Optional[Emit] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tom_s: Optional[TomS] = field(
        default=None,
        metadata={
            "name": "TomS",
            "type": "Element",
            "required": True,
        }
    )
    local_entrega: Optional[LocalEntrega] = field(
        default=None,
        metadata={
            "name": "localEntrega",
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
    cobr: List[Cobr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 999,
        }
    )
    inf_adic: List[str] = field(
        default_factory=list,
        metadata={
            "name": "infAdic",
            "type": "Element",
            "max_occurs": 999,
            "max_length": 256,
        }
    )
    observacoes: List[Observacoes] = field(
        default_factory=list,
        metadata={
            "name": "Observacoes",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    reemb: List[Reemb] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 999,
        }
    )
    versao: str = field(
        init=False,
        default="1.00",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class NfsE:
    class Meta:
        name = "NFS-e"

    inf_nfse: Optional[InfNfse] = field(
        default=None,
        metadata={
            "name": "infNFSe",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class EnvioLote:
    class Meta:
        name = "envioLote"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    dh_trans: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhTrans",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\d{4}-\d{2}-\d{2}(\s\d{2}:\d{2}:\d{2})?",
        }
    )
    nfs_e: Optional[NfsE] = field(
        default=None,
        metadata={
            "name": "NFS-e",
            "type": "Element",
            "required": True,
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
