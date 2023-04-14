from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.equiplano.com.br/esnfs/tipos"


@dataclass
class TcCancelamentoNfse:
    """
    Representa a estrutura de cancelamento da Nfse.
    """
    class Meta:
        name = "tcCancelamentoNfse"

    dtCancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dsCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1024,
        }
    )


@dataclass
class TcCompetencia:
    """
    Representa a estrutura da competência.
    """
    class Meta:
        name = "tcCompetencia"

    nrAnoCompetencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{4}",
        }
    )
    nrMesCompetencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "1",
            "max_inclusive": "12",
            "pattern": r"[0-9]{1,2}",
        }
    )


@dataclass
class TcDeducao:
    """
    Representa a estrutura da deducao.
    """
    class Meta:
        name = "tcDeducao"

    vlDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    dsJustificativaDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class TcDocumento:
    """
    Representa a estrutura do documento.
    """
    class Meta:
        name = "tcDocumento"

    nrDocumento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    tpDocumento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-3]{1}",
        }
    )
    dsDocumentoEstrangeiro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
        }
    )


@dataclass
class TcErroAlerta:
    """
    Representa a estrutura do Erro/Alerta.
    """
    class Meta:
        name = "tcErroAlerta"

    cdMensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        }
    )
    dsMensagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 512,
        }
    )
    dsCorrecao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 512,
        }
    )


@dataclass
class TcIdentificacaoNfse:
    """
    Representa da identificação na NFS-e.
    """
    class Meta:
        name = "tcIdentificacaoNfse"

    nrNfse: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cdAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 8,
            "max_length": 100,
        }
    )
    nrRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    nrEmissorRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    """
    Representa a estrutura da identificação do prestador.
    """
    class Meta:
        name = "tcIdentificacaoPrestador"

    nrInscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    idEntidade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoRps:
    """
    Representa a identificação do Rps.
    """
    class Meta:
        name = "tcIdentificacaoRps"

    nrRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrEmissorRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcNfseSemCancelamento:
    """
    Representa a estrutura da Nota Fiscal de Serviços Eletrônica.
    """
    class Meta:
        name = "tcNfseSemCancelamento"

    nrNfs: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cdAutenticacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 8,
            "max_length": 100,
        }
    )
    dtEmissaoNfs: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    nrEmissorRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dtEmissaoRps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dsLink: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcPrestador:
    """
    Representa a estrutura do prestador.
    """
    class Meta:
        name = "tcPrestador"

    nrCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    nrInscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,10}",
        }
    )
    isOptanteSimplesNacional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2]{1}",
        }
    )
    idEntidade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcProtocolo:
    """
    Representa a estrutura do protocolo.
    """
    class Meta:
        name = "tcProtocolo"

    nrLote: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dtRecebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrProtocolo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcProtocoloIntegracao:
    """
    Representa a estrutura do protocolo.
    """
    class Meta:
        name = "tcProtocoloIntegracao"

    nrProtocolo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dtProtocolo: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dsProtocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 512,
        }
    )
    isOk: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcRetencoes:
    """
    Representa a estrutura das retenções.
    """
    class Meta:
        name = "tcRetencoes"

    vlCofins: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlCsll: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlInss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlIrrf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlPis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlIss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlAliquotaCofins: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vlAliquotaCsll: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vlAliquotaInss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vlAliquotaIrrf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vlAliquotaPis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )


@dataclass
class TcServicoAeSubItem:
    """
    Estrutura do serviço AE sub item.
    """
    class Meta:
        name = "tcServicoAeSubItem"

    nrSubItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dsSubItem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    isInformarDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    isTomadorObrigatorio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    tpRetencao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-3]{1}",
        }
    )
    vlAliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlPercentualMaximoDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )


@dataclass
class TcServicoIntegracao:
    """
    Representa a estrutura para importação dos serviçoes de uma empresa
    (Utilizada somente na integração STM/ESNFS) Serviço.
    """
    class Meta:
        name = "tcServicoIntegracao"

    nrItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrSubItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    isInformarDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    isTomadorObrigatorio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    vlAliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )


@dataclass
class TcServicoLivroFeo:
    """
    Representa a estrutura do serviço para o livro fiscal eletrônico.
    """
    class Meta:
        name = "tcServicoLivroFEO"

    nrServicoItemLC116: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrServicoSubItemLC116: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dsDiscriminacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1024,
        }
    )
    vlServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlAliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vlDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlBaseCalculo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlIssServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    dsJustificativaDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class TcGuiaRecolhimento:
    """
    Representa de uma guia de recolhimento.
    """
    class Meta:
        name = "tcGuiaRecolhimento"

    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrGuia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    stGuia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    competencia: Optional[TcCompetencia] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dsCodigoBarra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 44,
        }
    )
    tpCodigoBarra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-2]{1}",
        }
    )
    dtVencimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dtEmissaoGuia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    vlMovimento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlImposto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlImpostoRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlPago: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    dsObservacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 60,
        }
    )


@dataclass
class TcIdentificacaoTomador:
    """
    Representa a identificacao do tomador.
    """
    class Meta:
        name = "tcIdentificacaoTomador"

    documento: Optional[TcDocumento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nmTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
        }
    )


@dataclass
class TcMensagemRetorno:
    """
    Representa a estrutura da mensagem de retorno.
    """
    class Meta:
        name = "tcMensagemRetorno"

    listaErros: Optional["TcMensagemRetorno.ListaErros"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    listaAlertas: Optional["TcMensagemRetorno.ListaAlertas"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ListaErros:
        erro: List[TcErroAlerta] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class ListaAlertas:
        alerta: List[TcErroAlerta] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class TcNfse:
    """
    Representa a estrutura da nfs-e incluindo a estrututa de cancelamento da
    mesma, quando existente.
    """
    class Meta:
        name = "tcNfse"

    nfse: Optional[TcNfseSemCancelamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cancelamento: Optional[TcCancelamentoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcNotaLivroFeo:
    """
    Representa a estrutura das notas para serem utilizadas no livro fiscal
    eletrônico.
    """
    class Meta:
        name = "tcNotaLivroFEO"

    nrNfs: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dtEmissaoNfs: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tpTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    nrCnpjTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    nrInscricaoMunicipalTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    nmTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
        }
    )
    vlTotalNfs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlTotalImposto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlTotalDeducoes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    isTomadorInformado: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    isIssRetido: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    servicos: Optional["TcNotaLivroFeo.Servicos"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Servicos:
        servico: List[TcServicoIntegracao] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class TcPessoa:
    """
    Estrutura da pessoas.
    """
    class Meta:
        name = "tcPessoa"

    idEntidade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tpPessoa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    stPessoa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-6]{1}",
        }
    )
    nmPessoa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
        }
    )
    nrInscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    nrInscricaoEstadual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    nrDocumentoContador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 20,
        }
    )
    nmFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
        }
    )
    nrDocumento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    nrCep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8}",
        }
    )
    dsEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nrEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
        }
    )
    dsComplemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nmBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 25,
        }
    )
    nmCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 30,
        }
    )
    nmUf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 2,
        }
    )
    nmPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    nrTelefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    dsEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dsEnderecoWeb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 80,
        }
    )
    dtEnquadramentoSimples: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    nmContato: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 60,
        }
    )
    tpOpcaoSimplesNfs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2]{1}",
        }
    )
    tpIss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-5]{1}",
        }
    )
    isSubstitutoTributario: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    tpOpcaoMEI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    servicos: Optional["TcPessoa.Servicos"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Servicos:
        servico: List[TcServicoIntegracao] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class TcPessoaHomologacao:
    """
    Estrutura da pessoa.
    """
    class Meta:
        name = "tcPessoaHomologacao"

    idEntidade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tpPessoa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    stPessoa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-6]{1}",
        }
    )
    nmPessoa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
        }
    )
    nrInscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    nrInscricaoEstadual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    nrDocumentoContador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 20,
        }
    )
    nmFantasia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
        }
    )
    nrDocumento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    nrCep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8}",
        }
    )
    dsEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 40,
        }
    )
    nrEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
        }
    )
    dsComplemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nmBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 25,
        }
    )
    nmCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    nmUf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 2,
        }
    )
    nmPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    nrTelefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    dsEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "pattern": r"[\w\-_]+(\.[\w\-_]+)*@(([\w\-]{2,63}\.)+[A-Za-z]{2,6}|\[\d{1,3}(\.\d{1,3}){3}\])",
        }
    )
    dsEnderecoWeb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 80,
        }
    )
    dtEnquadramentoSimples: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    nmContato: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 60,
        }
    )
    tpOpcaoSimplesNfs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2]{1}",
        }
    )
    dsEmailNfs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "pattern": r"[\w\-_]+(\.[\w\-_]+)*@(([\w\-]{2,63}\.)+[A-Za-z]{2,6}|\[\d{1,3}(\.\d{1,3}){3}\])",
        }
    )
    isReceberEMailNfsRecebida: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    isEnvEMailContadorNfsEmitida: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    dsFraseSeguranca: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 255,
        }
    )
    dtEmissaoNfsSolicitacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dtEmissaoNfsAutorizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    qtMediaNotasEmitidas: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    isEnvioArquivoLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    qtEmissoresRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    isAuthorizedWebServices: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    stEmissaoNfsAutorizacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[1-3]{1}",
        }
    )
    servicos: Optional["TcPessoaHomologacao.Servicos"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Servicos:
        servico: List[TcServicoIntegracao] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class TcServico:
    """
    Representa a estrutura do serviço.
    """
    class Meta:
        name = "tcServico"

    nrServicoItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrServicoSubItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    vlServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlAliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    deducao: Optional[TcDeducao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    vlBaseCalculo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlIssServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    dsDiscriminacaoServico: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1024,
        }
    )


@dataclass
class TcServicoAeitem:
    """
    Estrutura do serviço AE item.
    """
    class Meta:
        name = "tcServicoAeitem"

    nrItem: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dsItem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    isInformarDeducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    isTomadorObrigatorio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    tpRetencao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-3]{1}",
        }
    )
    vlAliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    subItemList: Optional["TcServicoAeitem.SubItemList"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class SubItemList:
        subItem: List[TcServicoAeSubItem] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class TcTomador:
    """
    Representa a estrutura do tomador.
    """
    class Meta:
        name = "tcTomador"

    documento: Optional[TcDocumento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    nmTomador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
        }
    )
    dsEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "pattern": r"[\w\-_]+(\.[\w\-_]+)*@(([\w\-]{2,63}\.)+[A-Za-z]{2,6}|\[\d{1,3}(\.\d{1,3}){3}\])",
        }
    )
    nrInscricaoEstadual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    nrInscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    dsEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nrEndereco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
        }
    )
    dsComplemento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nmBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 25,
        }
    )
    nrCidadeIbge: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    nmUf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 2,
        }
    )
    nmCidadeEstrangeira: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
        }
    )
    nmPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    nrCep: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8}",
        }
    )
    nrTelefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )


@dataclass
class TcLivroFiscalEletronico:
    """
    Representa a estrutura do livro fiscal eletrônico.
    """
    class Meta:
        name = "tcLivroFiscalEletronico"

    nrVersaoLayout: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrMesCompetencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "1",
            "max_inclusive": "12",
            "pattern": r"[0-9]{1,2}",
        }
    )
    nrAnoCompetencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{4}",
        }
    )
    nrCnpjPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    nrInscricaoMunicipalPrestador: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,10}",
        }
    )
    isOptanteSimplesNacional: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dtEnquadramentoSimplesNacional: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    notas: Optional["TcLivroFiscalEletronico.Notas"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Notas:
        nota: List[TcNotaLivroFeo] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class TcRps:
    """
    Representa a estrutura de recibo provisório de serviços (Rps)
    """
    class Meta:
        name = "tcRps"

    nrRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nrEmissorRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dtEmissaoRps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    stRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    tpTributacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    nrCidadeIbgeServico: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    isIssRetido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2]{1}",
        }
    )
    tomador: Optional[TcTomador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    listaServicos: Optional["TcRps.ListaServicos"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    vlTotalRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vlLiquidoRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    retencoes: Optional[TcRetencoes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dsImpostos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 500,
        }
    )

    @dataclass
    class ListaServicos:
        servico: List[TcServico] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class TcServicoAtualizacao:
    """
    Estrutura do serviço para atualização.
    """
    class Meta:
        name = "tcServicoAtualizacao"

    item: Optional[TcServicoAeitem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
