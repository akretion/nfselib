from dataclasses import dataclass, field
from typing import Optional
from nfselib.issnet.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_url_visualizacao_nfse_serie_envio.xsd"


@dataclass
class ConsultarUrlVisualizacaoNfseSerieEnvio:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_url_visualizacao_nfse_serie_envio.xsd"

    Prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    Numero: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "total_digits": 15,
        }
    )
    CodigoTributacaoMunicipio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    CodigoSerie: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
