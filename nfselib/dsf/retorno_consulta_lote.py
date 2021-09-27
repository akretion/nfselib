from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import XmlDateTime
from nfselib.dsf.tipos import (
    Nulo,
    TpListaAlertas,
    TpListaErros,
    TpListaNfse,
)

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class RetornoConsultaLote:
    """Schema utilizado para RETORNO de consulta de lote de RPS.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços o resultado da consulta de lote de RPS.

    :ivar cabecalho: Cabeçalho do retorno.
    :ivar alertas: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    :ivar lista_nfse: Lista de retorno para consulta de NFSe.
    """
    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["RetornoConsultaLote.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    alertas: Optional[TpListaAlertas] = field(
        default=None,
        metadata={
            "name": "Alertas",
            "type": "Element",
            "namespace": "",
        }
    )
    erros: Optional[TpListaErros] = field(
        default=None,
        metadata={
            "name": "Erros",
            "type": "Element",
            "namespace": "",
        }
    )
    lista_nfse: Optional[TpListaNfse] = field(
        default=None,
        metadata={
            "name": "ListaNFSe",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar cod_cidade: Código da Cidade
        :ivar sucesso: Campo indicativo do sucesso do pedido do serviço.
        :ivar numero_lote: Número de lote.
        :ivar cpfcnpjremetente: CNPJ do remetente autorizado a
            transmitir a mensagem XML.
        :ivar razao_social_remetente: Razão Social do remetente
            autorizado a transmitir a mensagem XML.
        :ivar data_envio_lote: Data/hora de envio do lote.
        :ivar qtd_notas_processadas: Quantidade de RPS do lote.
        :ivar tempo_processamento: Tempo de processamento do lote.
        :ivar valor_total_servicos: Valor total dos serviços dos RPS
            contidos na mensagem XML.
        :ivar valor_total_deducoes: Valor total das deduções dos RPS
            contidos na mensagem XML.
        :ivar versao: Versão do Schema XML utilizado.
        """
        cod_cidade: Optional[int] = field(
            default=None,
            metadata={
                "name": "CodCidade",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
            }
        )
        sucesso: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Sucesso",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        numero_lote: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroLote",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "max_inclusive": "2147483647",
                "pattern": r"[0-9]{1,12}",
            }
        )
        cpfcnpjremetente: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPFCNPJRemetente",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            }
        )
        razao_social_remetente: Optional[str] = field(
            default=None,
            metadata={
                "name": "RazaoSocialRemetente",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        data_envio_lote: Optional[Union[XmlDateTime, Nulo]] = field(
            default=None,
            metadata={
                "name": "DataEnvioLote",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        qtd_notas_processadas: Optional[int] = field(
            default=None,
            metadata={
                "name": "QtdNotasProcessadas",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 250,
            }
        )
        tempo_processamento: Optional[str] = field(
            default=None,
            metadata={
                "name": "TempoProcessamento",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,15}",
            }
        )
        valor_total_servicos: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValorTotalServicos",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "total_digits": 15,
                "fraction_digits": 2,
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
            }
        )
        valor_total_deducoes: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValorTotalDeducoes",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "total_digits": 15,
                "fraction_digits": 2,
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
            }
        )
        versao: str = field(
            init=False,
            default="1",
            metadata={
                "name": "Versao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )
