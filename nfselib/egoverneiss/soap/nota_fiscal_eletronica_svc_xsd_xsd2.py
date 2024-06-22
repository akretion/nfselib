from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from nfselib.egoverneiss.soap.nota_fiscal_eletronica_svc_xsd_xsd3 import (
    ArrayOfExecutor,
    ArrayOfNotaCanceladaLoteDto,
    ArrayOfNotaCancelamentoLoteDto,
    ArrayOfNotaFiscalConsultaDto,
    ArrayOfNotaFiscalLoteGeradaDto,
    ArrayOfNotaFiscalRelatorioDto,
    ArrayOfNotaFiscalRepasseR2LoteDto,
    ArrayOfNotaFiscalRepasseVinculadaDto,
    ArrayOfNotaFiscalRrelatorioDto,
    ArrayOfNotaFiscalRs2RelatorioDto,
    NotaFiscalDto,
    NotaFiscalGeradaDto,
    NotaFiscalRepasse2Dto,
    NotaFiscalRepasseDto,
    NotaFiscalRepasseGeradaDto,
    NotasFiscaisLoteDto,
)

__NAMESPACE__ = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"


@dataclass
class RequestBase:
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"


@dataclass
class ResponseBase:
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    Erro: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    MensagemErro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelamentoNotaFiscalLoteRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmailContato: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Homologacao: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Notas: Optional[ArrayOfNotaCancelamentoLoteDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelamentoNotaFiscalLoteResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelamentoNotaFiscalRepasseRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelamentoNotaFiscalRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Homologacao: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Motivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CancelamentoNotaFiscalResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"


@dataclass
class ConsultaCancelamentoNotasLoteRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodigoLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaCancelamentoNotasLoteResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    CodigoLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ContadorNotasCanceladas: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ContadorNotasErro: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataEnvio: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataFinalizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataInicioProcessamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NotasCanceladas: Optional[ArrayOfNotaCanceladaLoteDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaExecutoresVinculadosRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodigoLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaExecutoresVinculadosResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    CodigoLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ContadorExecutoresErro: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ContadorExecutoresVinculados: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataEnvio: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataFinalizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataInicioProcessamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExecutoresVinculados: Optional[ArrayOfNotaFiscalRepasseVinculadaDto] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
    )


@dataclass
class ConsultaNotaFiscalCompletaResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    DataEnvio: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataFinalizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    NotasGeradas: Optional[ArrayOfNotaFiscalRelatorioDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    QtdeNotas: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNotaFiscalLoteRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodigoLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    StatusNotas: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaNotaFiscalLoteResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    CodigoLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ContadorNotasErro: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ContadorNotasGeradas: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataEnvio: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataFinalizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataInicioProcessamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NotasGeradas: Optional[ArrayOfNotaFiscalLoteGeradaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaNotaFiscalRepasseR2LoteRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodigoLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNotaFiscalRepasseR2Response(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    DataEnvio: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataFinalizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    NotasGeradas: Optional[ArrayOfNotaFiscalRs2RelatorioDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    QtdeNotas: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNotaFiscalRepasseRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    CNPJReceptor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CPFReceptor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataFinal: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataInicial: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroNota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaNotaFiscalRepasseResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    DataEnvio: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataFinalizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    NotasGeradas: Optional[ArrayOfNotaFiscalRrelatorioDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    QtdeNotas: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ConsultaNotaFiscalRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    CNPJTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CPFTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataFinal: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataInicial: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroNotaFinal: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroNotaInicial: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroReciboFinal: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroReciboInicial: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroReciboUnico: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaNotaFiscalResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    DataEnvio: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataFinalizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    NotasGeradas: Optional[ArrayOfNotaFiscalConsultaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    QtdeNotas: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class EmissaoNotaFiscalLoteRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    Notas: Optional[NotasFiscaisLoteDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmissaoNotaFiscalLoteResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmissaoNotaFiscalRepasseR2LoteRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmailContato: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Homologacao: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Notas: Optional[ArrayOfNotaFiscalRepasseR2LoteDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmissaoNotaFiscalRepasseR2LoteResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmissaoNotaFiscalRepasseR2Request(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    NotaFiscalRepasse: Optional[NotaFiscalRepasse2Dto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmissaoNotaFiscalRepasseRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    NotaFiscalRepasse: Optional[NotaFiscalRepasseDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmissaoNotaFiscalRepasseResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    NotaFiscalGerada: Optional[NotaFiscalRepasseGeradaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroControle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmissaoNotaFiscalRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    NotaFiscal: Optional[NotaFiscalDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EmissaoNotaFiscalResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    NotaFiscalGerada: Optional[NotaFiscalGeradaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EnviarExecutoresRequest(RequestBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    CNPJEmissor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ListaExecutores: Optional[ArrayOfExecutor] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class EnviarExecutoresResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    Mensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfEmissaoNotaFiscalRepasseResponse:
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    EmissaoNotaFiscalRepasseResponse: List[
        EmissaoNotaFiscalRepasseResponse
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ConsultaNotaFiscalRepasseR2LoteResponse(ResponseBase):
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Negocio.WebServices.Mensagem"

    CodigoLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ContadorNotasErro: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ContadorNotasRepasseR2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataEnvio: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataFinalizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataInicioProcessamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NotasRepasses: Optional[ArrayOfEmissaoNotaFiscalRepasseResponse] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
