from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://localhost:8080/WsNFe2/tp"


class Nulo(Enum):
    """
    Definição para aceitar dado tipo nulo.
    """
    VALUE = ""


class TpAssincrono(Enum):
    """
    Tipo de processamento.

    :cvar S: Processamento Assíncrono
    :cvar N: Processamento Síncrono
    """
    S = "S"
    N = "N"


@dataclass
class TpBairroCompleto:
    """
    Informações do Bairro com o seu Tipo.

    :ivar tipo_bairro: Tipo do Bairro (Bairro, Vila etc)
    :ivar nome_bairro: Nome do Bairro.
    """
    class Meta:
        name = "tpBairroCompleto"

    tipo_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoBairro",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    nome_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeBairro",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )


@dataclass
class TpCpfcnpj2:
    """
    Tipo que representa um CPF/CNPJ.
    """
    class Meta:
        name = "tpCPFCNPJ2"

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
    Chave de identificação da NF-e.

    :ivar inscricao_prestador: Inscrição municipal do prestador de
        serviços.
    :ivar numero_nfe: Número da NF-e.
    :ivar codigo_verificacao: Código de verificação da NF-e.
    :ivar razao_social_prestador: Razão Social do Prestador do RPS.
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
            "pattern": r"[0-9]{6,11}",
        }
    )
    numero_nfe: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNFe",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    razao_social_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocialPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        }
    )


@dataclass
class TpChaveSubstituicaoNfse:
    """
    Chave de identificação para Substituição de uma NFSe.

    :ivar inscricao_prestador: Inscrição municipal do prestador de
        serviços.
    :ivar cpfcnpjtomador: CPF/CNPJ do Tomador.
    :ivar numero_nfse_substituida: Número da NFSe a ser substituida.
    :ivar data_emissao_nfse_substituida: Data da Emissão da NFSe a ser
        substituida.
    """
    class Meta:
        name = "tpChaveSubstituicaoNFSe"

    inscricao_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    cpfcnpjtomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPFCNPJTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{11}|[0-9]{14}",
        }
    )
    numero_nfse_substituida: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNFSeSubstituida",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_emissao_nfse_substituida: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DataEmissaoNFSeSubstituida",
            "type": "Element",
            "namespace": "",
            "required": True,
            "white_space": "collapse",
        }
    )


class TpDeducaoPor(Enum):
    """
    Tipo que representa o modo de Dedução.

    :cvar VALOR: Dedução por valor em R$
    :cvar PERCENTUAL: Dedução por percentual do valor total de serviços
    """
    VALOR = "Valor"
    PERCENTUAL = "Percentual"


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
            "max_length": 10,
            "white_space": "preserve",
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
            "white_space": "preserve",
        }
    )
    numero_endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroEndereco",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 9,
            "white_space": "preserve",
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
            "white_space": "preserve",
        }
    )
    tipo_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoBairro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )
    cidade: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cidade",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]",
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
            "pattern": r"[0-9]{0,8}",
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
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
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
            "pattern": r"[0-9]{6,11}",
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
    data_envio_lote: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEnvioLote",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    qtd_notas_processadas: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "QtdNotasProcessadas",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 10,
            "fraction_digits": 4,
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


class TpItemTributavel(Enum):
    """
    Informa se o Item de serviço é tributavel ou nao.

    :cvar S: Sim - Item tributável
    :cvar N: Item não tributável
    """
    S = "S"
    N = "N"


@dataclass
class TpLogradouroCompleto:
    """
    Informações do Logradouro com o seu Tipo.

    :ivar tipo_logradouro: Tipo do Logradouro (Rua, Avenida etc)
    :ivar nome_logradouro: Nome do Logradouro.
    """
    class Meta:
        name = "tpLogradouroCompleto"

    tipo_logradouro: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoLogradouro",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    nome_logradouro: Optional[str] = field(
        default=None,
        metadata={
            "name": "NomeLogradouro",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )


class TpMetodoEnvio(Enum):
    """
    Metodo de Envio.

    :cvar WS: Web Service
    :cvar DLL: Componente RPS - DLL.
    :cvar DMS: Sistema DMS.
    """
    WS = "WS"
    DLL = "DLL"
    DMS = "DMS"


@dataclass
class TpNotaCancelamentoNfse:
    """
    Tipo Detalhes do Cancelamento de NFSe.

    :ivar inscricao_municipal_prestador: Inscrição municipal do
        prestador de serviços.
    :ivar numero_nota: Número da NF-e.
    :ivar codigo_verificacao: Código de verificação da NF-e.
    :ivar motivo_cancelamento: Motivo do Cancelamento da Nota Fiscal.
    :ivar id:
    """
    class Meta:
        name = "tpNotaCancelamentoNFSe"

    inscricao_municipal_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    numero_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNota",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    motivo_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "MotivoCancelamento",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 80,
            "white_space": "preserve",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TpNotaConsultaNfse:
    """
    Tipo Detalhes da Nota da Consulta de NFSe.

    :ivar inscricao_municipal_prestador: Inscrição municipal do
        prestador de serviços.
    :ivar numero_nota: Número da NF-e.
    :ivar codigo_verificacao: Código de verificação da NF-e.
    :ivar id:
    """
    class Meta:
        name = "tpNotaConsultaNFSe"

    inscricao_municipal_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    numero_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNota",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
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


class TpOperacao(Enum):
    """
    Tipo Operação.

    :cvar A: Sem Dedução.
    :cvar B: Com Dedução/Materiais.
    :cvar C: Imune/Isenta de ISSQN
    :cvar D: Devolução/Simples Remessa.
    :cvar J: Intermediação.
    """
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    J = "J"


@dataclass
class TpRpsconsultaNfse:
    """
    Tipo Detalhes do RPSSe.

    :ivar inscricao_municipal_prestador: Inscrição municipal do
        prestador de serviços.
    :ivar numero_rps: Número RPS.
    :ivar serie_prestacao: Serie RPS.
    :ivar id:
    """
    class Meta:
        name = "tpRPSConsultaNFSe"

    inscricao_municipal_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    numero_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    serie_prestacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeriePrestacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


class TpSerieRps(Enum):
    """
    Tipo série de documento.

    :cvar NF: Nota Fiscal de Servicos
    """
    NF = "NF"


class TpSerieRpssubstituido(Enum):
    """
    Tipo série de documento.

    :cvar NF: Nota Fiscal de Servicos
    :cvar VALUE:
    """
    NF = "NF"
    VALUE = ""


class TpSituacaoRps(Enum):
    """
    Tipo referente aos possíveis status de RPS.

    :cvar N: Normal.
    :cvar C: Cancelado.
    """
    N = "N"
    C = "C"


class TpStatusNfe(Enum):
    """
    Tipo referente aos possíveis status de NFSe.

    :cvar VALUE_1: Normal.
    :cvar VALUE_2: Cancelada.
    :cvar VALUE_3: Substituída
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TpTipoDeducao(Enum):
    """
    Tipo que representa as descrições das deduções permitidas.

    :cvar DESPESAS_COM_MATERIAIS: Despesas com Materiais.
    :cvar DESPESAS_COM_SUBEMPREITADA: Despesas com Subempreitada.
    :cvar DESPESAS_COM_MERCADORIAS: Despesas com Mercadorias.
    :cvar SERVICOS_DE_VEICULACAO_E_DIVULGACAO: Servicos de Veiculacao e
        Divulgacao
    :cvar SERVICOS: Outros Servicos que permitem dedução. Ex.
        Intermediação de Serviços, quando em uma nota existe um
        intermediário.
    :cvar MAPA_DE_CONST_CIVIL: Mapa de construção civil.
    :cvar VALUE:
    """
    DESPESAS_COM_MATERIAIS = "Despesas com Materiais"
    DESPESAS_COM_SUBEMPREITADA = "Despesas com Subempreitada"
    DESPESAS_COM_MERCADORIAS = "Despesas com Mercadorias"
    SERVICOS_DE_VEICULACAO_E_DIVULGACAO = "Servicos de Veiculacao e Divulgacao"
    SERVICOS = "Servicos"
    MAPA_DE_CONST_CIVIL = "Mapa de Const. Civil"
    VALUE = ""


class TpTipoRps(Enum):
    """
    Tipo referente aos possíveis tipos de RPS.

    :cvar RPS: Recibo Provisório de Serviços.
    """
    RPS = "RPS"


class TpTipoRecolhimento(Enum):
    """
    Tipo referente ao recolhimento.

    :cvar A: A Recolher.
    :cvar R: Retido na Fonte.
    """
    A = "A"
    R = "R"


class TpTributacao(Enum):
    """
    Tipo referente aos modos de tributação.

    :cvar C: Isenta de ISS.
    :cvar F: Imune.
    :cvar K: Depósito em Juízo.
    :cvar E: Não Incidente no Município.
    :cvar T: Tributável
    :cvar H: Tributável Simples Nacional.
    :cvar G: Tributável Fixo.
    :cvar N: Não Tributável.
    :cvar M: Tributação Microempresário Individual (MEI)
    """
    C = "C"
    F = "F"
    K = "K"
    E = "E"
    T = "T"
    H = "H"
    G = "G"
    N = "N"
    M = "M"


class TpTributacaoNfe(Enum):
    """
    Tipo referente aos modos de tributação da NFe.

    :cvar T: Tributação no municipio de São Paulo.
    :cvar F: Tributação fora do municipio
    :cvar I: Isento.
    :cvar J: ISS Suspenso por Decisão Judicial.
    """
    T = "T"
    F = "F"
    I = "I"
    J = "J"


@dataclass
class TpChaveRps:
    """
    Tipo que define a chave identificadora de um RPS.

    :ivar inscricao_prestador: Inscrição municipal do prestador de
        serviços.
    :ivar serie_rps: Série do RPS.
    :ivar numero_rps: Número do RPS.
    :ivar data_emissao_rps: Data de Emissao do RPS.
    :ivar razao_social_prestador: Razão Social do Prestador do RPS.
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
            "pattern": r"[0-9]{6,11}",
        }
    )
    serie_rps: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "name": "SerieRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    numero_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_emissao_rps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRPS",
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
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        }
    )


@dataclass
class TpConsultaNfse:
    """
    NFSe de retorno de consulta.

    :ivar inscricao_prestador: Inscrição municipal do prestador de
        serviços.
    :ivar numero_nfe: Número da NF-e.
    :ivar codigo_verificacao: Código de verificação da NF-e.
    :ivar serie_rps: Série do RPS.
    :ivar numero_rps: Número do RPS.
    :ivar data_emissao_rps: Data de Emissão do RPS.
    :ivar razao_social_prestador: Razão Social do Prestador do Serviço.
    :ivar tipo_recolhimento: Tipo do Recolhimento do Serviço.
    :ivar valor_deduzir: Valor total de deduções.
    :ivar valor_total: Valor total de Itens de Nota.
    :ivar aliquota: Valor total de Itens de Nota.
    """
    class Meta:
        name = "tpConsultaNFSe"

    inscricao_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    numero_nfe: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNFe",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    serie_rps: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "name": "SerieRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    numero_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_emissao_rps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRPS",
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
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        }
    )
    tipo_recolhimento: Optional[TpTipoRecolhimento] = field(
        default=None,
        metadata={
            "name": "TipoRecolhimento",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    valor_deduzir: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorDeduzir",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    valor_total: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorTotal",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )


@dataclass
class TpDeducoes:
    """
    Tipo deduções de nota fiscal.
    """
    class Meta:
        name = "tpDeducoes"

    deducao_por: Optional[TpDeducaoPor] = field(
        default=None,
        metadata={
            "name": "DeducaoPor",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tipo_deducao: Optional[TpTipoDeducao] = field(
        default=None,
        metadata={
            "name": "TipoDeducao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cpfcnpjreferencia: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "CPFCNPJReferencia",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{11}|[0-9]{14}",
        }
    )
    numero_nfreferencia: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNFReferencia",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "pattern": r"[0-9]{1,10}",
        }
    )
    valor_total_referencia: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorTotalReferencia",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    percentual_deduzir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PercentualDeduzir",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
    valor_deduzir: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorDeduzir",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )


@dataclass
class TpDetalhesConsultaRps:
    """
    Tipo Detalhes da Consulta de RPS.

    :ivar inscricao_prestador: Inscrição municipal do prestador de
        serviços.
    :ivar serie_rps: Série do RPS.
    :ivar numero_rps: Número do RPS.
    """
    class Meta:
        name = "tpDetalhesConsultaRPS"

    inscricao_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    serie_rps: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "name": "SerieRPS",
            "type": "Element",
            "namespace": "",
        }
    )
    numero_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )


@dataclass
class TpItens:
    """
    Tipo Itens de Nota Fiscal.
    """
    class Meta:
        name = "tpItens"

    discriminacao_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscriminacaoServico",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 250,
            "white_space": "preserve",
        }
    )
    quantidade: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Quantidade",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 10,
            "fraction_digits": 4,
        }
    )
    valor_unitario: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorUnitario",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 4,
        }
    )
    valor_total: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorTotal",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    tributavel: Optional[TpItemTributavel] = field(
        default=None,
        metadata={
            "name": "Tributavel",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpLoteCancelamentoNfse:
    """
    Lista de Detalhes do Cancelamento de NFSe.
    """
    class Meta:
        name = "tpLoteCancelamentoNFSe"

    nota: List[TpNotaCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "name": "Nota",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TpNotasCancelamentoNfse:
    """
    Lista de Detalhes do Cancelamento de NFSe.
    """
    class Meta:
        name = "tpNotasCancelamentoNFSe"

    nota: List[TpNotaCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "name": "Nota",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        }
    )


@dataclass
class TpNotasConsultaNfse:
    """
    Lista de Detalhes da Consulta de NFSe.
    """
    class Meta:
        name = "tpNotasConsultaNFSe"

    nota: List[TpNotaConsultaNfse] = field(
        default_factory=list,
        metadata={
            "name": "Nota",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        }
    )


@dataclass
class TpRpssConsultaNfse:
    """
    Lista de Detalhes da Consulta de NFSe.
    """
    class Meta:
        name = "tpRPSsConsultaNFSe"

    rps: List[TpRpsconsultaNfse] = field(
        default_factory=list,
        metadata={
            "name": "RPS",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        }
    )


@dataclass
class TpRetornoNotasCancelamentoNfse:
    """
    Lista de Detalhes do Cancelamento de NFSe.
    """
    class Meta:
        name = "tpRetornoNotasCancelamentoNFSe"

    nota: List[TpNotaCancelamentoNfse] = field(
        default_factory=list,
        metadata={
            "name": "Nota",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpChaveNfeRps:
    """
    Tipo que representa a chave de uma NFSe e a Chave do RPS que a mesma
    substitui.

    :ivar chave_nfe: Chave da NFSe gerada.
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
class TpListaDeducoes:
    """
    Deduções.
    """
    class Meta:
        name = "tpListaDeducoes"

    deducao: List[TpDeducoes] = field(
        default_factory=list,
        metadata={
            "name": "Deducao",
            "type": "Element",
            "namespace": "",
            "max_occurs": 200,
        }
    )


@dataclass
class TpListaDetalhesConsultaRps:
    """
    Lista de Detalhes da Consulta RPS.
    """
    class Meta:
        name = "tpListaDetalhesConsultaRPS"

    detalhe: List[TpDetalhesConsultaRps] = field(
        default_factory=list,
        metadata={
            "name": "Detalhe",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 50,
        }
    )


@dataclass
class TpListaItens:
    """
    Itens de Serviço.
    """
    class Meta:
        name = "tpListaItens"

    item: List[TpItens] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 25,
        }
    )


@dataclass
class TpListaNfse:
    """
    Lista de NFSE consultada.
    """
    class Meta:
        name = "tpListaNFSe"

    consulta_nfse: List[TpConsultaNfse] = field(
        default_factory=list,
        metadata={
            "name": "ConsultaNFSe",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpLoteConsultaNfse:
    """
    Lista de Detalhes da Consulta de NFSe.
    """
    class Meta:
        name = "tpLoteConsultaNFSe"

    nota_consulta: Optional[TpNotasConsultaNfse] = field(
        default=None,
        metadata={
            "name": "NotaConsulta",
            "type": "Element",
            "namespace": "",
        }
    )
    rpsconsulta: Optional[TpRpssConsultaNfse] = field(
        default=None,
        metadata={
            "name": "RPSConsulta",
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TpListaAlertas:
    """
    Alertas.
    """
    class Meta:
        name = "tpListaAlertas"

    alerta: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "name": "Alerta",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpListaErros:
    """
    Erros.
    """
    class Meta:
        name = "tpListaErros"

    erro: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "name": "Erro",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpListaNfseRps:
    """
    NFSE e seu respectivo RPS.
    """
    class Meta:
        name = "tpListaNFSeRPS"

    chave_nfse_rps: List[TpChaveNfeRps] = field(
        default_factory=list,
        metadata={
            "name": "ChaveNFSeRPS",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpNfse:
    """
    Tipo que representa uma NFSe.

    :ivar numero_nota: Número da Nota Fiscal
    :ivar data_processamento: Data que a Nota Fiscal foi Processada
    :ivar numero_lote: Número do Lote
    :ivar codigo_verificacao: Código de Verificacao
    :ivar assinatura: Assinatura digital do RPS.
    :ivar inscricao_municipal_prestador: Informe a Inscrição Municipal
        do Prestador
    :ivar razao_social_prestador: Informe a Razao Social do Prestador
    :ivar tipo_rps: Informe o Tipo do RPS emitido.
    :ivar serie_rps: Informe a Série do RPS emitido.
    :ivar numero_rps: Informe o Número do RPS emitido.
    :ivar data_emissao_rps: Informe a Data de emissão do RPS.
    :ivar situacao_rps: Informe o Status do RPS.
    :ivar serie_rpssubstituido: Informe a Série do RPS substituído.
    :ivar numero_rpssubstituido: Informe o Número do RPS substituído.
    :ivar numero_nfse_substituida: Informe o Número da NFSe substituída.
    :ivar data_emissao_nfse_substituida: Informe a Data de Emissão da
        NFSe substituída.
    :ivar serie_prestacao: Série de prestação
    :ivar inscricao_municipal_tomador: Informe a Inscrição Municipal do
        Tomador. ATENÇÃO: Este campo só deverá ser preenchido para
        tomadores estabelecidos no município. Quando este campo for
        preenchido, seu conteúdo será considerado como prioritário com
        relação ao campo de CPF/CNPJ do Tomador, sendo utilizado para
        identificar o Tomador e recuperar seus dados da base de dados da
        Prefeitura.
    :ivar cpfcnpjtomador: Informe o CPF/CNPJ do tomador do serviço. O
        conteúdo deste campo será ignorado caso o campo
        InscricaoMunicipalTomador esteja preenchido.
    :ivar razao_social_tomador: Informe o Nome/Razão Social do tomador.
        Este campo é obrigatório apenas para tomadores Pessoa Jurídica
        (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ
        ou a Inscrição Municipal do tomador pertença ao município.
    :ivar doc_tomador_estrangeiro: Informe o Documento de Identificação
        do tomador. Este campo é obrigatório apenas para tomadores
        estrageiros, ou seja quando no CidadeTomador que indica o Codigo
        SIAFI da cidade do tomador for informado 0009999
    :ivar tipo_logradouro_tomador: Informe o Tipo do Logradouro do
        Endereço do Tomador.
    :ivar logradouro_tomador: Informe o Logradouro do Endereço do
        Tomador.
    :ivar numero_endereco_tomador: Informe o Número do Endereço do
        Tomador.
    :ivar complemento_endereco_tomador: Informe o Comlpemento do
        Endereço do Tomador.
    :ivar tipo_bairro_tomador: Informe o Tipo do Bairro do Endereço do
        Tomador.
    :ivar bairro_tomador: Informe o Bairro do Endereço do Tomador.
    :ivar cidade_tomador: Informe a Cidade do Tomador.
    :ivar cidade_tomador_descricao: Informe a Descricao Cidade do
        Tomador.
    :ivar ceptomador: Informe o CEP do Tomador.
    :ivar email_tomador: Informe o e-mail do tomador.
    :ivar codigo_atividade: Informe o código da atividade do RPS. Este
        código deve pertencer à lista CNAE.
    :ivar aliquota_atividade: Informe o valor da alíquota.
    :ivar tipo_recolhimento: Informe a retenção.
    :ivar municipio_prestacao: Informe o Município da Prestação do
        Serviço.
    :ivar municipio_prestacao_descricao: Informe o Município da
        Prestação do Serviço.
    :ivar operacao: Informe a Operação da Prestação do Serviço.
    :ivar tributacao: Informe o tipo de tributação do RPS.
    :ivar valor_pis: Informe o valor da retenção do PIS.
    :ivar valor_cofins: Informe o valor da retenção do COFINS.
    :ivar valor_inss: Informe o valor da retenção do INSS.
    :ivar valor_ir: Informe o valor da retenção do IR.
    :ivar valor_csll: Informe o valor da retenção do CSLL.
    :ivar aliquota_pis: Informe a Alíquota da retenção do PIS.
    :ivar aliquota_cofins: Informe a Alíquota da retenção do COFINS.
    :ivar aliquota_inss: Informe a Alíquota da retenção do INSS.
    :ivar aliquota_ir: Informe a Alíquota da retenção do IR.
    :ivar aliquota_csll: Informe a Alíquota da retenção do CSLL.
    :ivar descricao_rps: Descrição da Nota.
    :ivar dddprestador: DDD do Prestador.
    :ivar telefone_prestador: Telefone do Prestador.
    :ivar dddtomador: DDD do Tomador.
    :ivar telefone_tomador: Telefone do Tomador.
    :ivar mot_cancelamento: Informe o Motivo do Cancelamento.
    :ivar cpfcnpjintermediario: CPF/CNPJ do intermediário do serviço.
        Campo não é obrigatório, deve ser informado quando houver um
        intermediário entre o tomador e o prestador.
    :ivar deducoes: Lista de Deduções.
    :ivar itens: Lista de Itens.
    """
    class Meta:
        name = "tpNFSe"

    numero_nota: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNota",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_processamento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataProcessamento",
            "type": "Element",
            "namespace": "",
        }
    )
    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    codigo_verificacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    assinatura: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Assinatura",
            "type": "Element",
            "namespace": "",
            "format": "base64",
        }
    )
    inscricao_municipal_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    razao_social_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocialPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
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
    serie_rps: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "name": "SerieRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    numero_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_emissao_rps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    situacao_rps: Optional[TpSituacaoRps] = field(
        default=None,
        metadata={
            "name": "SituacaoRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    serie_rpssubstituido: Optional[TpSerieRpssubstituido] = field(
        default=None,
        metadata={
            "name": "SerieRPSSubstituido",
            "type": "Element",
            "namespace": "",
        }
    )
    numero_rpssubstituido: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPSSubstituido",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    numero_nfse_substituida: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNFSeSubstituida",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_emissao_nfse_substituida: Optional[Union[XmlDateTime, Nulo]] = field(
        default=None,
        metadata={
            "name": "DataEmissaoNFSeSubstituida",
            "type": "Element",
            "namespace": "",
        }
    )
    serie_prestacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeriePrestacao",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    inscricao_municipal_tomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalTomador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{6,11}",
        }
    )
    cpfcnpjtomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPFCNPJTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{11}|[0-9]{14}",
        }
    )
    razao_social_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocialTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        }
    )
    doc_tomador_estrangeiro: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTomadorEstrangeiro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 20,
            "white_space": "preserve",
        }
    )
    tipo_logradouro_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoLogradouroTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    logradouro_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogradouroTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )
    numero_endereco_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroEnderecoTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 9,
            "white_space": "preserve",
        }
    )
    complemento_endereco_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComplementoEnderecoTomador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        }
    )
    tipo_bairro_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoBairroTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    bairro_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "BairroTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )
    cidade_tomador: Optional[int] = field(
        default=None,
        metadata={
            "name": "CidadeTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
        }
    )
    cidade_tomador_descricao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CidadeTomadorDescricao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )
    ceptomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "CEPTomador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0,8}",
        }
    )
    email_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailTomador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 60,
            "white_space": "preserve",
        }
    )
    codigo_atividade: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoAtividade",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{9}",
        }
    )
    aliquota_atividade: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaAtividade",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    tipo_recolhimento: Optional[TpTipoRecolhimento] = field(
        default=None,
        metadata={
            "name": "TipoRecolhimento",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    municipio_prestacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "MunicipioPrestacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
        }
    )
    municipio_prestacao_descricao: Optional[str] = field(
        default=None,
        metadata={
            "name": "MunicipioPrestacaoDescricao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        }
    )
    operacao: Optional[TpOperacao] = field(
        default=None,
        metadata={
            "name": "Operacao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tributacao: Optional[TpTributacao] = field(
        default=None,
        metadata={
            "name": "Tributacao",
            "type": "Element",
            "namespace": "",
            "required": True,
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
    aliquota_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaPIS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    aliquota_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaCOFINS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    aliquota_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaINSS",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    aliquota_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaIR",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    aliquota_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaCSLL",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    descricao_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescricaoRPS",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 1500,
            "white_space": "preserve",
        }
    )
    dddprestador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "DDDPrestador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0,3}",
        }
    )
    telefone_prestador: Optional[Union[int, Nulo]] = field(
        default=None,
        metadata={
            "name": "TelefonePrestador",
            "type": "Element",
            "namespace": "",
            "max_inclusive": 99999999,
        }
    )
    dddtomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "DDDTomador",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{0,3}",
        }
    )
    telefone_tomador: Optional[Union[int, Nulo]] = field(
        default=None,
        metadata={
            "name": "TelefoneTomador",
            "type": "Element",
            "namespace": "",
            "max_inclusive": 99999999,
        }
    )
    mot_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "MotCancelamento",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "white_space": "preserve",
        }
    )
    cpfcnpjintermediario: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "CPFCNPJIntermediario",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{11}|[0-9]{14}",
        }
    )
    deducoes: Optional[TpListaDeducoes] = field(
        default=None,
        metadata={
            "name": "Deducoes",
            "type": "Element",
            "namespace": "",
        }
    )
    itens: Optional[TpListaItens] = field(
        default=None,
        metadata={
            "name": "Itens",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpRps:
    """
    Tipo que representa um RPS.

    :ivar assinatura: Assinatura digital do RPS.
    :ivar inscricao_municipal_prestador: Informe a Inscrição Municipal
        do Prestador
    :ivar razao_social_prestador: Informe a Razao Social do Prestador
    :ivar tipo_rps: Informe o Tipo do RPS emitido.
    :ivar serie_rps: Informe a Série do RPS emitido.
    :ivar numero_rps: Informe o Número do RPS emitido.
    :ivar data_emissao_rps: Informe a Data de emissão do RPS.
    :ivar situacao_rps: Informe o Status do RPS.
    :ivar serie_rpssubstituido: Informe a Série do RPS substituído.
    :ivar numero_rpssubstituido: Informe o Número do RPS substituído.
    :ivar numero_nfse_substituida: Informe o Número da NFSe substituída.
    :ivar data_emissao_nfse_substituida: Informe a Data de Emissão da
        NFSe substituída.
    :ivar serie_prestacao: Informe o Documento de Prestação
    :ivar inscricao_municipal_tomador: Informe a Inscrição Municipal do
        Tomador. ATENÇÃO: Este campo só deverá ser preenchido para
        tomadores estabelecidos no município. Quando este campo for
        preenchido, seu conteúdo será considerado como prioritário com
        relação ao campo de CPF/CNPJ do Tomador, sendo utilizado para
        identificar o Tomador e recuperar seus dados da base de dados da
        Prefeitura.
    :ivar cpfcnpjtomador: Informe o CPF/CNPJ do tomador do serviço. O
        conteúdo deste campo será ignorado caso o campo
        InscricaoMunicipalTomador esteja preenchido.
    :ivar razao_social_tomador: Informe o Nome/Razão Social do tomador.
        Este campo é obrigatório apenas para tomadores Pessoa Jurídica
        (CNPJ). Este campo será ignorado caso seja fornecido um CPF/CNPJ
        ou a Inscrição Municipal do tomador pertença ao município.
    :ivar doc_tomador_estrangeiro: Informe o Documento de Identificação
        do tomador. Este campo é obrigatório apenas para tomadores
        estrageiros, ou seja quando no CidadeTomador que indica o Codigo
        SIAFI da cidade do tomador for informado 0009999
    :ivar tipo_logradouro_tomador: Informe o Tipo do Logradouro do
        Endereço do Tomador.
    :ivar logradouro_tomador: Informe o Logradouro do Endereço do
        Tomador.
    :ivar numero_endereco_tomador: Informe o Número do Endereço do
        Tomador.
    :ivar complemento_endereco_tomador: Informe o Comlpemento do
        Endereço do Tomador.
    :ivar tipo_bairro_tomador: Informe o Tipo do Bairro do Endereço do
        Tomador.
    :ivar bairro_tomador: Informe o Bairro do Endereço do Tomador.
    :ivar cidade_tomador: Informe a Cidade do Tomador.
    :ivar cidade_tomador_descricao: Informe a Descricao da Cidade do
        Tomador.
    :ivar ceptomador: Informe o CEP do Tomador.
    :ivar email_tomador: Informe o e-mail do tomador.
    :ivar codigo_atividade: Informe o código da atividade do RPS. Este
        código deve pertencer à lista CNAE.
    :ivar aliquota_atividade: Informe o valor da alíquota.
    :ivar tipo_recolhimento: Informe a retenção.
    :ivar municipio_prestacao: Informe o Município da Prestação do
        Serviço.
    :ivar municipio_prestacao_descricao: Informe o Município da
        Prestação do Serviço.
    :ivar operacao: Informe a Operação da Prestação do Serviço.
    :ivar tributacao: Informe o tipo de tributação do RPS.
    :ivar valor_pis: Informe o valor da retenção do PIS.
    :ivar valor_cofins: Informe o valor da retenção do COFINS.
    :ivar valor_inss: Informe o valor da retenção do INSS.
    :ivar valor_ir: Informe o valor da retenção do IR.
    :ivar valor_csll: Informe o valor da retenção do CSLL.
    :ivar aliquota_pis: Informe a Alíquota da retenção do PIS.
    :ivar aliquota_cofins: Informe a Alíquota da retenção do COFINS.
    :ivar aliquota_inss: Informe a Alíquota da retenção do INSS.
    :ivar aliquota_ir: Informe a Alíquota da retenção do IR.
    :ivar aliquota_csll: Informe a Alíquota da retenção do CSLL.
    :ivar descricao_rps: Descrição da Nota.
    :ivar dddprestador: DDD do Prestador.
    :ivar telefone_prestador: Telefone do Prestador.
    :ivar dddtomador: DDD do Tomador.
    :ivar telefone_tomador: Telefone do Tomador.
    :ivar mot_cancelamento: Informe o Motivo do Cancelamento.
    :ivar cpfcnpjintermediario: Informe o CPF/CNPJ do intermediário do
        serviço. Campo não é obrigatório, deve ser informado quando
        houver um intermediário entre o tomador e o prestador.
    :ivar deducoes: Lista de Deduções.
    :ivar itens: Lista de Itens.
    :ivar id:
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
    inscricao_municipal_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    razao_social_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocialPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
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
    serie_rps: Optional[TpSerieRps] = field(
        default=None,
        metadata={
            "name": "SerieRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    numero_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_emissao_rps: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissaoRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    situacao_rps: Optional[TpSituacaoRps] = field(
        default=None,
        metadata={
            "name": "SituacaoRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    serie_rpssubstituido: Optional[TpSerieRpssubstituido] = field(
        default=None,
        metadata={
            "name": "SerieRPSSubstituido",
            "type": "Element",
            "namespace": "",
        }
    )
    numero_rpssubstituido: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroRPSSubstituido",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    numero_nfse_substituida: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroNFSeSubstituida",
            "type": "Element",
            "namespace": "",
            "min_inclusive": "0",
            "max_inclusive": "2147483647",
            "pattern": r"[0-9]{1,12}",
        }
    )
    data_emissao_nfse_substituida: Optional[Union[XmlDate, Nulo]] = field(
        default=None,
        metadata={
            "name": "DataEmissaoNFSeSubstituida",
            "type": "Element",
            "namespace": "",
            "white_space": "collapse",
        }
    )
    serie_prestacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeriePrestacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    inscricao_municipal_tomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipalTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{6,11}",
        }
    )
    cpfcnpjtomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPFCNPJTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{11}|[0-9]{14}",
        }
    )
    razao_social_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocialTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 120,
            "white_space": "preserve",
        }
    )
    doc_tomador_estrangeiro: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTomadorEstrangeiro",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 20,
            "white_space": "preserve",
        }
    )
    tipo_logradouro_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoLogradouroTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    logradouro_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogradouroTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )
    numero_endereco_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumeroEnderecoTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 9,
            "white_space": "preserve",
        }
    )
    complemento_endereco_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComplementoEnderecoTomador",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        }
    )
    tipo_bairro_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoBairroTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    bairro_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "BairroTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )
    cidade_tomador: Optional[int] = field(
        default=None,
        metadata={
            "name": "CidadeTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
        }
    )
    cidade_tomador_descricao: Optional[str] = field(
        default=None,
        metadata={
            "name": "CidadeTomadorDescricao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 50,
            "white_space": "preserve",
        }
    )
    ceptomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEPTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{0,8}",
        }
    )
    email_tomador: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 60,
            "white_space": "preserve",
        }
    )
    codigo_atividade: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoAtividade",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{9}",
        }
    )
    aliquota_atividade: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaAtividade",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    tipo_recolhimento: Optional[TpTipoRecolhimento] = field(
        default=None,
        metadata={
            "name": "TipoRecolhimento",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    municipio_prestacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "MunicipioPrestacao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": 1,
        }
    )
    municipio_prestacao_descricao: Optional[str] = field(
        default=None,
        metadata={
            "name": "MunicipioPrestacaoDescricao",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 30,
            "white_space": "preserve",
        }
    )
    operacao: Optional[TpOperacao] = field(
        default=None,
        metadata={
            "name": "Operacao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tributacao: Optional[TpTributacao] = field(
        default=None,
        metadata={
            "name": "Tributacao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    valor_pis: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValorPIS",
            "type": "Element",
            "namespace": "",
            "required": True,
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
            "required": True,
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
            "required": True,
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
            "required": True,
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
            "required": True,
            "min_inclusive": "0",
            "total_digits": 15,
            "fraction_digits": 2,
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{0,2})?",
        }
    )
    aliquota_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaPIS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    aliquota_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaCOFINS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    aliquota_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaINSS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    aliquota_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaIR",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    aliquota_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AliquotaCSLL",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 6,
            "fraction_digits": 4,
        }
    )
    descricao_rps: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescricaoRPS",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 0,
            "max_length": 1500,
            "white_space": "preserve",
        }
    )
    dddprestador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "DDDPrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{0,3}",
        }
    )
    telefone_prestador: Optional[Union[int, Nulo]] = field(
        default=None,
        metadata={
            "name": "TelefonePrestador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": 99999999,
        }
    )
    dddtomador: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "DDDTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]{0,3}",
        }
    )
    telefone_tomador: Optional[Union[int, Nulo]] = field(
        default=None,
        metadata={
            "name": "TelefoneTomador",
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": 99999999,
        }
    )
    mot_cancelamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "MotCancelamento",
            "type": "Element",
            "namespace": "",
            "min_length": 0,
            "max_length": 80,
            "white_space": "preserve",
        }
    )
    cpfcnpjintermediario: Optional[Union[str, Nulo]] = field(
        default=None,
        metadata={
            "name": "CPFCNPJIntermediario",
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{11}|[0-9]{14}",
        }
    )
    deducoes: Optional[TpListaDeducoes] = field(
        default=None,
        metadata={
            "name": "Deducoes",
            "type": "Element",
            "namespace": "",
        }
    )
    itens: Optional[TpListaItens] = field(
        default=None,
        metadata={
            "name": "Itens",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TpListaNfseConsultaNota:
    """
    Lista de NFSE consultada.
    """
    class Meta:
        name = "tpListaNFSeConsultaNota"

    nota: List[TpNfse] = field(
        default_factory=list,
        metadata={
            "name": "Nota",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TpLote:
    """
    Lote de RPS.
    """
    class Meta:
        name = "tpLote"

    rps: List[TpRps] = field(
        default_factory=list,
        metadata={
            "name": "RPS",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
