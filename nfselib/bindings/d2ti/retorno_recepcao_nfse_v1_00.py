from dataclasses import dataclass, field
from typing import Optional

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
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,9}",
        }
    )


@dataclass
class ChaveSeguranca:
    class Meta:
        name = "chaveSeguranca"
        namespace = "http://www.ctaconsult.com/nfse"


@dataclass
class Codigo:
    class Meta:
        name = "codigo"
        namespace = "http://www.ctaconsult.com/nfse"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
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

    codigo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,9}",
        }
    )


@dataclass
class Erros:
    class Meta:
        name = "erros"
        namespace = "http://www.ctaconsult.com/nfse"

    erro: Optional[Erro] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RetornoNfseLote:
    class Meta:
        name = "retornoNfseLote"
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
        }
    )
    chaveSeguranca: Optional[ChaveSeguranca] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
