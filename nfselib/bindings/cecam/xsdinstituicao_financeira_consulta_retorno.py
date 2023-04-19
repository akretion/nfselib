from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class ConsultaLancamentoInstituicaoFinanceira:
    Header: Optional["ConsultaLancamentoInstituicaoFinanceira.Header"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    Filtro: Optional["ConsultaLancamentoInstituicaoFinanceira.Filtro"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Header:
        """
        :ivar CNPJInstituicao: CNPJ da Instituicao Financeira (sem
            mascara)
        :ivar Chave: Chave identificadora da empresa adquirida pelo
            sistema de ISS ELetronico
        """
        CNPJInstituicao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "length": 14,
            }
        )
        Chave: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "length": 48,
            }
        )

    @dataclass
    class Filtro:
        """
        :ivar NumeroDocumentoInicial: Número do documento
        :ivar Data_Emissao: Data do Lançamento
        :ivar Lote: Numero do Lote
        """
        NumeroDocumentoInicial: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Data_Emissao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        Lote: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
