from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from nfselib.egoverneiss.soap.nota_fiscal_eletronica_svc_xsd_xsd4 import (
    PessoaDto,
)

__NAMESPACE__ = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"


@dataclass
class Executor:
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Atividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CNPJExecutor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CNPJTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CPFExecutor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NomeExecutor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroDocumento: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroNotaRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ValorRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NotaCanceladaLoteDto:
    class Meta:
        name = "NotaCanceladaLoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Cancelada: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
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
    Motivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroNota: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class NotaCancelamentoLoteDto:
    class Meta:
        name = "NotaCancelamentoLoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Motivo: Optional[str] = field(
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
            "required": True,
        },
    )


@dataclass
class NotaFiscalConsultaDto:
    class Meta:
        name = "NotaFiscalConsultaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodAtividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodObra: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodigoAutenticidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataRecibo: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DocTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EnderecoPrestacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    LinkNFE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    MotivoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NomeTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NossoNumero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Numero: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    NumeroRecibo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    SubstituicaoTributaria: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Valor: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorNFE: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class NotaFiscalGeradaDto:
    class Meta:
        name = "NotaFiscalGeradaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Autenticador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotaFiscalRrelatorioDto:
    class Meta:
        name = "NotaFiscalRRelatorioDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    AnoMesReferencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodAutenticidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DtEmissao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorDoc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorFone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorIM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorUF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    HrEmissao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    LinkNFR: Optional[str] = field(
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
    NumeroNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecDoc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecFone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecIM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecUF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorIRRF: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorNota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorPisPasep: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class NotaFiscalRs2RelatorioDto:
    class Meta:
        name = "NotaFiscalRS2RelatorioDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    AnoMesReferencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodAutenticidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DtEmissao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorDoc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorFone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorIM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmissorUF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExecCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExecDoc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExecEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExecEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExecFone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExecIM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExecUF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    HrEmissao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    LinkNFR: Optional[str] = field(
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
    NumeroNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecDoc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecFone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecIM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    RecUF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorIRRF: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorPisPasep: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class NotaFiscalRepasseGeradaDto:
    class Meta:
        name = "NotaFiscalRepasseGeradaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Autenticador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Numero: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotaFiscalRepasseVinculadaDto:
    class Meta:
        name = "NotaFiscalRepasseVinculadaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    CNPJExecutor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CPFExecutor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
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
    NomeExecutor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroDocumento: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroNotaRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorVinculado: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ArrayOfExecutor:
    class Meta:
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Executor: List[Executor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaCanceladaLoteDto:
    class Meta:
        name = "ArrayOfNotaCanceladaLoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaCanceladaLoteDTO: List[NotaCanceladaLoteDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaCancelamentoLoteDto:
    class Meta:
        name = "ArrayOfNotaCancelamentoLoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaCancelamentoLoteDTO: List[NotaCancelamentoLoteDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaFiscalConsultaDto:
    class Meta:
        name = "ArrayOfNotaFiscalConsultaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalConsultaDTO: List[NotaFiscalConsultaDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaFiscalRrelatorioDto:
    class Meta:
        name = "ArrayOfNotaFiscalRRelatorioDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalRRelatorioDTO: List[NotaFiscalRrelatorioDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaFiscalRs2RelatorioDto:
    class Meta:
        name = "ArrayOfNotaFiscalRS2RelatorioDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalRS2RelatorioDTO: List[NotaFiscalRs2RelatorioDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaFiscalRepasseVinculadaDto:
    class Meta:
        name = "ArrayOfNotaFiscalRepasseVinculadaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalRepasseVinculadaDTO: List[NotaFiscalRepasseVinculadaDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotaFiscalDto:
    class Meta:
        name = "NotaFiscalDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Atividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CEPPrestacaoServico: Optional[str] = field(
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
    CidadePrestacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataRecibo: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DeduzirRepasse: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EnderecoPrestacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EqptoRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EstadoPrestacaoServico: Optional[str] = field(
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
    InformacoesAdicionais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NotaSubstituida: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NotificarTomadorPorEmail: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroCDC: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroCei: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    NumeroRecibo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    SemIncidenciaISS: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SimplesNacional: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SubstituicaoTributaria: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Tomador: Optional[PessoaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    TomadorEstrangeiro: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Valor: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ValorCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorDeducao: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorIR: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorOutrosImpostos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorPisPasep: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    nrExercicioReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    nrMesReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotaFiscalLoteGeradaDto(NotaFiscalGeradaDto):
    class Meta:
        name = "NotaFiscalLoteGeradaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    EquipamentoRecibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Erro: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Identificador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    MensagemErro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Recibo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotaFiscalR2LoteDto:
    class Meta:
        name = "NotaFiscalR2LoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    ConteudoEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmailDestinatario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmitidaParaHomologacao: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    EnviarPorEmail: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Executor: Optional[PessoaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExercicioReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    MesReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroControle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Tomador: Optional[PessoaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorIRRF: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorPisPasep: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NotaFiscalRelatorioDto:
    class Meta:
        name = "NotaFiscalRelatorioDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    BaseCalculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CDC: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CEI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CEPPrestacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CidadePrestacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    CodigoAutenticidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DataEmissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    DataRecibo: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DescricaoAtividade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    DescricaoServicos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmitidaParaHomologacao: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    EmitidaParaPreVisualizacao: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    EnderecoPrestacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EstadoPrestacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    IdObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    IdSegmentoAtividade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    InformacoesAdicionais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    IsCEI: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    NotaFiscalSubstituida: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Numero: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    NumeroRecibo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Prestador: Optional[PessoaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    PrestadorEmPPA: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ProcessoJudicial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    SimplesNacional: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SomarISSAoValorTotal: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SubstituicaoTributaria: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    SuspensaoExigiblidade: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Tomador: Optional[PessoaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Valor: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorDeducao: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorIR: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorIss: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ValorOutrosImpostos: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorPisPasep: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotaFiscalRepasse2Dto:
    class Meta:
        name = "NotaFiscalRepasse2DTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ConteudoEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmailDestinatario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmitidaParaHomologacao: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    EnviarPorEmail: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    Executor: Optional[PessoaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ExercicioReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    MesReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroControle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Tomador: Optional[PessoaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorIRRF: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorPisPasep: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class NotaFiscalRepasseDto:
    class Meta:
        name = "NotaFiscalRepasseDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    ChaveAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ConteudoEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmailDestinatario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    EmitidaParaHomologacao: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    EnviarPorEmail: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ExercicioReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    MesReferencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    NumeroControle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    Receptor: Optional[PessoaDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCSLL: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorCofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorINSS: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorIRRF: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorNota: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ValorPisPasep: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ValorRepasse: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ArrayOfNotaFiscalLoteGeradaDto:
    class Meta:
        name = "ArrayOfNotaFiscalLoteGeradaDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalLoteGeradaDTO: List[NotaFiscalLoteGeradaDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaFiscalRelatorioDto:
    class Meta:
        name = "ArrayOfNotaFiscalRelatorioDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalRelatorioDTO: List[NotaFiscalRelatorioDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotaFiscalLoteDto(NotaFiscalDto):
    class Meta:
        name = "NotaFiscalLoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    Identificador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotaFiscalRepasseR2LoteDto:
    class Meta:
        name = "NotaFiscalRepasseR2LoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalRepasse: Optional[NotaFiscalR2LoteDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaFiscalLoteDto:
    class Meta:
        name = "ArrayOfNotaFiscalLoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalLoteDTO: List[NotaFiscalLoteDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfNotaFiscalRepasseR2LoteDto:
    class Meta:
        name = "ArrayOfNotaFiscalRepasseR2LoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

    NotaFiscalRepasseR2LoteDTO: List[NotaFiscalRepasseR2LoteDto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class NotasFiscaisLoteDto:
    class Meta:
        name = "NotasFiscaisLoteDTO"
        namespace = "http://schemas.datacontract.org/2004/07/Eissnfe.Dominio.DataTransferObject.Prestador"

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
    Notas: Optional[ArrayOfNotaFiscalLoteDto] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
