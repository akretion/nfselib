from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.ctaconsult.com/nfse"


@dataclass
class Autenticacao:
    class Meta:
        name = "autenticacao"
        namespace = "http://www.ctaconsult.com/nfse"

    token: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChaveSeguranca:
    class Meta:
        name = "chaveSeguranca"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Codigo:
    class Meta:
        name = "codigo"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )


@dataclass
class CodigoMunicipio:
    class Meta:
        name = "codigoMunicipio"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )


@dataclass
class CodigoStatus:
    class Meta:
        name = "codigoStatus"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )


@dataclass
class Descricao:
    class Meta:
        name = "descricao"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Erro:
    class Meta:
        name = "erro"
        namespace = "http://www.ctaconsult.com/nfse"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    descricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class NumeroNota:
    class Meta:
        name = "numeroNota"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Protocolo:
    class Meta:
        name = "protocolo"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,9}",
        }
    )


@dataclass
class Token:
    class Meta:
        name = "token"
        namespace = "http://www.ctaconsult.com/nfse"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Erros:
    class Meta:
        name = "erros"
        namespace = "http://www.ctaconsult.com/nfse"

    erro: List[Erro] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class RetornoCancelamentoNfseLote:
    class Meta:
        name = "retornoCancelamentoNfseLote"
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
