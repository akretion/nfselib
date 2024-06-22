from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Contribuinte"


@dataclass
class EnderecoDto:
    class Meta:
        name = "EnderecoDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Contribuinte"

    Bairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Cidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Complemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Estado: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Logradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Pais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    TipoLogradouro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class PessoaDto:
    class Meta:
        name = "PessoaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Contribuinte"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DDD: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Endereco: Optional[EnderecoDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Nome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
