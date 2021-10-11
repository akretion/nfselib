from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
class TcContato:
    class Meta:
        name = "tcContato"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    telefone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    codigo_obra: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoObra",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    art: Optional[str] = field(
        default=None,
        metadata={
            "name": "Art",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcEndereco:
    class Meta:
        name = "tcEndereco"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    endereco: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "",
        }
    )
    numero: Optional[str] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "",
        }
    )
    complemento: Optional[str] = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "",
        }
    )
    bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "",
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "",
        }
    )
    uf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "",
        }
    )
    cep: Optional[int] = field(
        default=None,
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcIdentificacaoPrestador:
    class Meta:
        name = "tcIdentificacaoPrestador"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    numero: Optional[int] = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    serie: Optional[str] = field(
        default=None,
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tipo: Optional[int] = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    codigo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    mensagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcTransform:
    class Meta:
        name = "tcTransform"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TcValores:
    class Meta:
        name = "tcValores"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    valor_servicos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    valor_deducoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_pis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_cofins: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_inss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_ir: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_csll: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "",
        }
    )
    iss_retido: Optional[int] = field(
        default=None,
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_iss: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "",
        }
    )
    outras_retencoes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "",
        }
    )
    base_calculo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    aliquota: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_liquido_nfse: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "",
        }
    )
    valor_iss_retido: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValorIssRetido",
            "type": "Element",
            "namespace": "",
        }
    )
    desconto_condicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "",
        }
    )
    desconto_incondicionado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DigestValue:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class TcCanonicalizationMethod:
    class Meta:
        name = "tcCanonicalizationMethod"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcDigestMethod:
    class Meta:
        name = "tcDigestMethod"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcSignatureMethod:
    class Meta:
        name = "tcSignatureMethod"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcX509Data:
    class Meta:
        name = "tcX509Data"
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    x509_certificate: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TcDadosServico:
    class Meta:
        name = "tcDadosServico"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    valores: Optional[TcValores] = field(
        default=None,
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    item_lista_servico: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    codigo_cnae: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "",
        }
    )
    codigo_tributacao_municipio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "",
        }
    )
    discriminacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    codigo_municipio: Optional[int] = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TcIdentificacaoIntermediarioServico:
    class Meta:
        name = "tcIdentificacaoIntermediarioServico"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcIdentificacaoTomador:
    class Meta:
        name = "tcIdentificacaoTomador"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    cpf_cnpj: Optional[TcCpfCnpj] = field(
        default=None,
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "",
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcListaMensagemRetorno:
    class Meta:
        name = "tcListaMensagemRetorno"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    mensagem_retorno: List[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class CanonicalizationMethod(TcCanonicalizationMethod):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DigestMethod(TcDigestMethod):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureMethod(TcSignatureMethod):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Transform(TcTransform):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class X509Data(TcX509Data):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class EnviarLoteRpsResposta1:
    class Meta:
        name = "enviarLoteRpsResposta"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "",
        }
    )
    data_recebimento: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
            "namespace": "",
        }
    )
    protocolo: Optional[int] = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "namespace": "",
        }
    )
    lista_mensagem_retorno: Optional[TcListaMensagemRetorno] = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    identificacao_tomador: Optional[TcIdentificacaoTomador] = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "",
        }
    )
    razao_social: Optional[str] = field(
        default=None,
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "",
        }
    )
    endereco: Optional[TcEndereco] = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "",
        }
    )
    contato: Optional[TcContato] = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TcKeyInfo:
    class Meta:
        name = "tcKeyInfo"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    x509_data: Optional[X509Data] = field(
        default=None,
        metadata={
            "name": "X509Data",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcTransforms:
    class Meta:
        name = "tcTransforms"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )


@dataclass
class EnviarLoteRpsEnvioResponse:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    enviar_lote_rps_resposta: Optional[EnviarLoteRpsResposta1] = field(
        default=None,
        metadata={
            "name": "EnviarLoteRpsResposta",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class EnviarLoteRpsResposta(EnviarLoteRpsResposta1):
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"


@dataclass
class TcInfRps:
    class Meta:
        name = "tcInfRps"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    identificacao_rps: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    data_emissao: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    natureza_operacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "NaturezaOperacao",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    regime_especial_tributacao: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "",
        }
    )
    optante_simples_nacional: Optional[int] = field(
        default=None,
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    incentivador_cultural: Optional[int] = field(
        default=None,
        metadata={
            "name": "IncentivadorCultural",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    rps_substituido: Optional[TcIdentificacaoRps] = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "",
        }
    )
    servico: Optional[TcDadosServico] = field(
        default=None,
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    prestador: Optional[TcIdentificacaoPrestador] = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tomador: Optional[TcDadosTomador] = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    intermediario_servico: Optional[TcIdentificacaoIntermediarioServico] = field(
        default=None,
        metadata={
            "name": "IntermediarioServico",
            "type": "Element",
            "namespace": "",
        }
    )
    construcao_civil: Optional[TcDadosConstrucaoCivil] = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
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
class Transforms(TcTransforms):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class RecepcionarLoteRpsEnviarLoteRpsEnvioOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    body: Optional["RecepcionarLoteRpsEnviarLoteRpsEnvioOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        enviar_lote_rps_envio_response: Optional[EnviarLoteRpsEnvioResponse] = field(
            default=None,
            metadata={
                "name": "EnviarLoteRpsEnvioResponse",
                "type": "Element",
                "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            }
        )
        fault: Optional["RecepcionarLoteRpsEnviarLoteRpsEnvioOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class TcReference:
    class Meta:
        name = "tcReference"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Reference(TcReference):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class TcSigInfo:
    class Meta:
        name = "tcSigInfo"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_method: Optional[SignatureMethod] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class Signature:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    signed_info: Optional[TcSigInfo] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "required": True,
        }
    )
    signature_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "required": True,
        }
    )
    key_info: Optional[TcKeyInfo] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TcRps:
    class Meta:
        name = "tcRps"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    inf_rps: Optional[TcInfRps] = field(
        default=None,
        metadata={
            "name": "InfRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class TcListaRps:
    class Meta:
        name = "tcListaRps"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    rps: List[TcRps] = field(
        default_factory=list,
        metadata={
            "name": "Rps",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    inscricao_municipal: Optional[str] = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "",
        }
    )
    quantidade_rps: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    lista_rps: Optional[TcListaRps] = field(
        default=None,
        metadata={
            "name": "ListaRps",
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
            "required": True,
        }
    )


@dataclass
class EnviarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    lote_rps: Optional[TcLoteRps] = field(
        default=None,
        metadata={
            "name": "LoteRps",
            "type": "Element",
            "namespace": "",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass
class RecepcionarLoteRpsEnviarLoteRpsEnvioInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        target_namespace = "http://www.betha.com.br/e-nota-contribuinte-ws"

    body: Optional["RecepcionarLoteRpsEnviarLoteRpsEnvioInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        enviar_lote_rps_envio: Optional[EnviarLoteRpsEnvio] = field(
            default=None,
            metadata={
                "name": "EnviarLoteRpsEnvio",
                "type": "Element",
                "namespace": "http://www.betha.com.br/e-nota-contribuinte-ws",
            }
        )


class RecepcionarLoteRpsEnviarLoteRpsEnvio:
    style = "document"
    location = "http://e-gov.betha.com.br/e-nota-contribuinte-ws/recepcionarLoteRps"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = RecepcionarLoteRpsEnviarLoteRpsEnvioInput
    output = RecepcionarLoteRpsEnviarLoteRpsEnvioOutput
