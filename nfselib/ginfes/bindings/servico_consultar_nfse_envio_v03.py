from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from nfselib.ginfes.bindings.tipos_v03 import (
    TcIdentificacaoIntermediarioServico,
    TcIdentificacaoPrestador,
    TcIdentificacaoTomador,
)
from nfselib.ginfes.bindings.xmldsig_core_schema_v02 import Signature

__NAMESPACE__ = "http://www.ginfes.com.br/servico_consultar_nfse_envio_v03.xsd"


@dataclass
class ConsultarNfseEnvio:
    class Meta:
        namespace = (
            "http://www.ginfes.com.br/servico_consultar_nfse_envio_v03.xsd"
        )

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "total_digits": 15,
            "white_space": "collapse",
        },
    )
    PeriodoEmissao: Optional["ConsultarNfseEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    IntermediarioServico: Optional[TcIdentificacaoIntermediarioServico] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )

    @dataclass
    class PeriodoEmissao:
        DataInicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        DataFinal: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
