from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from nfselib.dsf.bindings.tipos import (
    TpAssincrono,
    TpListaAlertas,
    TpListaErros,
    TpListaNfseRps,
)

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class RetornoEnvioLoteRps:
    """Schema utilizado para RETORNO de Requisição de Envio de lote de RPS.

    Este Schema XML é utilizado pelo Web Service para informar aos
    prestadores de serviços o resultado do pedido de envio de lote de
    RPS.

    :ivar Cabecalho: Cabeçalho do retorno.
    :ivar Alertas: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar Erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    :ivar ChavesNFSeRPS: Chave da NF-e e Chave do RPS que esta
        substitui.
    """

    class Meta:
        name = "RetornoEnvioLoteRPS"
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["RetornoEnvioLoteRps.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Alertas: Optional[TpListaAlertas] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Erros: Optional[TpListaErros] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ChavesNFSeRPS: Optional[TpListaNfseRps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar CodCidade: Código da Cidade
        :ivar Sucesso: Campo indicativo do sucesso do pedido do serviço.
        :ivar NumeroLote: Número de lote.
        :ivar CPFCNPJRemetente: CNPJ do remetente autorizado a
            transmitir a mensagem XML.
        :ivar DataEnvioLote: Data/hora de envio do lote.
        :ivar QtdNotasProcessadas: Quantidade de RPS do lote.
        :ivar TempoProcessamento: Tempo de processamento do lote.
        :ivar ValorTotalServicos: Valor total dos serviços dos RPS
            contidos na mensagem XML.
        :ivar ValorTotalDeducoes: Valor total das deduções dos RPS
            contidos na mensagem XML.
        :ivar Versao: Versão do Schema XML utilizado.
        :ivar Assincrono: Tipo de processamento: N-Processamento
            Sincrono, S-Processamento Assíncrono
        """

        CodCidade: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
            },
        )
        Sucesso: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        NumeroLote: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "max_inclusive": "2147483647",
                "pattern": r"[0-9]{1,12}",
            },
        )
        CPFCNPJRemetente: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            },
        )
        DataEnvioLote: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        QtdNotasProcessadas: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 250,
            },
        )
        TempoProcessamento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,15}",
            },
        )
        ValorTotalServicos: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "total_digits": 15,
                "fraction_digits": 2,
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
            },
        )
        ValorTotalDeducoes: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "total_digits": 15,
                "fraction_digits": 2,
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
            },
        )
        Versao: str = field(
            init=False,
            default="1",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )
        Assincrono: Optional[TpAssincrono] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
