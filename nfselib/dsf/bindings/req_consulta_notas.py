from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from nfselib.dsf.bindings.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqConsultaNotas:
    """Schema utilizado para REQUISIÇAO de consultas de notas que foram enviadas
    por lote de RPS.

    Este Schema XML é utilizado pelos prestadores de serviços para
    consultas de notas que foram enviadas por lote de RPS.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar signature:
    """

    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["ReqConsultaNotas.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
        :ivar dtInicio: Informe a data de início do período transmitido
            (AAAA-MM-DD).
        :ivar dtFim: Informe a data final do período transmitido (AAAA-
            MM-DD).
        :ivar NotaInicial: Numero da nota inicial da consulta. Ou seja a
            consulta ira retornar as notas no periodo, onde o numero da
            nota seja maior ou igual a esse numero. O retorno não pode
            ultrapassar 500Kb. Caso não tenha o numero da nota, passar o
            valor Zero, será retornado as notas geradas no periodo até o
            limite de 500kb.
        :ivar Versao: Informe a Versão.
        :ivar Id:
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
        NotaInicial: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_inclusive": "0",
                "max_inclusive": "2147483647",
                "pattern": r"[0-9]{1,12}",
            },
        )
        Versao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
