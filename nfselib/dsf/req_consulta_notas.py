from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nfselib.dsf.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqConsultaNotas:
    """Schema utilizado para REQUISIÇAO de consultas de notas que foram
    enviadas por lote de RPS.

    Este Schema XML é utilizado pelos prestadores de serviços para
    consultas de notas que foram enviadas por lote de RPS.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar signature:
    """
    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["ReqConsultaNotas.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
        :ivar dt_inicio: Informe a data de início do período transmitido
            (AAAA-MM-DD).
        :ivar dt_fim: Informe a data final do período transmitido (AAAA-
            MM-DD).
        :ivar nota_inicial: Numero da nota inicial da consulta. Ou seja
            a consulta ira retornar as notas no periodo, onde o numero
            da nota seja maior ou igual a esse numero. O retorno não
            pode ultrapassar 500Kb. Caso não tenha o numero da nota,
            passar o valor Zero, será retornado as notas geradas no
            periodo até o limite de 500kb.
        :ivar versao: Informe a Versão.
        :ivar id:
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
        nota_inicial: Optional[str] = field(
            default=None,
            metadata={
                "name": "NotaInicial",
                "type": "Element",
                "namespace": "",
                "min_inclusive": "0",
                "max_inclusive": "2147483647",
                "pattern": r"[0-9]{1,12}",
            }
        )
        versao: Optional[str] = field(
            default=None,
            metadata={
                "name": "Versao",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
            }
        )
