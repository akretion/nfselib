from dataclasses import dataclass, field
from typing import Optional

from nfselib.dsf.bindings.tipos import (
    TpListaAlertas,
    TpListaErros,
    TpListaNfseConsultaNota,
)

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class RetornoConsultaNfseRps:
    """Schema utilizado para Retrono de consulta de notas.

    Este Schema XML é utilizado pelos prestadores de serviços o retorno
    da consulta de Notas fiscais emitidas por RPS.

    :ivar Cabecalho: Cabeçalho da Consulta.
    :ivar NotasConsultadas: Informe os RPS a serem consultados por NF-e.
    :ivar Alertas: Elemento que representa a ocorrência de eventos de
        alertas o durante o processamento da mensagem XML.
    :ivar Erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """

    class Meta:
        name = "RetornoConsultaNFSeRPS"
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["RetornoConsultaNfseRps.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    NotasConsultadas: Optional[TpListaNfseConsultaNota] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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

    @dataclass
    class Cabecalho:
        """
        :ivar CodCidade: Informe o Codigo da Cidade.
        :ivar CPFCNPJRemetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar transacao: Informe se as NF-e a serem consultadas farão
            parte de uma mesma transação. Informe sempre True.
        :ivar Versao: Informe a Versão do Schema XML utilizado.
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
        CPFCNPJRemetente: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{11}|[0-9]{14}",
            },
        )
        transacao: bool = field(
            default=True,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
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
