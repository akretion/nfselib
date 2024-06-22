from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"


@dataclass
class ConsultarLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    header: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarLoteRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfse:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    header: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    header: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfsePorRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarNfseResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSituacaoLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    header: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ConsultarSituacaoLoteRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRps:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    header: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class RecepcionarLoteRpsResponse:
    class Meta:
        namespace = "http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd"

    return_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "return",
            "type": "Element",
            "namespace": "",
        },
    )
