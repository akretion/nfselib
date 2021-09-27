from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.gif.nfse_infisc_v1 import (
    End,
    Fat,
)
from nfselib.gif.xmldsig_core_schema_v1_01 import Signature


@dataclass
class DadosDaObra:
    class Meta:
        name = "dadosDaObra"

    x_log_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLogObra",
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    x_compl_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "xComplObra",
            "type": "Element",
            "max_length": 100,
        }
    )
    v_numero_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "vNumeroObra",
            "type": "Element",
            "max_length": 15,
        }
    )
    x_bairro_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairroObra",
            "type": "Element",
            "max_length": 100,
        }
    )
    x_cep_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCepObra",
            "type": "Element",
            "pattern": r"[0-9]{8}",
        }
    )
    c_cidade_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "cCidadeObra",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]*",
        }
    )
    x_cidade_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCidadeObra",
            "type": "Element",
            "required": True,
            "max_length": 60,
        }
    )
    x_uf_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "xUfObra",
            "type": "Element",
            "required": True,
            "max_length": 2,
        }
    )
    c_pais_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPaisObra",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPaisObra",
            "type": "Element",
            "required": True,
            "max_length": 100,
        }
    )
    numero_art: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroArt",
            "type": "Element",
            "max_length": 12,
        }
    )
    numero_cei: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroCei",
            "type": "Element",
            "max_length": 12,
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
class ConfirmaLote:
    class Meta:
        name = "confirmaLote"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    dh_recbto: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhRecbto",
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
class PedidoNfsePng:
    class Meta:
        name = "pedidoNFSePNG"

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
class Prest:
    class Meta:
        name = "prest"

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
            "max_length": 150,
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
    x_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "xEmail",
            "type": "Element",
            "max_length": 50,
        }
    )
    x_site: Optional[str] = field(
        default=None,
        metadata={
            "name": "xSite",
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
            "pattern": r"|[0-9]{1,13}",
        }
    )
    fone2: Optional[str] = field(
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
    regime_trib: Optional[str] = field(
        default=None,
        metadata={
            "name": "regimeTrib",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1}",
        }
    )
