from dataclasses import dataclass, field
from typing import Optional
from nfselib.dsf.tipos import (
    TpListaAlertas,
    TpListaErros,
)

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class RetornoConsultaSeqRps:
    """
    Schema utilizado para RETORNO da Consulta Sequêncial de RPS.

    :ivar cabecalho: Cabeçalho do retorno.
    :ivar alertas: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """
    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["RetornoConsultaSeqRps.Cabecalho"] = field(
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

    @dataclass
    class Cabecalho:
        """
        :ivar cod_cid: Código da Cidade
        :ivar cpfcnpjremetente: CNPJ do remetente autorizado a
            transmitir a mensagem XML.
        :ivar imprestador: Inscrição Municipal do Prestador.
        :ivar nro_ultimo_rps: Informe o Número do RPS emitido.
        :ivar serie_prestacao:
        :ivar versao: Versão do Schema XML utilizado.
        """
        cod_cid: Optional[int] = field(
            default=None,
            metadata={
                "name": "CodCid",
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
        imprestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "IMPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{6,11}",
            }
        )
        nro_ultimo_rps: Optional[str] = field(
            default=None,
            metadata={
                "name": "NroUltimoRps",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "max_inclusive": "2147483647",
                "pattern": r"[0-9]{1,12}",
            }
        )
        serie_prestacao: Optional[int] = field(
            default=None,
            metadata={
                "name": "SeriePrestacao",
                "type": "Element",
                "namespace": "",
                "min_inclusive": 1,
                "max_inclusive": 99,
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
