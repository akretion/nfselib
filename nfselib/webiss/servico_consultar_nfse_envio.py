from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nfselib.webiss.tipos_complexos import (
    TcIdentificacaoIntermediarioServico,
    TcIdentificacaoPrestador,
    TcIdentificacaoTomador,
)

__NAMESPACE__ = "http://www.abrasf.org.br/nfse"


@dataclass
class ConsultarNfseEnvio:
    class Meta:
        namespace = "http://www.abrasf.org.br/nfse"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    numero_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "total_digits": 15,
        }
    )
    periodo_emissao: Optional["ConsultarNfseEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "PeriodoEmissao",
            "type": "Element",
        }
    )
    tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
        }
    )

    @dataclass
    class PeriodoEmissao:
        data_inicial: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataInicial",
                "type": "Element",
                "required": True,
            }
        )
        data_final: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DataFinal",
                "type": "Element",
                "required": True,
            }
        )
