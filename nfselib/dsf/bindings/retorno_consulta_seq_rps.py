from dataclasses import dataclass, field
from typing import Optional

from nfselib.dsf.bindings.tipos import (
    TpListaAlertas,
    TpListaErros,
)

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class RetornoConsultaSeqRps:
    """
    Schema utilizado para RETORNO da Consulta Sequêncial de RPS.

    :ivar Cabecalho: Cabeçalho do retorno.
    :ivar Alertas: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar Erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """

    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["RetornoConsultaSeqRps.Cabecalho"] = field(
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

    @dataclass
    class Cabecalho:
        """
        :ivar CodCid: Código da Cidade
        :ivar CPFCNPJRemetente: CNPJ do remetente autorizado a
            transmitir a mensagem XML.
        :ivar IMPrestador: Inscrição Municipal do Prestador.
        :ivar NroUltimoRps: Informe o Número do RPS emitido.
        :ivar SeriePrestacao:
        :ivar Versao: Versão do Schema XML utilizado.
        """

        CodCid: Optional[int] = field(
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
        IMPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{6,11}",
            },
        )
        NroUltimoRps: Optional[str] = field(
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
        SeriePrestacao: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_inclusive": 1,
                "max_inclusive": 99,
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
