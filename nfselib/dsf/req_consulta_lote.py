from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqConsultaLote:
    """Schema utilizado para REQUISIçÂO de Consulta de Lote de RPS.

    Este Schema XML é utilizado pelos Prestadores de serviços para
    consultarem Lote de RPS emitidos por eles.

    :ivar cabecalho: Cabeçalho do pedido.
    """
    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    cabecalho: Optional["ReqConsultaLote.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar cod_cidade: Informe o Codigo da Cidade.
        :ivar cpfcnpjremetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar versao: Informe a Versão do Schema XML utilizado.
        :ivar numero_lote: Informe o Número do Lote a ser consultado.
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
        numero_lote: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumeroLote",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": "0",
                "max_inclusive": "2147483647",
                "pattern": r"[0-9]{1,12}",
            }
        )
