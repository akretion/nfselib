from dataclasses import dataclass, field
from typing import Optional
from nfselib.blumenau_sc.tipos_nfe_v01 import TpCpfcnpj
from nfselib.blumenau_sc.xmldsig_core_schema_v01 import Signature

__NAMESPACE__ = "http://nfse.blumenau.sc.gov.br"


@dataclass
class PedidoInformacoesLote:
    """Schema utilizado para PEDIDO de informações de lote.

    Este Schema XML é utilizado pelos prestadores de serviços para
    obterem informações de lotes de RPS que geraram NFS-e.

    :ivar cabecalho: Cabeçalho do pedido.
    :ivar signature: Assinatura digital do contribuinte que gerou o lote
        de RPS.
    """
    class Meta:
        namespace = "http://nfse.blumenau.sc.gov.br"

    cabecalho: Optional["PedidoInformacoesLote.Cabecalho"] = field(
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
            "required": True,
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar cpfcnpjremetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar numero_lote: Informe o número do lote que deseja obter
            informações. Caso não seja informado o número do lote, serão
            retornadas informações do último lote gerador de NFS-e.
        :ivar inscricao_prestador: Informe a Inscrição municipal do
            prestador de serviços que gerou o lote.
        :ivar versao: Informe a Versão do Schema XML utilizado.
        """
        cpfcnpjremetente: Optional[TpCpfcnpj] = field(
            default=None,
            metadata={
                "name": "CPFCNPJRemetente",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        numero_lote: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroLote",
                "type": "Element",
                "namespace": "",
                "pattern": r"[0-9]{1,13}",
            }
        )
        inscricao_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "InscricaoPrestador",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,15}",
            }
        )
        versao: str = field(
            init=False,
            default="1",
            metadata={
                "name": "Versao",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )
