from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://localhost:8080/WsNFe2/lote"


@dataclass
class ReqConsultaLote:
    """Schema utilizado para REQUISIçÂO de Consulta de Lote de RPS.

    Este Schema XML é utilizado pelos Prestadores de serviços para
    consultarem Lote de RPS emitidos por eles.

    :ivar Cabecalho: Cabeçalho do pedido.
    """

    class Meta:
        namespace = "http://localhost:8080/WsNFe2/lote"

    Cabecalho: Optional["ReqConsultaLote.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar CodCidade: Informe o Codigo da Cidade.
        :ivar CPFCNPJRemetente: Informe o CPF/CNPJ do Remetente
            autorizado a transmitir a mensagem XML.
        :ivar Versao: Informe a Versão do Schema XML utilizado.
        :ivar NumeroLote: Informe o Número do Lote a ser consultado.
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
        NumeroLote: Optional[str] = field(
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
