from dataclasses import dataclass, field
from typing import Optional
from nfselib.issnet.tipos_complexos import TcIdentificacaoPrestador

__NAMESPACE__ = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_url_visualizacao_nfse_serie_envio.xsd"


@dataclass
class ConsultarUrlVisualizacaoNfseSerieEnvio:
    class Meta:
        namespace = "http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_url_visualizacao_nfse_serie_envio.xsd"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "required": True,
        }
    )
    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "required": True,
            "total_digits": 15,
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    codigo_serie: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoSerie",
            "type": "Element",
            "required": True,
        }
    )
