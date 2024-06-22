from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from nfselib.dsf.bindings.tipos import (
    TpListaErros,
    TpListaNfseConsultaNota,
)

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class RetornoConsultaNotas:
    """Schema utilizado para Retrono de consulta de notas.

    Este Schema XML é utilizado pelos prestadores de serviços o retorno
    da consulta de Notas fiscais emitidas por RPS.

    :ivar Cabecalho: Cabeçalho da Consulta.
    :ivar Notas: Informe os RPS a serem substituidos por NF-e.
    :ivar Erros: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    """

    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["RetornoConsultaNotas.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Notas: Optional[TpListaNfseConsultaNota] = field(
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
        :ivar InscricaoMunicipalPrestador: Informe a Inscrição Municipal
            do Prestador
        :ivar dtInicio: Informe a data de início do     período
            transmitido     (AAAA-MM-DD).
        :ivar dtFim: Informe a data final do período transmitido (AAAA-
            MM-DD).
        :ivar Versao: Versão do Schema XML utilizado.
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
        InscricaoMunicipalPrestador: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{6,11}",
            },
        )
        dtInicio: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        dtFim: Optional[XmlDate] = field(
            default=None,
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
