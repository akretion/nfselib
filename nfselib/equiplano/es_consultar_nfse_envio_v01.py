from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from nfselib.equiplano.tipos_esnfs_v01 import (
    TcIdentificacaoPrestador,
    TcIdentificacaoTomador,
)
from nfselib.equiplano.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs"


@dataclass
class EsConsultarNfseEnvio:
    class Meta:
        name = "esConsultarNfseEnvio"
        namespace = "http://www.equiplano.com.br/esnfs"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrNfse",
            "type": "Element",
            "namespace": "",
        }
    )
    periodo_emissao: Optional["EsConsultarNfseEnvio.PeriodoEmissao"] = field(
        default=None,
        metadata={
            "name": "periodoEmissao",
            "type": "Element",
            "namespace": "",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )

    @dataclass
    class PeriodoEmissao:
        dt_inicial: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "dtInicial",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        dt_final: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "dtFinal",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        tomador: Optional[TcIdentificacaoTomador] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
