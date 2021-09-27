from dataclasses import dataclass, field
from typing import Optional
from nfselib.dsf.tipos import (
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

    :ivar cabecalho: Cabeçalho da Consulta.
    :ivar notas_consultadas: Informe os RPS a serem consultados por
        NF-e.
    :ivar alertas: Elemento que representa a ocorrência de eventos de
        alertas o durante o processamento da mensagem XML.
    :ivar erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """
    class Meta:
        name = "RetornoConsultaNFSeRPS"
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["RetornoConsultaNfseRps.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    notas_consultadas: Optional[TpListaNfseConsultaNota] = field(
        default=None,
        metadata={
            "name": "NotasConsultadas",
            "type": "Element",
            "namespace": "",
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

    @dataclass
    class Cabecalho:
        """
        :ivar cod_cidade: Informe o Codigo da Cidade.
        :ivar cpfcnpjremetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar transacao: Informe se as NF-e a serem consultadas farão
            parte de uma mesma transação. Informe sempre True.
        :ivar versao: Informe a Versão do Schema XML utilizado.
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
        transacao: bool = field(
            default=True,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
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
