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

    dt_cancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtCancelamento",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ds_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsCancelamento",
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

    nr_ano_competencia: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrAnoCompetencia",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{4}",
        }
    )
    nr_mes_competencia: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrMesCompetencia",
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

    vl_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlDeducao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    ds_justificativa_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsJustificativaDeducao",
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

    nr_documento: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrDocumento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    tp_documento: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpDocumento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-3]{1}",
        }
    )
    ds_documento_estrangeiro: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsDocumentoEstrangeiro",
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

    cd_mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "cdMensagem",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        }
    )
    ds_mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsMensagem",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 512,
        }
    )
    ds_correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsCorrecao",
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

    nr_nfse: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrNfse",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cd_autenticacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "cdAutenticacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 8,
            "max_length": 100,
        }
    )
    nr_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrRps",
            "type": "Element",
            "namespace": "",
        }
    )
    nr_emissor_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrEmissorRps",
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

    nr_inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoMunicipal",
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
    id_entidade: Optional[int] = field(
        default=None,
        metadata={
            "name": "idEntidade",
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

    nr_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_emissor_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrEmissorRps",
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

    nr_nfs: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrNfs",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cd_autenticacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "cdAutenticacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 8,
            "max_length": 100,
        }
    )
    dt_emissao_nfs: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtEmissaoNfs",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrRps",
            "type": "Element",
            "namespace": "",
        }
    )
    nr_emissor_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrEmissorRps",
            "type": "Element",
            "namespace": "",
        }
    )
    dt_emissao_rps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtEmissaoRps",
            "type": "Element",
            "namespace": "",
        }
    )
    ds_link: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsLink",
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

    nr_cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrCnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    nr_inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoMunicipal",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,10}",
        }
    )
    is_optante_simples_nacional: Optional[str] = field(
        default=None,
        metadata={
            "name": "isOptanteSimplesNacional",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2]{1}",
        }
    )
    id_entidade: Optional[int] = field(
        default=None,
        metadata={
            "name": "idEntidade",
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

    nr_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrLote",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dt_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtRecebimento",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_protocolo: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrProtocolo",
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

    nr_protocolo: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrProtocolo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dt_protocolo: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtProtocolo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ds_protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsProtocolo",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 512,
        }
    )
    is_ok: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isOk",
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

    vl_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlCofins",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlCsll",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlInss",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_irrf: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlIrrf",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlPis",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlIss",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_aliquota_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquotaCofins",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vl_aliquota_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquotaCsll",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vl_aliquota_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquotaInss",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vl_aliquota_irrf: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquotaIrrf",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vl_aliquota_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquotaPis",
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

    nr_sub_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrSubItem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ds_sub_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsSubItem",
            "type": "Element",
            "namespace": "",
        }
    )
    is_informar_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "isInformarDeducao",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    is_tomador_obrigatorio: Optional[str] = field(
        default=None,
        metadata={
            "name": "isTomadorObrigatorio",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    tp_retencao: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpRetencao",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-3]{1}",
        }
    )
    vl_aliquota: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquota",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_percentual_maximo_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlPercentualMaximoDeducao",
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

    nr_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrItem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_sub_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrSubItem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    is_informar_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "isInformarDeducao",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    is_tomador_obrigatorio: Optional[str] = field(
        default=None,
        metadata={
            "name": "isTomadorObrigatorio",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    vl_aliquota: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquota",
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

    nr_servico_item_lc116: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrServicoItemLC116",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_servico_sub_item_lc116: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrServicoSubItemLC116",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ds_discriminacao_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsDiscriminacaoServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1024,
        }
    )
    vl_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_aliquota: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquota",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 5,
            "pattern": r"0\.[0-9]{0,4}|[0-9]{1}[0-9]{0,4}(\.[0-9]{0,4})?",
        }
    )
    vl_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlDeducao",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_base_calculo: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlBaseCalculo",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_iss_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlIssServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    ds_justificativa_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsJustificativaDeducao",
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
    nr_guia: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrGuia",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    st_guia: Optional[str] = field(
        default=None,
        metadata={
            "name": "stGuia",
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
    ds_codigo_barra: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsCodigoBarra",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 44,
        }
    )
    tp_codigo_barra: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpCodigoBarra",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-2]{1}",
        }
    )
    dt_vencimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dtVencimento",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dt_emissao_guia: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtEmissaoGuia",
            "type": "Element",
            "namespace": "",
        }
    )
    vl_movimento: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlMovimento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_imposto: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlImposto",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_imposto_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlImpostoRetido",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_pago: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlPago",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    ds_observacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsObservacao",
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
    nm_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmTomador",
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

    lista_erros: Optional["TcMensagemRetorno.ListaErros"] = field(
        default=None,
        metadata={
            "name": "listaErros",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    lista_alertas: Optional["TcMensagemRetorno.ListaAlertas"] = field(
        default=None,
        metadata={
            "name": "listaAlertas",
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

    nr_nfs: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrNfs",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dt_emissao_nfs: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dtEmissaoNfs",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tp_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpTributacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    nr_cnpj_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrCnpjTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    nr_inscricao_municipal_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoMunicipalTomador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    nm_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
        }
    )
    vl_total_nfs: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlTotalNfs",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_total_imposto: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlTotalImposto",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_total_deducoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlTotalDeducoes",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    is_tomador_informado: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isTomadorInformado",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    is_iss_retido: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isIssRetido",
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

    id_entidade: Optional[int] = field(
        default=None,
        metadata={
            "name": "idEntidade",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tp_pessoa: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpPessoa",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    st_pessoa: Optional[str] = field(
        default=None,
        metadata={
            "name": "stPessoa",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-6]{1}",
        }
    )
    nm_pessoa: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmPessoa",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
        }
    )
    nr_inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoMunicipal",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    nr_inscricao_estadual: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoEstadual",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    nr_documento_contador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrDocumentoContador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 20,
        }
    )
    nm_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmFantasia",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
        }
    )
    nr_documento: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrDocumento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    nr_cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrCep",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8}",
        }
    )
    ds_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEndereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nr_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrEndereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
        }
    )
    ds_complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsComplemento",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nm_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmBairro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 25,
        }
    )
    nm_cidade: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmCidade",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 30,
        }
    )
    nm_uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmUf",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 2,
        }
    )
    nm_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmPais",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    nr_telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrTelefone",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    ds_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEmail",
            "type": "Element",
            "namespace": "",
        }
    )
    ds_endereco_web: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEnderecoWeb",
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 80,
        }
    )
    dt_enquadramento_simples: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dtEnquadramentoSimples",
            "type": "Element",
            "namespace": "",
        }
    )
    nm_contato: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmContato",
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 60,
        }
    )
    tp_opcao_simples_nfs: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpOpcaoSimplesNfs",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2]{1}",
        }
    )
    tp_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpIss",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-5]{1}",
        }
    )
    is_substituto_tributario: Optional[int] = field(
        default=None,
        metadata={
            "name": "isSubstitutoTributario",
            "type": "Element",
            "namespace": "",
        }
    )
    tp_opcao_mei: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpOpcaoMEI",
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

    id_entidade: Optional[int] = field(
        default=None,
        metadata={
            "name": "idEntidade",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tp_pessoa: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpPessoa",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    st_pessoa: Optional[str] = field(
        default=None,
        metadata={
            "name": "stPessoa",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-6]{1}",
        }
    )
    nm_pessoa: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmPessoa",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
        }
    )
    nr_inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoMunicipal",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    nr_inscricao_estadual: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoEstadual",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    nr_documento_contador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrDocumentoContador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 20,
        }
    )
    nm_fantasia: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmFantasia",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
        }
    )
    nr_documento: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrDocumento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    nr_cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrCep",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8}",
        }
    )
    ds_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEndereco",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 40,
        }
    )
    nr_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrEndereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
        }
    )
    ds_complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsComplemento",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nm_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmBairro",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 25,
        }
    )
    nm_cidade: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmCidade",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    nm_uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmUf",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 2,
        }
    )
    nm_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmPais",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    nr_telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrTelefone",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    ds_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEmail",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "pattern": r"[\w\-_]+(\.[\w\-_]+)*@(([\w\-]{2,63}\.)+[A-Za-z]{2,6}|\[\d{1,3}(\.\d{1,3}){3}\])",
        }
    )
    ds_endereco_web: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEnderecoWeb",
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 80,
        }
    )
    dt_enquadramento_simples: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dtEnquadramentoSimples",
            "type": "Element",
            "namespace": "",
        }
    )
    nm_contato: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmContato",
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 60,
        }
    )
    tp_opcao_simples_nfs: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpOpcaoSimplesNfs",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-2]{1}",
        }
    )
    ds_email_nfs: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEmailNfs",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "pattern": r"[\w\-_]+(\.[\w\-_]+)*@(([\w\-]{2,63}\.)+[A-Za-z]{2,6}|\[\d{1,3}(\.\d{1,3}){3}\])",
        }
    )
    is_receber_email_nfs_recebida: Optional[str] = field(
        default=None,
        metadata={
            "name": "isReceberEMailNfsRecebida",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    is_env_email_contador_nfs_emitida: Optional[str] = field(
        default=None,
        metadata={
            "name": "isEnvEMailContadorNfsEmitida",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    ds_frase_seguranca: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsFraseSeguranca",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 255,
        }
    )
    dt_emissao_nfs_solicitacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtEmissaoNfsSolicitacao",
            "type": "Element",
            "namespace": "",
        }
    )
    dt_emissao_nfs_autorizacao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtEmissaoNfsAutorizacao",
            "type": "Element",
            "namespace": "",
        }
    )
    qt_media_notas_emitidas: Optional[int] = field(
        default=None,
        metadata={
            "name": "qtMediaNotasEmitidas",
            "type": "Element",
            "namespace": "",
        }
    )
    is_envio_arquivo_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "isEnvioArquivoLote",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    qt_emissores_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "qtEmissoresRps",
            "type": "Element",
            "namespace": "",
        }
    )
    is_authorized_web_services: Optional[str] = field(
        default=None,
        metadata={
            "name": "isAuthorizedWebServices",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    st_emissao_nfs_autorizacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "stEmissaoNfsAutorizacao",
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

    nr_servico_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrServicoItem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_servico_sub_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrServicoSubItem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    vl_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_aliquota: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquota",
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
    vl_base_calculo: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlBaseCalculo",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_iss_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlIssServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    ds_discriminacao_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsDiscriminacaoServico",
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

    nr_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrItem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    ds_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsItem",
            "type": "Element",
            "namespace": "",
        }
    )
    is_informar_deducao: Optional[str] = field(
        default=None,
        metadata={
            "name": "isInformarDeducao",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    is_tomador_obrigatorio: Optional[str] = field(
        default=None,
        metadata={
            "name": "isTomadorObrigatorio",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-2]{1}",
        }
    )
    tp_retencao: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpRetencao",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-3]{1}",
        }
    )
    vl_aliquota: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlAliquota",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    sub_item_list: Optional["TcServicoAeitem.SubItemList"] = field(
        default=None,
        metadata={
            "name": "subItemList",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class SubItemList:
        sub_item: List[TcServicoAeSubItem] = field(
            default_factory=list,
            metadata={
                "name": "subItem",
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
    nm_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
        }
    )
    ds_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEmail",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "pattern": r"[\w\-_]+(\.[\w\-_]+)*@(([\w\-]{2,63}\.)+[A-Za-z]{2,6}|\[\d{1,3}(\.\d{1,3}){3}\])",
        }
    )
    nr_inscricao_estadual: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoEstadual",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 20,
        }
    )
    nr_inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoMunicipal",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,10}",
        }
    )
    ds_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsEndereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nr_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrEndereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
        }
    )
    ds_complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsComplemento",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 40,
        }
    )
    nm_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmBairro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 25,
        }
    )
    nr_cidade_ibge: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrCidadeIbge",
            "type": "Element",
            "namespace": "",
        }
    )
    nm_uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmUf",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 2,
        }
    )
    nm_cidade_estrangeira: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmCidadeEstrangeira",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
        }
    )
    nm_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "nmPais",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    nr_cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrCep",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8}",
        }
    )
    nr_telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrTelefone",
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

    nr_versao_layout: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrVersaoLayout",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_mes_competencia: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrMesCompetencia",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "1",
            "max_inclusive": "12",
            "pattern": r"[0-9]{1,2}",
        }
    )
    nr_ano_competencia: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrAnoCompetencia",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{4}",
        }
    )
    nr_cnpj_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrCnpjPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 20,
        }
    )
    nr_inscricao_municipal_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrInscricaoMunicipalPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,10}",
        }
    )
    is_optante_simples_nacional: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isOptanteSimplesNacional",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dt_enquadramento_simples_nacional: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dtEnquadramentoSimplesNacional",
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

    nr_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nr_emissor_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrEmissorRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dt_emissao_rps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dtEmissaoRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    st_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "stRps",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    tp_tributacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpTributacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[1-4]{1}",
        }
    )
    nr_cidade_ibge_servico: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrCidadeIbgeServico",
            "type": "Element",
            "namespace": "",
        }
    )
    is_iss_retido: Optional[str] = field(
        default=None,
        metadata={
            "name": "isIssRetido",
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
    lista_servicos: Optional["TcRps.ListaServicos"] = field(
        default=None,
        metadata={
            "name": "listaServicos",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    vl_total_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlTotalRps",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 18,
            "pattern": r"((\d){1,18})|((\d){1,16}\.(\d){1,2})|((\d){0,16}\.(\d){1,2})",
        }
    )
    vl_liquido_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlLiquidoRps",
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
    ds_impostos: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsImpostos",
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
