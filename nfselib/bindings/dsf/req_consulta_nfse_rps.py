from dataclasses import dataclass, field
from typing import Optional
from nfselib.bindings.dsf.tipos import TpLoteConsultaNfse
from nfselib.bindings.dsf.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqConsultaNfseRps:
    """Schema utilizado para  Consulta de NFSe.

    Este Schema XML é utilizado pelos Prestadores de serviços
    consultarem NFSe emitidas por eles.

    :ivar Cabecalho: Cabeçalho do pedido.
    :ivar Lote: Detalhe do pedido de consulta de NFSe. Cada detalhe
        deverá conter a Chave de uma NFSe e sua respectiva assinatura de
        consulta.
    :ivar signature:
    """
    class Meta:
        name = "ReqConsultaNFSeRPS"
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["ReqConsultaNfseRps.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    Lote: Optional[TpLoteConsultaNfse] = field(
        default=None,
        metadata={
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
            }
        )
        CPFCNPJRemetente: Optional[str] = field(
            default=None,
            metadata={
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
        Versao: str = field(
            init=False,
            default="1",
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )
