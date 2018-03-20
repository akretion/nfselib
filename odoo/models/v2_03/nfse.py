# -*- coding: utf-8 -*-

#
# Generated Tue Mar 20 04:15:47 2018 by generateDS.py(Akretion's branch).
# Python 3.5.2 (default, Sep 14 2017, 22:51:06)  [GCC 5.4.0 20160609]
#
from odoo import fields
from .. import spec_models

# u"Tipo Codigo da Lista de Servicos LC 116/2003"
tsItemListaServico = [
    ("01.01", u"01.01"),
    ("01.02", u"01.02"),
    ("01.03", u"01.03"),
    ("01.04", u"01.04"),
    ("01.05", u"01.05"),
    ("01.06", u"01.06"),
    ("01.07", u"01.07"),
    ("01.08", u"01.08"),
    ("02.01", u"02.01"),
    ("03.02", u"03.02"),
    ("03.03", u"03.03"),
    ("03.04", u"03.04"),
    ("03.05", u"03.05"),
    ("04.01", u"04.01"),
    ("04.02", u"04.02"),
    ("04.03", u"04.03"),
    ("04.04", u"04.04"),
    ("04.05", u"04.05"),
    ("04.06", u"04.06"),
    ("04.07", u"04.07"),
    ("04.08", u"04.08"),
    ("04.09", u"04.09"),
    ("04.10", u"04.10"),
    ("04.11", u"04.11"),
    ("04.12", u"04.12"),
    ("04.13", u"04.13"),
    ("04.14", u"04.14"),
    ("04.15", u"04.15"),
    ("04.16", u"04.16"),
    ("04.17", u"04.17"),
    ("04.18", u"04.18"),
    ("04.19", u"04.19"),
    ("04.20", u"04.20"),
    ("04.21", u"04.21"),
    ("04.22", u"04.22"),
    ("04.23", u"04.23"),
    ("05.01", u"05.01"),
    ("05.02", u"05.02"),
    ("05.03", u"05.03"),
    ("05.04", u"05.04"),
    ("05.05", u"05.05"),
    ("05.06", u"05.06"),
    ("05.07", u"05.07"),
    ("05.08", u"05.08"),
    ("05.09", u"05.09"),
    ("06.01", u"06.01"),
    ("06.02", u"06.02"),
    ("06.03", u"06.03"),
    ("06.04", u"06.04"),
    ("06.05", u"06.05"),
    ("07.01", u"07.01"),
    ("07.02", u"07.02"),
    ("07.03", u"07.03"),
    ("07.04", u"07.04"),
    ("07.05", u"07.05"),
    ("07.06", u"07.06"),
    ("07.07", u"07.07"),
    ("07.08", u"07.08"),
    ("07.09", u"07.09"),
    ("07.10", u"07.10"),
    ("07.11", u"07.11"),
    ("07.12", u"07.12"),
    ("07.13", u"07.13"),
    ("07.16", u"07.16"),
    ("07.17", u"07.17"),
    ("07.18", u"07.18"),
    ("07.19", u"07.19"),
    ("07.20", u"07.20"),
    ("07.21", u"07.21"),
    ("07.22", u"07.22"),
    ("08.01", u"08.01"),
    ("08.02", u"08.02"),
    ("09.01", u"09.01"),
    ("09.02", u"09.02"),
    ("09.03", u"09.03"),
    ("10.01", u"10.01"),
    ("10.02", u"10.02"),
    ("10.03", u"10.03"),
    ("10.04", u"10.04"),
    ("10.05", u"10.05"),
    ("10.06", u"10.06"),
    ("10.07", u"10.07"),
    ("10.08", u"10.08"),
    ("10.09", u"10.09"),
    ("10.10", u"10.10"),
    ("11.01", u"11.01"),
    ("11.02", u"11.02"),
    ("11.03", u"11.03"),
    ("11.04", u"11.04"),
    ("12.01", u"12.01"),
    ("12.02", u"12.02"),
    ("12.03", u"12.03"),
    ("12.04", u"12.04"),
    ("12.05", u"12.05"),
    ("12.06", u"12.06"),
    ("12.07", u"12.07"),
    ("12.08", u"12.08"),
    ("12.09", u"12.09"),
    ("12.10", u"12.10"),
    ("12.11", u"12.11"),
    ("12.12", u"12.12"),
    ("12.13", u"12.13"),
    ("12.14", u"12.14"),
    ("12.15", u"12.15"),
    ("12.16", u"12.16"),
    ("12.17", u"12.17"),
    ("13.02", u"13.02"),
    ("13.03", u"13.03"),
    ("13.04", u"13.04"),
    ("13.05", u"13.05"),
    ("14.01", u"14.01"),
    ("14.02", u"14.02"),
    ("14.03", u"14.03"),
    ("14.04", u"14.04"),
    ("14.05", u"14.05"),
    ("14.06", u"14.06"),
    ("14.07", u"14.07"),
    ("14.08", u"14.08"),
    ("14.09", u"14.09"),
    ("14.10", u"14.10"),
    ("14.11", u"14.11"),
    ("14.12", u"14.12"),
    ("14.13", u"14.13"),
    ("15.01", u"15.01"),
    ("15.02", u"15.02"),
    ("15.03", u"15.03"),
    ("15.04", u"15.04"),
    ("15.05", u"15.05"),
    ("15.06", u"15.06"),
    ("15.07", u"15.07"),
    ("15.08", u"15.08"),
    ("15.09", u"15.09"),
    ("15.10", u"15.10"),
    ("15.11", u"15.11"),
    ("15.12", u"15.12"),
    ("15.13", u"15.13"),
    ("15.14", u"15.14"),
    ("15.15", u"15.15"),
    ("15.16", u"15.16"),
    ("15.17", u"15.17"),
    ("15.18", u"15.18"),
    ("16.01", u"16.01"),
    ("17.01", u"17.01"),
    ("17.02", u"17.02"),
    ("17.03", u"17.03"),
    ("17.04", u"17.04"),
    ("17.05", u"17.05"),
    ("17.06", u"17.06"),
    ("17.08", u"17.08"),
    ("17.09", u"17.09"),
    ("17.10", u"17.10"),
    ("17.11", u"17.11"),
    ("17.12", u"17.12"),
    ("17.13", u"17.13"),
    ("17.14", u"17.14"),
    ("17.15", u"17.15"),
    ("17.16", u"17.16"),
    ("17.17", u"17.17"),
    ("17.18", u"17.18"),
    ("17.19", u"17.19"),
    ("17.20", u"17.20"),
    ("17.21", u"17.21"),
    ("17.22", u"17.22"),
    ("17.23", u"17.23"),
    ("17.24", u"17.24"),
    ("18.01", u"18.01"),
    ("19.01", u"19.01"),
    ("20.01", u"20.01"),
    ("20.02", u"20.02"),
    ("20.03", u"20.03"),
    ("21.01", u"21.01"),
    ("22.01", u"22.01"),
    ("23.01", u"23.01"),
    ("24.01", u"24.01"),
    ("25.01", u"25.01"),
    ("25.02", u"25.02"),
    ("25.03", u"25.03"),
    ("25.04", u"25.04"),
    ("26.01", u"26.01"),
    ("27.01", u"27.01"),
    ("28.01", u"28.01"),
    ("29.01", u"29.01"),
    ("30.01", u"30.01"),
    ("31.01", u"31.01"),
    ("32.01", u"32.01"),
    ("33.01", u"33.01"),
    ("34.01", u"34.01"),
    ("35.01", u"35.01"),
    ("36.01", u"36.01"),
    ("37.01", u"37.01"),
    ("38.01", u"38.01"),
    ("39.01", u"39.01"),
    ("40.01", u"40.01"),
]

# u"UF ("
tsUf = [
    ("AC", u"AC - Acre"),
    ("AL", u"AL - Alagoas"),
    ("AM", u"AM - Amazonas"),
    ("AP", u"AP - Amapa"),
    ("BA", u"BA - Bahia"),
    ("CE", u"CE - Ceara"),
    ("DF", u"DF - Distrito Federal"),
    ("ES", u"ES - Espirito Santo"),
    ("GO", u"GO - Goias"),
    ("MA", u"MA - Maranhao"),
    ("MG", u"MG - Minas Gerais"),
    ("MS", u"MS - Mato Grosso do Sul"),
    ("MT", u"MT - Mato Grosso"),
    ("PA", u"PA - Para"),
    ("PB", u"PB - Paraiba"),
    ("PE", u"PE - Pernambuco"),
    ("PI", u"PI - Piaui"),
    ("PR", u"PR - Parana"),
    ("RJ", u"RJ - Rio de Janeiro"),
    ("RN", u"RN - Rio Grande do Norte"),
    ("RO", u"RO - Rondonia"),
    ("RR", u"RR - Roraima"),
    ("RS", u"RS - Rio Grande do Sul"),
    ("SC", u"SC - Santa Catarina"),
    ("SE", u"SE - Sergipe"),
    ("SP", u"SP - Sao Paulo"),
    ("TO", u"TO - Tocantins)"),
]


class CancelarNfseEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.cancelarnfseenvio'
    _generateds_type = 'CancelarNfseEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Pedido'

    nfe_Pedido = fields.Many2one(
        "nfe.v3_10.tcpedidocancelamento",
        string="Pedido", xsd_required=True)


class CancelarNfseResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.cancelarnfseresposta'
    _generateds_type = 'CancelarNfseResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_RetCancelamento'

    nfe_choice5 = fields.Selection([
        ('nfe_RetCancelamento', 'RetCancelamento'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno')],
        "RetCancelamento/ListaMensagemRetorno",
        default="nfe_RetCancelamento")
    nfe_RetCancelamento = fields.Many2one(
        "nfe.v3_10.tcretcancelamento",
        choice='5',
        string="RetCancelamento",
        xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='5',
        string="ListaMensagemRetorno",
        xsd_required=True)


class ConsultarLoteRpsEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarloterpsenvio'
    _generateds_type = 'ConsultarLoteRpsEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Prestador'

    nfe_Prestador = fields.Many2one(
        "nfe.v3_10.tcidentificacaoprestador",
        string="Prestador", xsd_required=True)
    nfe_Protocolo = fields.Char(
        string="Protocolo", xsd_required=True)


class ConsultarLoteRpsResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarloterpsresposta'
    _generateds_type = 'ConsultarLoteRpsResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Situacao'

    nfe_choice7 = fields.Selection([
        ('nfe_ListaNfse', 'ListaNfse'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno'),
        ('nfe_ListaMensagemRetornoLote', 'ListaMensagemRetornoLote')],
        "ListaNfse/ListaMensagemRetorno/ListaMensagemRetorn...",
        default="nfe_ListaNfse")
    nfe_ListaNfse = fields.Many2one(
        "nfe.v3_10.listanfse2",
        choice='7',
        string="ListaNfse", xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='7',
        string="ListaMensagemRetorno",
        xsd_required=True)
    nfe_ListaMensagemRetornoLote = fields.Many2one(
        "nfe.v3_10.listamensagemretornolote",
        choice='7',
        string="ListaMensagemRetornoLote",
        xsd_required=True)


class ConsultarNfseFaixaEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarnfsefaixaenvio'
    _generateds_type = 'ConsultarNfseFaixaEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Prestador'

    nfe_Prestador = fields.Many2one(
        "nfe.v3_10.tcidentificacaoprestador",
        string="Prestador", xsd_required=True)
    nfe_Faixa = fields.Many2one(
        "nfe.v3_10.faixa",
        string="Faixa", xsd_required=True)
    nfe_Pagina = fields.Integer(
        string="Pagina", xsd_required=True)


class ConsultarNfseFaixaResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarnfsefaixaresposta'
    _generateds_type = 'ConsultarNfseFaixaResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_ListaNfse'

    nfe_choice13 = fields.Selection([
        ('nfe_ListaNfse', 'ListaNfse'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno')],
        "ListaNfse/ListaMensagemRetorno",
        default="nfe_ListaNfse")
    nfe_ListaNfse = fields.Many2one(
        "nfe.v3_10.listanfse7",
        choice='13',
        string="ListaNfse", xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='13',
        string="ListaMensagemRetorno",
        xsd_required=True)


class ConsultarNfseRpsEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarnfserpsenvio'
    _generateds_type = 'ConsultarNfseRpsEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_IdentificacaoRps'

    nfe_IdentificacaoRps = fields.Many2one(
        "nfe.v3_10.tcidentificacaorps",
        string="IdentificacaoRps",
        xsd_required=True)
    nfe_Prestador = fields.Many2one(
        "nfe.v3_10.tcidentificacaoprestador",
        string="Prestador", xsd_required=True)


class ConsultarNfseRpsResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarnfserpsresposta'
    _generateds_type = 'ConsultarNfseRpsResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_choice8 = fields.Selection([
        ('nfe_CompNfse', 'CompNfse'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno')],
        "CompNfse/ListaMensagemRetorno",
        default="nfe_CompNfse")
    nfe_CompNfse = fields.Many2one(
        "nfe.v3_10.tccompnfse",
        choice='8',
        string="CompNfse", xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='8',
        string="ListaMensagemRetorno",
        xsd_required=True)


class ConsultarNfseServicoPrestadoEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarnfseservicoprestadoenvio'
    _generateds_type = 'ConsultarNfseServicoPrestadoEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Prestador'

    nfe_choice9 = fields.Selection([
        ('nfe_PeriodoEmissao', 'PeriodoEmissao'),
        ('nfe_PeriodoCompetencia', 'PeriodoCompetencia')],
        "PeriodoEmissao/PeriodoCompetencia",
        default="nfe_PeriodoEmissao")
    nfe_Prestador = fields.Many2one(
        "nfe.v3_10.tcidentificacaoprestador",
        string="Prestador", xsd_required=True)
    nfe_NumeroNfse = fields.Integer(
        string="NumeroNfse")
    nfe_PeriodoEmissao = fields.Many2one(
        "nfe.v3_10.periodoemissao",
        choice='9',
        string="PeriodoEmissao")
    nfe_PeriodoCompetencia = fields.Many2one(
        "nfe.v3_10.periodocompetencia",
        choice='9',
        string="PeriodoCompetencia")
    nfe_Tomador = fields.Many2one(
        "nfe.v3_10.tcidentificacaotomador",
        string="Tomador")
    nfe_Intermediario = fields.Many2one(
        "nfe.v3_10.tcidentificacaointermediario",
        string="Intermediario")
    nfe_Pagina = fields.Integer(
        string="Pagina", xsd_required=True)


class ConsultarNfseServicoPrestadoResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarnfseservicoprestadoresposta'
    _generateds_type = 'ConsultarNfseServicoPrestadoResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_ListaNfse'

    nfe_choice10 = fields.Selection([
        ('nfe_ListaNfse', 'ListaNfse'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno')],
        "ListaNfse/ListaMensagemRetorno",
        default="nfe_ListaNfse")
    nfe_ListaNfse = fields.Many2one(
        "nfe.v3_10.listanfse3",
        choice='10',
        string="ListaNfse", xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='10',
        string="ListaMensagemRetorno",
        xsd_required=True)


class ConsultarNfseServicoTomadoEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarnfseservicotomadoenvio'
    _generateds_type = 'ConsultarNfseServicoTomadoEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Consulente'

    nfe_choice11 = fields.Selection([
        ('nfe_PeriodoEmissao', 'PeriodoEmissao'),
        ('nfe_PeriodoCompetencia', 'PeriodoCompetencia')],
        "PeriodoEmissao/PeriodoCompetencia",
        default="nfe_PeriodoEmissao")
    nfe_Consulente = fields.Many2one(
        "nfe.v3_10.tcidentificacaoconsulente",
        string="Consulente", xsd_required=True)
    nfe_NumeroNfse = fields.Integer(
        string="NumeroNfse")
    nfe_PeriodoEmissao = fields.Many2one(
        "nfe.v3_10.periodoemissao4",
        choice='11',
        string="PeriodoEmissao")
    nfe_PeriodoCompetencia = fields.Many2one(
        "nfe.v3_10.periodocompetencia5",
        choice='11',
        string="PeriodoCompetencia")
    nfe_Prestador = fields.Many2one(
        "nfe.v3_10.tcidentificacaoprestador",
        string="Prestador")
    nfe_Tomador = fields.Many2one(
        "nfe.v3_10.tcidentificacaotomador",
        string="Tomador")
    nfe_Intermediario = fields.Many2one(
        "nfe.v3_10.tcidentificacaointermediario",
        string="Intermediario")
    nfe_Pagina = fields.Integer(
        string="Pagina", xsd_required=True)


class ConsultarNfseServicoTomadoResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.consultarnfseservicotomadoresposta'
    _generateds_type = 'ConsultarNfseServicoTomadoResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_ListaNfse'

    nfe_choice12 = fields.Selection([
        ('nfe_ListaNfse', 'ListaNfse'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno')],
        "ListaNfse/ListaMensagemRetorno",
        default="nfe_ListaNfse")
    nfe_ListaNfse = fields.Many2one(
        "nfe.v3_10.listanfse6",
        choice='12',
        string="ListaNfse", xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='12',
        string="ListaMensagemRetorno",
        xsd_required=True)


class EnviarLoteRpsEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.enviarloterpsenvio'
    _generateds_type = 'EnviarLoteRpsEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_LoteRps'

    nfe_LoteRps = fields.Many2one(
        "nfe.v3_10.tcloterps",
        string="LoteRps", xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class EnviarLoteRpsResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.enviarloterpsresposta'
    _generateds_type = 'EnviarLoteRpsResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_NumeroLote'

    nfe_choice2 = fields.Selection([
        ('nfe_NumeroLote', 'NumeroLote'),
        ('nfe_DataRecebimento', 'DataRecebimento'),
        ('nfe_Protocolo', 'Protocolo'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno')],
        "NumeroLote/DataRecebimento/Protocolo/ListaMensagem...",
        default="nfe_NumeroLote")
    nfe_NumeroLote = fields.Integer(
        choice='2',
        string="NumeroLote", xsd_required=True)
    nfe_DataRecebimento = fields.Datetime(
        choice='2',
        string="DataRecebimento",
        xsd_required=True)
    nfe_Protocolo = fields.Char(
        choice='2',
        string="Protocolo", xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='2',
        string="ListaMensagemRetorno",
        xsd_required=True)


class EnviarLoteRpsSincronoEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.enviarloterpssincronoenvio'
    _generateds_type = 'EnviarLoteRpsSincronoEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_LoteRps'

    nfe_LoteRps = fields.Many2one(
        "nfe.v3_10.tcloterps",
        string="LoteRps", xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class EnviarLoteRpsSincronoResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.enviarloterpssincronoresposta'
    _generateds_type = 'EnviarLoteRpsSincronoResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_NumeroLote'

    nfe_choice3 = fields.Selection([
        ('nfe_ListaNfse', 'ListaNfse'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno'),
        ('nfe_ListaMensagemRetornoLote', 'ListaMensagemRetornoLote')],
        "ListaNfse/ListaMensagemRetorno/ListaMensagemRetorn...",
        default="nfe_ListaNfse")
    nfe_NumeroLote = fields.Integer(
        string="NumeroLote")
    nfe_DataRecebimento = fields.Datetime(
        string="DataRecebimento")
    nfe_Protocolo = fields.Char(
        string="Protocolo")
    nfe_ListaNfse = fields.Many2one(
        "nfe.v3_10.listanfse",
        choice='3',
        string="ListaNfse", xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='3',
        string="ListaMensagemRetorno",
        xsd_required=True)
    nfe_ListaMensagemRetornoLote = fields.Many2one(
        "nfe.v3_10.listamensagemretornolote",
        choice='3',
        string="ListaMensagemRetornoLote",
        xsd_required=True)


class Faixa(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.faixa'
    _generateds_type = 'FaixaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_NumeroNfseInicial'

    nfe_NumeroNfseInicial = fields.Integer(
        string="NumeroNfseInicial",
        xsd_required=True)
    nfe_NumeroNfseFinal = fields.Integer(
        string="NumeroNfseFinal")


class GerarNfseEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.gerarnfseenvio'
    _generateds_type = 'GerarNfseEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Rps'

    nfe_Rps = fields.Many2one(
        "nfe.v3_10.tcdeclaracaoprestacaoservico",
        string="Rps", xsd_required=True)


class GerarNfseResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.gerarnfseresposta'
    _generateds_type = 'GerarNfseResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_ListaNfse'

    nfe_choice4 = fields.Selection([
        ('nfe_ListaNfse', 'ListaNfse'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno')],
        "ListaNfse/ListaMensagemRetorno",
        default="nfe_ListaNfse")
    nfe_ListaNfse = fields.Many2one(
        "nfe.v3_10.listanfse1",
        choice='4',
        string="ListaNfse", xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='4',
        string="ListaMensagemRetorno",
        xsd_required=True)


class ListaMensagemAlertaRetorno(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listamensagemalertaretorno'
    _generateds_type = 'ListaMensagemAlertaRetorno'
    _concrete_class = None
    _concrete_rec_name = 'nfe_MensagemRetorno'

    nfe_MensagemRetorno = fields.One2many(
        "nfe.v3_10.tcmensagemretorno",
        "nfe_MensagemRetorno_ListaMensagemAlertaRetorno_id",
        string="MensagemRetorno",
        xsd_required=True
    )


class ListaMensagemRetorno(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listamensagemretorno'
    _generateds_type = 'ListaMensagemRetorno'
    _concrete_class = None
    _concrete_rec_name = 'nfe_MensagemRetorno'

    nfe_MensagemRetorno = fields.One2many(
        "nfe.v3_10.tcmensagemretorno",
        "nfe_MensagemRetorno_ListaMensagemRetorno_id",
        string="MensagemRetorno",
        xsd_required=True
    )


class ListaMensagemRetornoLote(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listamensagemretornolote'
    _generateds_type = 'ListaMensagemRetornoLote'
    _concrete_class = None
    _concrete_rec_name = 'nfe_MensagemRetorno'

    nfe_MensagemRetorno = fields.One2many(
        "nfe.v3_10.tcmensagemretornolote",
        "nfe_MensagemRetorno_ListaMensagemRetornoLote_id",
        string="MensagemRetorno",
        xsd_required=True
    )


class ListaNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listanfse'
    _generateds_type = 'ListaNfseType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_CompNfse = fields.One2many(
        "nfe.v3_10.tccompnfse",
        "nfe_CompNfse_ListaNfse_id",
        string="CompNfse", xsd_required=True
    )
    nfe_ListaMensagemAlertaRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemalertaretorno",
        string="ListaMensagemAlertaRetorno")


class ListaNfse1(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listanfse1'
    _generateds_type = 'ListaNfseType1'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_CompNfse = fields.Many2one(
        "nfe.v3_10.tccompnfse",
        string="CompNfse", xsd_required=True)
    nfe_ListaMensagemAlertaRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemalertaretorno",
        string="ListaMensagemAlertaRetorno")


class ListaNfse2(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listanfse2'
    _generateds_type = 'ListaNfseType2'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_CompNfse = fields.One2many(
        "nfe.v3_10.tccompnfse",
        "nfe_CompNfse_ListaNfse2_id",
        string="CompNfse", xsd_required=True
    )
    nfe_ListaMensagemAlertaRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemalertaretorno",
        string="ListaMensagemAlertaRetorno")


class ListaNfse3(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listanfse3'
    _generateds_type = 'ListaNfseType3'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_CompNfse = fields.One2many(
        "nfe.v3_10.tccompnfse",
        "nfe_CompNfse_ListaNfse3_id",
        string="CompNfse", xsd_required=True
    )
    nfe_ProximaPagina = fields.Integer(
        string="ProximaPagina")


class ListaNfse6(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listanfse6'
    _generateds_type = 'ListaNfseType6'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_CompNfse = fields.One2many(
        "nfe.v3_10.tccompnfse",
        "nfe_CompNfse_ListaNfse6_id",
        string="CompNfse", xsd_required=True
    )
    nfe_ProximaPagina = fields.Integer(
        string="ProximaPagina")


class ListaNfse7(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listanfse7'
    _generateds_type = 'ListaNfseType7'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_CompNfse = fields.One2many(
        "nfe.v3_10.tccompnfse",
        "nfe_CompNfse_ListaNfse7_id",
        string="CompNfse", xsd_required=True
    )
    nfe_ProximaPagina = fields.Integer(
        string="ProximaPagina")


class ListaRps(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.listarps'
    _generateds_type = 'ListaRpsType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Rps'

    nfe_Rps = fields.One2many(
        "nfe.v3_10.tcdeclaracaoprestacaoservico",
        "nfe_Rps_ListaRps_id",
        string="Rps", xsd_required=True
    )


class NfseSubstituida(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.nfsesubstituida'
    _generateds_type = 'NfseSubstituidaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_CompNfse = fields.Many2one(
        "nfe.v3_10.tccompnfse",
        string="CompNfse", xsd_required=True)
    nfe_ListaMensagemAlertaRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemalertaretorno",
        string="ListaMensagemAlertaRetorno")


class NfseSubstituidora(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.nfsesubstituidora'
    _generateds_type = 'NfseSubstituidoraType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CompNfse'

    nfe_CompNfse = fields.Many2one(
        "nfe.v3_10.tccompnfse",
        string="CompNfse", xsd_required=True)


class PeriodoCompetencia(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.periodocompetencia'
    _generateds_type = 'PeriodoCompetenciaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_DataInicial'

    nfe_DataInicial = fields.Date(
        string="DataInicial", xsd_required=True)
    nfe_DataFinal = fields.Date(
        string="DataFinal", xsd_required=True)


class PeriodoCompetencia5(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.periodocompetencia5'
    _generateds_type = 'PeriodoCompetenciaType5'
    _concrete_class = None
    _concrete_rec_name = 'nfe_DataInicial'

    nfe_DataInicial = fields.Date(
        string="DataInicial", xsd_required=True)
    nfe_DataFinal = fields.Date(
        string="DataFinal", xsd_required=True)


class PeriodoEmissao(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.periodoemissao'
    _generateds_type = 'PeriodoEmissaoType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_DataInicial'

    nfe_DataInicial = fields.Date(
        string="DataInicial", xsd_required=True)
    nfe_DataFinal = fields.Date(
        string="DataFinal", xsd_required=True)


class PeriodoEmissao4(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.periodoemissao4'
    _generateds_type = 'PeriodoEmissaoType4'
    _concrete_class = None
    _concrete_rec_name = 'nfe_DataInicial'

    nfe_DataInicial = fields.Date(
        string="DataInicial", xsd_required=True)
    nfe_DataFinal = fields.Date(
        string="DataFinal", xsd_required=True)


class RetSubstituicao(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.retsubstituicao'
    _generateds_type = 'RetSubstituicaoType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_NfseSubstituida'

    nfe_NfseSubstituida = fields.Many2one(
        "nfe.v3_10.nfsesubstituida",
        string="NfseSubstituida",
        xsd_required=True)
    nfe_NfseSubstituidora = fields.Many2one(
        "nfe.v3_10.nfsesubstituidora",
        string="NfseSubstituidora",
        xsd_required=True)


class SubstituicaoNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.substituicaonfse'
    _generateds_type = 'SubstituicaoNfseType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_Pedido = fields.Many2one(
        "nfe.v3_10.tcpedidocancelamento",
        string="Pedido", xsd_required=True)
    nfe_Rps = fields.Many2one(
        "nfe.v3_10.tcdeclaracaoprestacaoservico",
        string="Rps", xsd_required=True)


class SubstituirNfseEnvio(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.substituirnfseenvio'
    _generateds_type = 'SubstituirNfseEnvio'
    _concrete_class = None
    _concrete_rec_name = 'nfe_SubstituicaoNfse'

    nfe_SubstituicaoNfse = fields.Many2one(
        "nfe.v3_10.substituicaonfse",
        string="SubstituicaoNfse",
        xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class SubstituirNfseResposta(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.substituirnfseresposta'
    _generateds_type = 'SubstituirNfseResposta'
    _concrete_class = None
    _concrete_rec_name = 'nfe_RetSubstituicao'

    nfe_choice6 = fields.Selection([
        ('nfe_RetSubstituicao', 'RetSubstituicao'),
        ('nfe_ListaMensagemRetorno', 'ListaMensagemRetorno')],
        "RetSubstituicao/ListaMensagemRetorno",
        default="nfe_RetSubstituicao")
    nfe_RetSubstituicao = fields.Many2one(
        "nfe.v3_10.retsubstituicao",
        choice='6',
        string="RetSubstituicao",
        xsd_required=True)
    nfe_ListaMensagemRetorno = fields.Many2one(
        "nfe.v3_10.listamensagemretorno",
        choice='6',
        string="ListaMensagemRetorno",
        xsd_required=True)


class cabecalho(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.cabecalho'
    _generateds_type = 'cabecalho'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_versaoDados = fields.Char(
        string="versaoDados", xsd_required=True)


class tcCancelamentoNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tccancelamentonfse'
    _generateds_type = 'tcCancelamentoNfse'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_Confirmacao = fields.Many2one(
        "nfe.v3_10.tcconfirmacaocancelamento",
        string="Confirmacao", xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class tcCompNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tccompnfse'
    _generateds_type = 'tcCompNfse'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Nfse'

    nfe_CompNfse_ListaNfse_id = fields.Many2one(
        "nfe.v3_10.listanfse")
    nfe_Nfse = fields.Many2one(
        "nfe.v3_10.tcnfse",
        string="Nfse", xsd_required=True)
    nfe_NfseCancelamento = fields.Many2one(
        "nfe.v3_10.tccancelamentonfse",
        string="NfseCancelamento")
    nfe_NfseSubstituicao = fields.Many2one(
        "nfe.v3_10.tcsubstituicaonfse",
        string="NfseSubstituicao")


class tcConfirmacaoCancelamento(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcconfirmacaocancelamento'
    _generateds_type = 'tcConfirmacaoCancelamento'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_Pedido = fields.Many2one(
        "nfe.v3_10.tcpedidocancelamento",
        string="Pedido", xsd_required=True)
    nfe_DataHora = fields.Datetime(
        string="DataHora", xsd_required=True)


class tcContato(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tccontato'
    _generateds_type = 'tcContato'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Telefone'

    nfe_Telefone = fields.Char(
        string="Telefone")
    nfe_Email = fields.Char(
        string="Email")


class tcCpfCnpj(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tccpfcnpj'
    _generateds_type = 'tcCpfCnpj'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Cpf'

    nfe_choice1 = fields.Selection([
        ('nfe_Cpf', 'Cpf'),
        ('nfe_Cnpj', 'Cnpj')],
        "Cpf/Cnpj",
        default="nfe_Cpf")
    nfe_Cpf = fields.Char(
        choice='1',
        string="Cpf", xsd_required=True)
    nfe_Cnpj = fields.Char(
        choice='1',
        string="Cnpj", xsd_required=True)


class tcDadosConstrucaoCivil(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcdadosconstrucaocivil'
    _generateds_type = 'tcDadosConstrucaoCivil'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CodigoObra'

    nfe_CodigoObra = fields.Char(
        string="CodigoObra")
    nfe_Art = fields.Char(
        string="Art", xsd_required=True)


class tcDadosIntermediario(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcdadosintermediario'
    _generateds_type = 'tcDadosIntermediario'
    _concrete_class = None
    _concrete_rec_name = 'nfe_IdentificacaoIntermediario'

    nfe_IdentificacaoIntermediario = fields.Many2one(
        "nfe.v3_10.tcidentificacaointermediario",
        string="IdentificacaoIntermediario",
        xsd_required=True)
    nfe_RazaoSocial = fields.Char(
        string="RazaoSocial", xsd_required=True)
    nfe_CodigoMunicipio = fields.Integer(
        string="CodigoMunicipio",
        xsd_required=True)


class tcDadosPrestador(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcdadosprestador'
    _generateds_type = 'tcDadosPrestador'
    _concrete_class = None
    _concrete_rec_name = 'nfe_IdentificacaoPrestador'

    nfe_IdentificacaoPrestador = fields.Many2one(
        "nfe.v3_10.tcidentificacaoprestador",
        string="IdentificacaoPrestador",
        xsd_required=True)
    nfe_RazaoSocial = fields.Char(
        string="RazaoSocial", xsd_required=True)
    nfe_NomeFantasia = fields.Char(
        string="NomeFantasia")
    nfe_Endereco = fields.Many2one(
        "nfe.v3_10.tcendereco",
        string="Endereco", xsd_required=True)
    nfe_Contato = fields.Many2one(
        "nfe.v3_10.tccontato",
        string="Contato")


class tcDadosServico(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcdadosservico'
    _generateds_type = 'tcDadosServico'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Valores'

    nfe_Valores = fields.Many2one(
        "nfe.v3_10.tcvaloresdeclaracaoservico",
        string="Valores", xsd_required=True)
    nfe_ItemListaServico = fields.Selection(
        tsItemListaServico,
        string="ItemListaServico",
        xsd_required=True,
        help=u"Tipo Codigo da Lista de Servicos LC 116/2003")
    nfe_CodigoCnae = fields.Integer(
        string="CodigoCnae")
    nfe_CodigoTributacaoMunicipio = fields.Char(
        string="CodigoTributacaoMunicipio")
    nfe_CodigoNbs = fields.Char(
        string="CodigoNbs")
    nfe_Discriminacao = fields.Char(
        string="Discriminacao", xsd_required=True)
    nfe_CodigoMunicipio = fields.Integer(
        string="CodigoMunicipio",
        xsd_required=True)
    nfe_CodigoPais = fields.Char(
        string="CodigoPais")
    nfe_MunicipioIncidencia = fields.Integer(
        string="MunicipioIncidencia")
    nfe_NumeroProcesso = fields.Char(
        string="NumeroProcesso")


class tcDadosTomador(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcdadostomador'
    _generateds_type = 'tcDadosTomador'
    _concrete_class = None
    _concrete_rec_name = 'nfe_IdentificacaoTomador'

    nfe_IdentificacaoTomador = fields.Many2one(
        "nfe.v3_10.tcidentificacaotomador",
        string="IdentificacaoTomador")
    nfe_NifTomador = fields.Char(
        string="NifTomador")
    nfe_RazaoSocial = fields.Char(
        string="RazaoSocial")
    nfe_Endereco = fields.Many2one(
        "nfe.v3_10.tcendereco",
        string="Endereco")
    nfe_Contato = fields.Many2one(
        "nfe.v3_10.tccontato",
        string="Contato")


class tcDeclaracaoPrestacaoServico(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcdeclaracaoprestacaoservico'
    _generateds_type = 'tcDeclaracaoPrestacaoServico'
    _concrete_class = None
    _concrete_rec_name = 'nfe_InfDeclaracaoPrestacaoServico'

    nfe_Rps_ListaRps_id = fields.Many2one(
        "nfe.v3_10.listarps")
    nfe_InfDeclaracaoPrestacaoServico = fields.Many2one(
        "nfe.v3_10.tcinfdeclaracaoprestacaoservico",
        string="InfDeclaracaoPrestacaoServico",
        xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class tcEndereco(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcendereco'
    _generateds_type = 'tcEndereco'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Endereco'

    nfe_Endereco = fields.Char(
        string="Endereco")
    nfe_Numero = fields.Char(
        string="Numero")
    nfe_Complemento = fields.Char(
        string="Complemento")
    nfe_Bairro = fields.Char(
        string="Bairro")
    nfe_CodigoMunicipio = fields.Integer(
        string="CodigoMunicipio")
    nfe_Uf = fields.Selection(
        tsUf,
        string="Uf",
        help=u"UF (")
    nfe_CodigoPais = fields.Char(
        string="CodigoPais")
    nfe_Cep = fields.Char(
        string="Cep")


class tcIdentificacaoConsulente(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcidentificacaoconsulente'
    _generateds_type = 'tcIdentificacaoConsulente'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CpfCnpj'

    nfe_CpfCnpj = fields.Many2one(
        "nfe.v3_10.tccpfcnpj",
        string="CpfCnpj", xsd_required=True)
    nfe_InscricaoMunicipal = fields.Char(
        string="InscricaoMunicipal")


class tcIdentificacaoIntermediario(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcidentificacaointermediario'
    _generateds_type = 'tcIdentificacaoIntermediario'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CpfCnpj'

    nfe_CpfCnpj = fields.Many2one(
        "nfe.v3_10.tccpfcnpj",
        string="CpfCnpj")
    nfe_InscricaoMunicipal = fields.Char(
        string="InscricaoMunicipal")


class tcIdentificacaoNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcidentificacaonfse'
    _generateds_type = 'tcIdentificacaoNfse'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Numero'

    nfe_Numero = fields.Integer(
        string="Numero", xsd_required=True)
    nfe_CpfCnpj = fields.Many2one(
        "nfe.v3_10.tccpfcnpj",
        string="CpfCnpj", xsd_required=True)
    nfe_InscricaoMunicipal = fields.Char(
        string="InscricaoMunicipal")
    nfe_CodigoMunicipio = fields.Integer(
        string="CodigoMunicipio",
        xsd_required=True)


class tcIdentificacaoOrgaoGerador(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcidentificacaoorgaogerador'
    _generateds_type = 'tcIdentificacaoOrgaoGerador'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CodigoMunicipio'

    nfe_CodigoMunicipio = fields.Integer(
        string="CodigoMunicipio",
        xsd_required=True)
    nfe_Uf = fields.Selection(
        tsUf,
        string="Uf", xsd_required=True,
        help=u"UF (")


class tcIdentificacaoPrestador(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcidentificacaoprestador'
    _generateds_type = 'tcIdentificacaoPrestador'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CpfCnpj'

    nfe_CpfCnpj = fields.Many2one(
        "nfe.v3_10.tccpfcnpj",
        string="CpfCnpj")
    nfe_InscricaoMunicipal = fields.Char(
        string="InscricaoMunicipal")


class tcIdentificacaoRps(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcidentificacaorps'
    _generateds_type = 'tcIdentificacaoRps'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Numero'

    nfe_Numero = fields.Integer(
        string="Numero", xsd_required=True)
    nfe_Serie = fields.Char(
        string="Serie", xsd_required=True)


class tcIdentificacaoTomador(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcidentificacaotomador'
    _generateds_type = 'tcIdentificacaoTomador'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CpfCnpj'

    nfe_CpfCnpj = fields.Many2one(
        "nfe.v3_10.tccpfcnpj",
        string="CpfCnpj")
    nfe_InscricaoMunicipal = fields.Char(
        string="InscricaoMunicipal")


class tcInfDeclaracaoPrestacaoServico(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcinfdeclaracaoprestacaoservico'
    _generateds_type = 'tcInfDeclaracaoPrestacaoServico'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_Rps = fields.Many2one(
        "nfe.v3_10.tcinfrps",
        string="Rps")
    nfe_Competencia = fields.Date(
        string="Competencia", xsd_required=True)
    nfe_Servico = fields.Many2one(
        "nfe.v3_10.tcdadosservico",
        string="Servico", xsd_required=True)
    nfe_Prestador = fields.Many2one(
        "nfe.v3_10.tcidentificacaoprestador",
        string="Prestador", xsd_required=True)
    nfe_Tomador = fields.Many2one(
        "nfe.v3_10.tcdadostomador",
        string="Tomador")
    nfe_Intermediario = fields.Many2one(
        "nfe.v3_10.tcdadosintermediario",
        string="Intermediario")
    nfe_ConstrucaoCivil = fields.Many2one(
        "nfe.v3_10.tcdadosconstrucaocivil",
        string="ConstrucaoCivil")


class tcInfNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcinfnfse'
    _generateds_type = 'tcInfNfse'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_Numero = fields.Integer(
        string="Numero", xsd_required=True)
    nfe_CodigoVerificacao = fields.Char(
        string="CodigoVerificacao",
        xsd_required=True)
    nfe_DataEmissao = fields.Datetime(
        string="DataEmissao", xsd_required=True)
    nfe_NfseSubstituida = fields.Integer(
        string="NfseSubstituida")
    nfe_OutrasInformacoes = fields.Char(
        string="OutrasInformacoes")
    nfe_ValoresNfse = fields.Many2one(
        "nfe.v3_10.tcvaloresnfse",
        string="ValoresNfse", xsd_required=True)
    nfe_ValorCredito = fields.Monetary(
        string="ValorCredito")
    nfe_PrestadorServico = fields.Many2one(
        "nfe.v3_10.tcdadosprestador",
        string="PrestadorServico",
        xsd_required=True)
    nfe_OrgaoGerador = fields.Many2one(
        "nfe.v3_10.tcidentificacaoorgaogerador",
        string="OrgaoGerador", xsd_required=True)
    nfe_DeclaracaoPrestacaoServico = fields.Many2one(
        "nfe.v3_10.tcdeclaracaoprestacaoservico",
        string="DeclaracaoPrestacaoServico",
        xsd_required=True)


class tcInfPedidoCancelamento(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcinfpedidocancelamento'
    _generateds_type = 'tcInfPedidoCancelamento'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_IdentificacaoNfse = fields.Many2one(
        "nfe.v3_10.tcidentificacaonfse",
        string="IdentificacaoNfse",
        xsd_required=True)


class tcInfRps(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcinfrps'
    _generateds_type = 'tcInfRps'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_IdentificacaoRps = fields.Many2one(
        "nfe.v3_10.tcidentificacaorps",
        string="IdentificacaoRps",
        xsd_required=True)
    nfe_DataEmissao = fields.Date(
        string="DataEmissao", xsd_required=True)
    nfe_RpsSubstituido = fields.Many2one(
        "nfe.v3_10.tcidentificacaorps",
        string="RpsSubstituido")


class tcInfSubstituicaoNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcinfsubstituicaonfse'
    _generateds_type = 'tcInfSubstituicaoNfse'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_NfseSubstituidora = fields.Integer(
        string="NfseSubstituidora",
        xsd_required=True)


class tcLoteRps(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcloterps'
    _generateds_type = 'tcLoteRps'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_NumeroLote = fields.Integer(
        string="NumeroLote", xsd_required=True)
    nfe_CpfCnpj = fields.Many2one(
        "nfe.v3_10.tccpfcnpj",
        string="CpfCnpj", xsd_required=True)
    nfe_InscricaoMunicipal = fields.Char(
        string="InscricaoMunicipal")
    nfe_QuantidadeRps = fields.Integer(
        string="QuantidadeRps", xsd_required=True)
    nfe_ListaRps = fields.Many2one(
        "nfe.v3_10.listarps",
        string="ListaRps", xsd_required=True)


class tcMensagemRetorno(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcmensagemretorno'
    _generateds_type = 'tcMensagemRetorno'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Codigo'

    nfe_MensagemRetorno_ListaMensagemAlertaRetorno_id = fields.Many2one(
        "nfe.v3_10.listamensagemalertaretorno")
    nfe_Codigo = fields.Char(
        string="Codigo", xsd_required=True)
    nfe_Mensagem = fields.Char(
        string="Mensagem", xsd_required=True)
    nfe_Correcao = fields.Char(
        string="Correcao")


class tcMensagemRetornoLote(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcmensagemretornolote'
    _generateds_type = 'tcMensagemRetornoLote'
    _concrete_class = None
    _concrete_rec_name = 'nfe_IdentificacaoRps'

    nfe_MensagemRetorno_ListaMensagemRetornoLote_id = fields.Many2one(
        "nfe.v3_10.listamensagemretornolote")
    nfe_IdentificacaoRps = fields.Many2one(
        "nfe.v3_10.tcidentificacaorps",
        string="IdentificacaoRps",
        xsd_required=True)
    nfe_Codigo = fields.Char(
        string="Codigo", xsd_required=True)
    nfe_Mensagem = fields.Char(
        string="Mensagem", xsd_required=True)


class tcNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcnfse'
    _generateds_type = 'tcNfse'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_InfNfse = fields.Many2one(
        "nfe.v3_10.tcinfnfse",
        string="InfNfse", xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class tcPedidoCancelamento(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcpedidocancelamento'
    _generateds_type = 'tcPedidoCancelamento'
    _concrete_class = None
    _concrete_rec_name = 'nfe_InfPedidoCancelamento'

    nfe_InfPedidoCancelamento = fields.Many2one(
        "nfe.v3_10.tcinfpedidocancelamento",
        string="InfPedidoCancelamento",
        xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class tcRetCancelamento(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcretcancelamento'
    _generateds_type = 'tcRetCancelamento'
    _concrete_class = None
    _concrete_rec_name = 'nfe_NfseCancelamento'

    nfe_NfseCancelamento = fields.Many2one(
        "nfe.v3_10.tccancelamentonfse",
        string="NfseCancelamento",
        xsd_required=True)


class tcSubstituicaoNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcsubstituicaonfse'
    _generateds_type = 'tcSubstituicaoNfse'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_SubstituicaoNfse = fields.Many2one(
        "nfe.v3_10.tcinfsubstituicaonfse",
        string="SubstituicaoNfse",
        xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class tcValoresDeclaracaoServico(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcvaloresdeclaracaoservico'
    _generateds_type = 'tcValoresDeclaracaoServico'
    _concrete_class = None
    _concrete_rec_name = 'nfe_ValorServicos'

    nfe_ValorServicos = fields.Monetary(
        string="ValorServicos", xsd_required=True)
    nfe_ValorDeducoes = fields.Monetary(
        string="ValorDeducoes")
    nfe_ValorPis = fields.Monetary(
        string="ValorPis")
    nfe_ValorCofins = fields.Monetary(
        string="ValorCofins")
    nfe_ValorInss = fields.Monetary(
        string="ValorInss")
    nfe_ValorIr = fields.Monetary(
        string="ValorIr")
    nfe_ValorCsll = fields.Monetary(
        string="ValorCsll")
    nfe_OutrasRetencoes = fields.Monetary(
        string="OutrasRetencoes")
    nfe_ValTotTributos = fields.Monetary(
        string="ValTotTributos")
    nfe_ValorIss = fields.Monetary(
        string="ValorIss")
    nfe_Aliquota = fields.Monetary(
        string="Aliquota")
    nfe_DescontoIncondicionado = fields.Monetary(
        string="DescontoIncondicionado")
    nfe_DescontoCondicionado = fields.Monetary(
        string="DescontoCondicionado")


class tcValoresNfse(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.tcvaloresnfse'
    _generateds_type = 'tcValoresNfse'
    _concrete_class = None
    _concrete_rec_name = 'nfe_BaseCalculo'

    nfe_BaseCalculo = fields.Monetary(
        string="BaseCalculo")
    nfe_Aliquota = fields.Monetary(
        string="Aliquota")
    nfe_ValorIss = fields.Monetary(
        string="ValorIss")
    nfe_ValorLiquidoNfse = fields.Monetary(
        string="ValorLiquidoNfse",
        xsd_required=True)
