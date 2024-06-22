from dataclasses import dataclass, field
from typing import List, Optional

from nfselib.paulistana.bindings.tipos_nfe_v01 import TpEvento

__NAMESPACE__ = "http://www.prefeitura.sp.gov.br/nfe"


@dataclass
class RetornoConsultaCnpj:
    """Schema utilizado para RETORNO de Pedidos de Consultas de CNPJ.

    Este Schema XML é utilizado pelo Web Service para informar aos
    tomadores e/ou prestadores de serviços quais Inscrições Municipais
    (CCM) estão vinculadas a um determinado CNPJ e se estes CCM emitem
    NFS-e ou não.

    :ivar Cabecalho: Cabeçalho do retorno.
    :ivar Alerta: Elemento que representa a ocorrência de eventos de
        alerta durante o processamento da mensagem XML.
    :ivar Erro: Elemento que representa a ocorrência de eventos de erro
        durante o processamento da mensagem XML.
    :ivar Detalhe:
    """

    class Meta:
        name = "RetornoConsultaCNPJ"
        namespace = "http://www.prefeitura.sp.gov.br/nfe"

    Cabecalho: Optional["RetornoConsultaCnpj.Cabecalho"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    Alerta: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Erro: List[TpEvento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    Detalhe: List["RetornoConsultaCnpj.Detalhe"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Cabecalho:
        """
        :ivar Sucesso: Campo indicativo do sucesso do pedido do serviço.
        :ivar Versao: Versão do Schema XML utilizado.
        """

        Sucesso: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        Versao: str = field(
            init=False,
            default="1",
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,3}",
            },
        )

    @dataclass
    class Detalhe:
        """
        :ivar InscricaoMunicipal: Inscrição Municipal vinculada ao CNPJ
            consultado.
        :ivar EmiteNFe: Campo que indica se o CCM vinculado ao CNPJ
            consultado emite NFS-e ou não.
        """

        InscricaoMunicipal: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "pattern": r"[0-9]{8,8}",
            },
        )
        EmiteNFe: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
