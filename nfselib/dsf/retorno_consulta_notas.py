from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nfselib.dsf.tipos import (
    TpListaErros,
    TpListaNfseConsultaNota,
)

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class RetornoConsultaNotas:
    """Schema utilizado para Retrono de consulta de notas.

    Este Schema XML é utilizado pelos prestadores de serviços o retorno
    da consulta de Notas fiscais emitidas por RPS.

    :ivar cabecalho: Cabeçalho da Consulta.
    :ivar notas: Informe os RPS a serem substituidos por NF-e.
    :ivar erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """
    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["RetornoConsultaNotas.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    notas: Optional[TpListaNfseConsultaNota] = field(
        default=None,
        metadata={
            "name": "Notas",
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
        :ivar inscricao_municipal_prestador: Informe a Inscrição
            Municipal do Prestador
        :ivar dt_inicio: Informe a data de início do    período
            transmitido     (AAAA-MM-DD).
        :ivar dt_fim: Informe a data final do período transmitido (AAAA-
            MM-DD).
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
        inscricao_municipal_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "InscricaoMunicipalPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{6,11}",
            }
        )
        dt_inicio: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dtInicio",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        dt_fim: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dtFim",
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
