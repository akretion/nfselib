from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe/tipos"


@dataclass
class TpCpfcnpj:
    """
    Tipo que representa um CPF/CNPJ.
    """
    class Meta:
        name = "tpCPFCNPJ"

    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0}|[0-9]{11}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{14}",
        }
    )


@dataclass
class TpChaveNfe:
    """
    Chave de identificação da NFS-e.

    :ivar inscricao_prestador: Inscrição municipal do prestador de
        serviços.
    :ivar numero_nfe: Número da NFS-e.
    :ivar codigo_verificacao: Código de verificação da NFS-e.
    """
    class Meta:
        name = "tpChaveNFe"

    inscricao_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{8,8}",
        }
    )
    numero_nfe: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNFe",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "",
            "min_length": 8,
            "max_length": 8,
            "white_space": "collapse",
        }
    )


@dataclass
class TpChaveRps:
    """
    Tipo que define a chave identificadora de um RPS.

    :ivar inscricao_prestador: Inscrição municipal do prestador de
        serviços.
    :ivar serie_rps: Série do RPS.
    :ivar numero_rps: Número do RPS.
    """
    class Meta:
        name = "tpChaveRPS"

    inscricao_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{8,8}",
        }
    )
    serie_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "SerieRPS",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    numero_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        }
    )


@dataclass
class TpEndereco:
    """
    Tipo Endereço.
    """
    class Meta:
        name = "tpEndereco"

    tipo_logradouro: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoLogradouro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 3,
            "white_space": "collapse",
        }
    )
    logradouro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Logradouro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 50,
            "white_space": "collapse",
        }
    )
    numero_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroEndereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    complemento_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComplementoEndereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "collapse",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "collapse",
        }
    )
    cidade: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cidade",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{7}",
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "",
            "min_length": 2,
            "max_length": 2,
            "white_space": "collapse",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{7,8}",
        }
    )


class TpOpcaoSimples(Enum):
    """
    Tipo referente às possíveis opções de escolha pelo Simples.

    :cvar VALUE_0: Não-optante pelo Simples Federal nem Municipal.
    :cvar VALUE_1: Optante pelo Simples Federal (Alíquota de 1,0%).
    :cvar VALUE_2: Optante pelo Simples Federal (Alíquota de 0,5%).
    :cvar VALUE_3: Optante pelo Simples Municipal.
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TpStatusNfe(Enum):
    """
    Tipo referente aos possíveis status de NFS-e.

    :cvar N: Normal.
    :cvar C: Cancelada.
    :cvar E: Extraviada.
    """
    N = "N"
    C = "C"
    E = "E"


class TpTipoRps(Enum):
    """
    Tipo referente aos possíveis tipos de RPS.

    :cvar RPS: Recibo Provisório de Serviços.
    :cvar RPS_M: Recibo Provisório de Serviços proveniente de Nota
        Fiscal Conjugada (Mista).
    :cvar RPS_C: Cupom.
    """
    RPS = "RPS"
    RPS_M = "RPS-M"
    RPS_C = "RPS-C"


@dataclass
class TpChaveNfeRps:
    """
    Tipo que representa a chave de uma NFS-e e a Chave do RPS que a mesma
    substitui.

    :ivar chave_nfe: Chave da NFS-e gerada.
    :ivar chave_rps: Chave do RPS substituído.
    """
    class Meta:
        name = "tpChaveNFeRPS"

    chave_nfe: Optional[TpChaveNfe] = field(
        default=None,
        metadata={
            "name": "ChaveNFe",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    chave_rps: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "name": "ChaveRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TpEvento:
    """
    :ivar codigo: Código do evento.
    :ivar descricao: Descrição do enveto.
    :ivar chave_rps: Chave do RPS.
    :ivar chave_nfe: Chave da NFe.
    """
    class Meta:
        name = "tpEvento"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{3,4}",
        }
    )
    descricao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Descricao",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 300,
            "white_space": "collapse",
        }
    )
    chave_rps: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "name": "ChaveRPS",
            "type": "Element",
            "namespace": "",
        }
    )
    chave_nfe: Optional[TpChaveNfe] = field(
        default=None,
        metadata={
            "name": "ChaveNFe",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpInformacoesLote:
    """
    Informações do lote processado.

    :ivar numero_lote: Número de lote.
    :ivar inscricao_prestador: Inscrição municipal do prestador dos RPS
        contidos no lote.
    :ivar cpfcnpjremetente: CNPJ do remetente autorizado a transmitir a
        mensagem XML.
    :ivar data_envio_lote: Data/hora de envio do lote.
    :ivar qtd_notas_processadas: Quantidade de RPS do lote.
    :ivar tempo_processamento: Tempo de processamento do lote.
    :ivar valor_total_servicos: Valor total dos serviços dos RPS
        contidos na mensagem XML.
    :ivar valor_total_deducoes: Valor total das deduções dos RPS
        contidos na mensagem XML.
    """
    class Meta:
        name = "tpInformacoesLote"

    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        }
    )
    inscricao_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{8,8}",
        }
    )
    cpfcnpjremetente: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "name": "CPFCNPJRemetente",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    data_envio_lote: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEnvioLote",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    qtd_notas_processadas: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdNotasProcessadas",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        }
    )
    tempo_processamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "TempoProcessamento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        }
    )
    valor_total_servicos: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorTotalServicos",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_total_deducoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorTotalDeducoes",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class TpNfe:
    """
    Tipo que representa uma NFS-e.

    :ivar assinatura: Assinatura digital da NFS-e.
    :ivar chave_nfe: Chave de identificação da NFS-e.
    :ivar data_emissao_nfe: Data de emissão da NFS-e
    :ivar numero_lote: Número de lote gerador da NFS-e.
    :ivar chave_rps: Chave do RPS que originou a NFS-e.
    :ivar tipo_rps: Tipo do RPS emitido.
    :ivar data_emissao_rps: Data de emissão do RPS que originou a NFS-e.
    :ivar cpfcnpjprestador: CPF/CNPJ do Prestador do serviço.
    :ivar razao_social_prestador: Nome/Razão Social do Prestador.
    :ivar endereco_prestador: Endereço do Prestador.
    :ivar email_prestador: E-mail do Prestador.
    :ivar status_nfe: Status da NFS-e.
    :ivar data_cancelamento: Data de cancelamento da NFS-e.
    :ivar tributacao_nfe: Tributação da NFS-e.
    :ivar opcao_simples: Opção pelo Simples.
    :ivar numero_guia: Número da guia vinculada a NFS-e.
    :ivar data_quitacao_guia: Data de quitação da guia vinculada a
        NFS-e.
    :ivar valor_servicos: Valor dos serviços prestados.
    :ivar valor_deducoes: Valor das deduções.
    :ivar valor_pis: Valor da retenção do PIS.
    :ivar valor_cofins: Valor da retenção do COFINS.
    :ivar valor_inss: Valor da retenção do INSS.
    :ivar valor_ir: Valor da retenção do IR.
    :ivar valor_csll: Valor da retenção do CSLL.
    :ivar codigo_servico: Código do serviço.
    :ivar aliquota_servicos: Valor da alíquota.
    :ivar valor_iss: Valor do ISS.
    :ivar valor_credito: Valor do crédito gerado.
    :ivar issretido: Retenção do ISS.
    :ivar cpfcnpjtomador: CPF/CNPJ do tomador do serviço.
    :ivar inscricao_municipal_tomador: Inscrição Municipal do Tomador.
    :ivar inscricao_estadual_tomador: Inscrição Estadual do tomador.
    :ivar razao_social_tomador: Nome/Razão Social do tomador.
    :ivar endereco_tomador: Endereço do tomador.
    :ivar email_tomador: E-mail do tomador.
    :ivar cpfcnpjintermediario: CNPJ do intermediário de serviço.
    :ivar inscricao_municipal_intermediario: Inscrição Municipal do
        intermediário de serviço.
    :ivar issretido_intermediario: Retenção do ISS pelo intermediário de
        serviço.
    :ivar email_intermediario: E-mail do intermediário de serviço.
    :ivar discriminacao: Descrição dos serviços.
    :ivar valor_carga_tributaria: Valor da carga tributária total em R$.
    :ivar percentual_carga_tributaria: Valor percentual da carga
        tributária.
    :ivar fonte_carga_tributaria: Fonte de informação da carga
        tributária.
    :ivar codigo_cei: Código do CEI – Cadastro específico do INSS.
    :ivar matricula_obra: Código que representa a matrícula da obra no
        sistema de cadastro de obras.
    :ivar municipio_prestacao: Código da cidade do município da
        prestação do serviço.
    :ivar numero_encapsulamento: Código que representa o número do
        encapsulamento.
    """
    class Meta:
        name = "tpNFe"

    assinatura: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Assinatura",
            "type": "Element",
            "namespace": "",
            "format": "base64",
        }
    )
    chave_nfe: Optional[TpChaveNfe] = field(
        default=None,
        metadata={
            "name": "ChaveNFe",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    data_emissao_nfe: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissaoNFe",
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
            "pattern": r"[0-9]{1,12}",
        }
    )
    chave_rps: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "name": "ChaveRPS",
            "type": "Element",
            "namespace": "",
        }
    )
    tipo_rps: Optional[TpTipoRps] = field(
        default=None,
        metadata={
            "name": "TipoRPS",
            "type": "Element",
            "namespace": "",
        }
    )
    data_emissao_rps: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRPS",
            "type": "Element",
            "namespace": "",
        }
    )
    cpfcnpjprestador: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "name": "CPFCNPJPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    razao_social_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocialPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        }
    )
    endereco_prestador: Optional[TpEndereco] = field(
        default=None,
        metadata={
            "name": "EnderecoPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    email_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPrestador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        }
    )
    status_nfe: Optional[TpStatusNfe] = field(
        default=None,
        metadata={
            "name": "StatusNFe",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    data_cancelamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataCancelamento",
            "type": "Element",
            "namespace": "",
        }
    )
    tributacao_nfe: Optional[str] = field(
        default=None,
        metadata={
            "name": "TributacaoNFe",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1,
            "white_space": "collapse",
        }
    )
    opcao_simples: Optional[TpOpcaoSimples] = field(
        default=None,
        metadata={
            "name": "OpcaoSimples",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    numero_guia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroGuia",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_quitacao_guia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataQuitacaoGuia",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_servicos: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_deducoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorPIS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCOFINS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorINSS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_ir: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIR",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCSLL",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    codigo_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{4,5}",
        }
    )
    aliquota_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaServicos",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        }
    )
    valor_iss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorISS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_credito: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    issretido: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ISSRetido",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cpfcnpjtomador: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "name": "CPFCNPJTomador",
            "type": "Element",
            "namespace": "",
        }
    )
    inscricao_municipal_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalTomador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8,8}",
        }
    )
    inscricao_estadual_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoEstadualTomador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,19}",
        }
    )
    razao_social_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocialTomador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        }
    )
    endereco_tomador: Optional[TpEndereco] = field(
        default=None,
        metadata={
            "name": "EnderecoTomador",
            "type": "Element",
            "namespace": "",
        }
    )
    email_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailTomador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        }
    )
    cpfcnpjintermediario: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "name": "CPFCNPJIntermediario",
            "type": "Element",
            "namespace": "",
        }
    )
    inscricao_municipal_intermediario: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalIntermediario",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8,8}",
        }
    )
    issretido_intermediario: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSRetidoIntermediario",
            "type": "Element",
            "namespace": "",
        }
    )
    email_intermediario: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailIntermediario",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    valor_carga_tributaria: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCargaTributaria",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    percentual_carga_tributaria: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PercentualCargaTributaria",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 7,
            "fraction_digits": 4,
        }
    )
    fonte_carga_tributaria: Optional[str] = field(
        default=None,
        metadata={
            "name": "FonteCargaTributaria",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    codigo_cei: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCEI",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        }
    )
    matricula_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "MatriculaObra",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        }
    )
    municipio_prestacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "MunicipioPrestacao",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{7}",
        }
    )
    numero_encapsulamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroEncapsulamento",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        }
    )


@dataclass
class TpRps:
    """
    Tipo que representa um RPS.

    :ivar assinatura: Assinatura digital do RPS.
    :ivar chave_rps: Informe a chave do RPS emitido.
    :ivar tipo_rps: Informe o Tipo do RPS emitido.
    :ivar data_emissao: Informe a Data de emissão do RPS.
    :ivar status_rps: Informe o Status do RPS.
    :ivar tributacao_rps: Informe o tipo de tributação do RPS.
    :ivar valor_servicos: Informe o valor dos serviços prestados.
    :ivar valor_deducoes: Informe o valor das deduções.
    :ivar valor_pis: Informe o valor da retenção do PIS.
    :ivar valor_cofins: Informe o valor da retenção do COFINS.
    :ivar valor_inss: Informe o valor da retenção do INSS.
    :ivar valor_ir: Informe o valor da retenção do IR.
    :ivar valor_csll: Informe o valor da retenção do CSLL.
    :ivar codigo_servico: Informe o código do serviço do RPS. Este
        código deve pertencer à lista de serviços.
    :ivar aliquota_servicos: Informe o valor da alíquota. Obs. O
        conteúdo deste campo será ignorado caso a tributação ocorra no
        município (Situação do RPS = T ).
    :ivar issretido: Informe a retenção.
    :ivar cpfcnpjtomador: Informe o CPF/CNPJ do tomador do serviço. O
        conteúdo deste campo será ignorado caso o campo
        InscricaoMunicipalTomador esteja preenchido.
    :ivar inscricao_municipal_tomador: Informe a Inscrição Municipal do
        Tomador. ATENÇÃO: Este campo só deverá ser preenchido para
        tomadores estabelecidos no município de São Paulo (CCM). Quando
        este campo for preenchido, seu conteúdo será considerado como
        prioritário com relação ao campo de CPF/CNPJ do Tomador, sendo
        utilizado para identificar o Tomador e recuperar seus dados da
        base de dados da Prefeitura.
    :ivar inscricao_estadual_tomador: Informe a inscrição estadual do
        tomador. Este campo será ignorado caso seja fornecido um
        CPF/CNPJ ou a Inscrição Municipal do tomador pertença ao
        município de São Paulo.
    :ivar razao_social_tomador: Informe o Nome/Razão Social do tomador.
        Este campo é obrigatório apenas para tomadores Pessoa Jurídica
        (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ
        ou a Inscrição Municipal do tomador pertença ao município de São
        Paulo.
    :ivar endereco_tomador: Informe o endereço do tomador. Os campos do
        endereço são obrigatórios apenas para tomadores pessoa jurídica
        (CNPJ informado). O conteúdo destes campos será ignorado caso
        seja fornecido um CPF/CNPJ ou a Inscrição Municipal do tomador
        pertença ao município de São Paulo.
    :ivar email_tomador: Informe o e-mail do tomador.
    :ivar cpfcnpjintermediario: CNPJ do intermediário de serviço.
    :ivar inscricao_municipal_intermediario: Inscrição Municipal do
        intermediário de serviço.
    :ivar issretido_intermediario: Retenção do ISS pelo intermediário de
        serviço.
    :ivar email_intermediario: E-mail do intermediário de serviço.
    :ivar discriminacao: Informe a discriminação dos serviços.
    :ivar valor_carga_tributaria: Valor da carga tributária total em R$.
    :ivar percentual_carga_tributaria: Valor percentual da carga
        tributária.
    :ivar fonte_carga_tributaria: Fonte de informação da carga
        tributária.
    :ivar codigo_cei: Código do CEI – Cadastro específico do INSS.
    :ivar matricula_obra: Código que representa a matrícula da obra no
        sistema de cadastro de obras.
    :ivar municipio_prestacao: Código da cidade do município da
        prestação do serviço.
    :ivar numero_encapsulamento: Código que representa o número do
        encapsulamento da obra.
    """
    class Meta:
        name = "tpRPS"

    assinatura: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Assinatura",
            "type": "Element",
            "namespace": "",
            "required": True,
            "format": "base64",
        }
    )
    chave_rps: Optional[TpChaveRps] = field(
        default=None,
        metadata={
            "name": "ChaveRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tipo_rps: Optional[TpTipoRps] = field(
        default=None,
        metadata={
            "name": "TipoRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    status_rps: Optional[TpStatusNfe] = field(
        default=None,
        metadata={
            "name": "StatusRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tributacao_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "TributacaoRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 1,
            "white_space": "collapse",
        }
    )
    valor_servicos: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_deducoes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorPIS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_cofins: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCOFINS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_inss: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorINSS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_ir: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorIR",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_csll: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCSLL",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    codigo_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{4,5}",
        }
    )
    aliquota_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaServicos",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
        }
    )
    issretido: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ISSRetido",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cpfcnpjtomador: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "name": "CPFCNPJTomador",
            "type": "Element",
            "namespace": "",
        }
    )
    inscricao_municipal_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalTomador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8,8}",
        }
    )
    inscricao_estadual_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoEstadualTomador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,19}",
        }
    )
    razao_social_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocialTomador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        }
    )
    endereco_tomador: Optional[TpEndereco] = field(
        default=None,
        metadata={
            "name": "EnderecoTomador",
            "type": "Element",
            "namespace": "",
        }
    )
    email_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailTomador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        }
    )
    cpfcnpjintermediario: Optional[TpCpfcnpj] = field(
        default=None,
        metadata={
            "name": "CPFCNPJIntermediario",
            "type": "Element",
            "namespace": "",
        }
    )
    inscricao_municipal_intermediario: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalIntermediario",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{8,8}",
        }
    )
    issretido_intermediario: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSRetidoIntermediario",
            "type": "Element",
            "namespace": "",
        }
    )
    email_intermediario: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailIntermediario",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 75,
            "white_space": "collapse",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    valor_carga_tributaria: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorCargaTributaria",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    percentual_carga_tributaria: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PercentualCargaTributaria",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 7,
            "fraction_digits": 4,
        }
    )
    fonte_carga_tributaria: Optional[str] = field(
        default=None,
        metadata={
            "name": "FonteCargaTributaria",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "collapse",
        }
    )
    codigo_cei: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoCEI",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        }
    )
    matricula_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "MatriculaObra",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        }
    )
    municipio_prestacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "MunicipioPrestacao",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{7}",
        }
    )
    numero_encapsulamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroEncapsulamento",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{1,12}",
        }
    )
