from dataclasses import dataclass, field
from typing import Optional
from nfselib.dsf.tipos import TpLoteConsultaNfse
from nfselib.dsf.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqConsultaNfseRps:
    """Schema utilizado para  Consulta de NFSe.

    Este Schema XML é utilizado pelos Prestadores de serviços
    consultarem NFSe emitidas por eles.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar lote: Detalhe do pedido de consulta de NFSe. Cada detalhe
        deverá conter a Chave de uma NFSe e sua respectiva assinatura de
        consulta.
    :ivar signature:
    """
    class Meta:
        name = "ReqConsultaNFSeRPS"
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["ReqConsultaNfseRps.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    lote: Optional[TpLoteConsultaNfse] = field(
        default=None,
        metadata={
            "name": "Lote",
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
