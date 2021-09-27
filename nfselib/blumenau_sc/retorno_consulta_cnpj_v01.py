from dataclasses import dataclass, field
from typing import List, Optional
from nfselib.blumenau_sc.tipos_nfe_v01 import TpEvento

__NAMESPACE__ = "http://nfse.blumenau.sc.gov.br"


@dataclass
class RetornoConsultaCnpj:
    """Schema utilizado para RETORNO de Pedidos de Consultas de CNPJ.

    Este Schema XML é utilizado pelo Web Service para informar aos
    tomadores e/ou prestadores de serviços quais Inscrições estão
    vinculadas a um determinado CNPJ e se estas Inscrições emitem NFS-e
    ou não.

    :ivar cabecalho: Cabeçalho do retorno.
    :ivar alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    :ivar detalhe:
    """
    class Meta:
        name = "RetornoConsultaCNPJ"
        namespace = "http://nfse.blumenau.sc.gov.br"

    cabecalho: Optional["RetornoConsultaCnpj.Cabecalho"] = field(
        default=None,
        metadata={
            "name": "Cabecalho",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    alerta: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "name": "Alerta",
            "type": "Element",
            "namespace": "",
        }
    )
    erro: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "name": "Erro",
            "type": "Element",
            "namespace": "",
        }
    )
    detalhe: List["RetornoConsultaCnpj.Detalhe"] = field(
        default_factory=list,
        metadata={
            "name": "Detalhe",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Cabecalho:
        """
        :ivar sucesso: Campo indicativo do sucesso do pedido do serviço.
        :ivar versao: Versão do Schema XML utilizado.
        """
        sucesso: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Sucesso",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        versao: str = field(
            init=False,
            default="1",
            metadata={
                "name": "Versao",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            }
        )

    @dataclass
    class Detalhe:
        """
        :ivar inscricao_municipal: Inscrição Municipal vinculada ao CNPJ
            consultado.
        :ivar emite_nfe: Campo que indica se a Inscrição vinculado ao
            CNPJ consultado emite NFS-e ou não.
        """
        inscricao_municipal: Optional[str] = field(
            default=None,
            metadata={
                "name": "InscricaoMunicipal",
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{1,15}",
            }
        )
        emite_nfe: Optional[bool] = field(
            default=None,
            metadata={
                "name": "EmiteNFe",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
