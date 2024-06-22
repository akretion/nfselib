from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "NFe"


@dataclass
class SdtConsultaNotasProtocoloOutMessage:
    class Meta:
        name = "SDT_ConsultaNotasProtocoloOut.Message"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    LinErr: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtConsultaNotasProtocoloOutXmlNotasReg20ItemReg30Item:
    class Meta:
        name = "SDT_ConsultaNotasProtocoloOut.XML_Notas.Reg20Item.Reg30Item"

    TributoSigla: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TributoAliquota: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TributoValor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtConsultaNotasProtocoloOutXmlNotasReg90:
    class Meta:
        name = "SDT_ConsultaNotasProtocoloOut.XML_Notas.Reg90"

    QtdRegNormal: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorNFS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorISS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorDed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorIssRet: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    QtdReg30: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorTributos: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtConsultaProtocoloInLogin:
    class Meta:
        name = "SDT_ConsultaProtocoloIn.Login"

    CodigoUsuario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CodigoContribuinte: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtConsultaProtocoloOutMessage:
    class Meta:
        name = "SDT_ConsultaProtocoloOut.Message"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    LinErr: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtCancelaNfeLogin:
    class Meta:
        name = "Sdt_CancelaNFE.Login"

    CodigoUsuario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CodigoContribuinte: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtCancelaNfeNota:
    class Meta:
        name = "Sdt_CancelaNFE.Nota"

    SerieNota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumeroNota: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SerieRPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumeroRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorNota: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    MotivoCancelamento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    PodeCancelarGuia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtProcessarpsInLogin:
    class Meta:
        name = "Sdt_ProcessarpsIn.Login"

    CodigoUsuario: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CodigoContribuinte: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtProcessarpsInSdtrpsReg20ItemReg30Item:
    class Meta:
        name = "Sdt_ProcessarpsIn.SDTRPS.Reg20Item.Reg30Item"

    TributoSigla: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TributoAliquota: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TributoValor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtProcessarpsInSdtrpsReg90:
    class Meta:
        name = "Sdt_ProcessarpsIn.SDTRPS.Reg90"

    QtdRegNormal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorNFS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorISS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorDed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorIssRetTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    QtdReg30: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ValorTributos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtProcessarpsOutMessage:
    class Meta:
        name = "Sdt_ProcessarpsOut.Message"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    LinErr: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtRetornoCancelaNfeMessage:
    class Meta:
        name = "Sdt_RetornoCancelaNFE.Message"

    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class ArrayOfSdtConsultaNotasProtocoloOutMessage:
    class Meta:
        name = "ArrayOfSDT_ConsultaNotasProtocoloOut.Message"

    SDT_ConsultaNotasProtocoloOutMessage: List[
        SdtConsultaNotasProtocoloOutMessage
    ] = field(
        default_factory=list,
        metadata={
            "name": "SDT_ConsultaNotasProtocoloOut.Message",
            "type": "Element",
            "namespace": "NFe",
        },
    )


@dataclass
class ArrayOfSdtConsultaNotasProtocoloOutXmlNotasReg20ItemReg30Item:
    class Meta:
        name = "ArrayOfSDT_ConsultaNotasProtocoloOut.XML_Notas.Reg20Item.Reg30Item"

    SDT_ConsultaNotasProtocoloOutXML_NotasReg20ItemReg30Item: List[
        SdtConsultaNotasProtocoloOutXmlNotasReg20ItemReg30Item
    ] = field(
        default_factory=list,
        metadata={
            "name": "SDT_ConsultaNotasProtocoloOut.XML_Notas.Reg20Item.Reg30Item",
            "type": "Element",
            "namespace": "NFe",
        },
    )


@dataclass
class ArrayOfSdtConsultaProtocoloOutMessage:
    class Meta:
        name = "ArrayOfSDT_ConsultaProtocoloOut.Message"

    SDT_ConsultaProtocoloOutMessage: List[SdtConsultaProtocoloOutMessage] = (
        field(
            default_factory=list,
            metadata={
                "name": "SDT_ConsultaProtocoloOut.Message",
                "type": "Element",
                "namespace": "NFe",
            },
        )
    )


@dataclass
class ArrayOfSdtProcessarpsInSdtrpsReg20ItemReg30Item:
    class Meta:
        name = "ArrayOfSdt_ProcessarpsIn.SDTRPS.Reg20Item.Reg30Item"

    Sdt_ProcessarpsInSDTRPSReg20ItemReg30Item: List[
        SdtProcessarpsInSdtrpsReg20ItemReg30Item
    ] = field(
        default_factory=list,
        metadata={
            "name": "Sdt_ProcessarpsIn.SDTRPS.Reg20Item.Reg30Item",
            "type": "Element",
            "namespace": "NFe",
        },
    )


@dataclass
class ArrayOfSdtProcessarpsOutMessage:
    class Meta:
        name = "ArrayOfSdt_ProcessarpsOut.Message"

    Sdt_ProcessarpsOutMessage: List[SdtProcessarpsOutMessage] = field(
        default_factory=list,
        metadata={
            "name": "Sdt_ProcessarpsOut.Message",
            "type": "Element",
            "namespace": "NFe",
        },
    )


@dataclass
class ArrayOfSdtRetornoCancelaNfeMessage:
    class Meta:
        name = "ArrayOfSdt_RetornoCancelaNFE.Message"

    Sdt_RetornoCancelaNFEMessage: List[SdtRetornoCancelaNfeMessage] = field(
        default_factory=list,
        metadata={
            "name": "Sdt_RetornoCancelaNFE.Message",
            "type": "Element",
            "namespace": "NFe",
        },
    )


@dataclass
class SdtConsultaNotasProtocoloOutXmlNotasReg20Item:
    class Meta:
        name = "SDT_ConsultaNotasProtocoloOut.XML_Notas.Reg20Item"

    TipoNf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumNf: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SerNf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DtEmiNf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DtHrGerNf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CodVernf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumRps: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SerRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DtEmiRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TipoCpfCnpjPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CpfCnpjPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    RazSocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    LogPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumEndPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ComplEndPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    BairroPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    MunPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SiglaUFPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CepPre: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    EmailPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TipoTribPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DtAdeSN: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    AlqIssSN: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SitNf: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DataCncNf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    MotivoCncNf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TipoCpfCnpjTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CpfCnpjTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    RazSocTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    LogTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumEndTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ComplEndTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    BairroTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    MunTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SiglaUFTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CepTom: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    EMailTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    LogLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumEndLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ComplEndLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    BairroLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    MunLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SiglaUFLocpre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CepLocPre: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CodSrv: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DiscrSrv: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlNFS: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlDed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DiscrDed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlBasCalc: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    AlqIss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlIss: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlIssRet: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Reg30: Optional["SdtConsultaNotasProtocoloOutXmlNotasReg20Item.Reg30"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "NFe",
                "required": True,
            },
        )
    )

    @dataclass
    class Reg30:
        Reg30Item: List[
            SdtConsultaNotasProtocoloOutXmlNotasReg20ItemReg30Item
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class SdtConsultaProtocoloIn:
    class Meta:
        name = "SDT_ConsultaProtocoloIn"

    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Login: Optional[SdtConsultaProtocoloInLogin] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtConsultaProtocoloOut:
    class Meta:
        name = "SDT_ConsultaProtocoloOut"

    Retorno: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    PrtXSts: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    PrtCSerRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    PrtCRps_1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    PrtCRps_2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    PrtLPrcIni: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "nillable": True,
        },
    )
    PrtLFinGrv: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "nillable": True,
        },
    )
    PnfCNfe_1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    PnfCnfe_2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Messages: Optional["SdtConsultaProtocoloOut.Messages"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )

    @dataclass
    class Messages:
        Message: List[SdtConsultaProtocoloOutMessage] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class SdtCancelaNfe:
    class Meta:
        name = "Sdt_CancelaNFE"

    Login: Optional[SdtCancelaNfeLogin] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Nota: Optional[SdtCancelaNfeNota] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class SdtProcessarpsInSdtrpsReg20Item:
    class Meta:
        name = "Sdt_ProcessarpsIn.SDTRPS.Reg20Item"

    TipoNFS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SerRps: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DtEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    RetFonte: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CodSrv: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DiscrSrv: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlNFS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlDed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DiscrDed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlBasCalc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    AlqIss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlIss: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    VlIssRet: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CpfCnpTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    RazSocTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TipoLogtom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    LogTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumEndTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ComplEndTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    BairroTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    MunTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SiglaUFTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CepTom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Telefone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    InscricaoMunicipal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TipoLogLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    LogLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    NumEndLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    ComplEndLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    BairroLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    MunLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SiglaUFLocpre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CepLocPre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Email1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Email2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Email3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Reg30: Optional["SdtProcessarpsInSdtrpsReg20Item.Reg30"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )

    @dataclass
    class Reg30:
        Reg30Item: List[SdtProcessarpsInSdtrpsReg20ItemReg30Item] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class SdtProcessarpsOut:
    class Meta:
        name = "Sdt_ProcessarpsOut"

    Retorno: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Protocolo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Messages: Optional["SdtProcessarpsOut.Messages"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )

    @dataclass
    class Messages:
        Message: List[SdtProcessarpsOutMessage] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class SdtRetornoCancelaNfe:
    class Meta:
        name = "Sdt_RetornoCancelaNFE"

    Retorno: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Messages: Optional["SdtRetornoCancelaNfe.Messages"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )

    @dataclass
    class Messages:
        Message: List[SdtRetornoCancelaNfeMessage] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class ArrayOfSdtConsultaNotasProtocoloOutXmlNotasReg20Item:
    class Meta:
        name = "ArrayOfSDT_ConsultaNotasProtocoloOut.XML_Notas.Reg20Item"

    SDT_ConsultaNotasProtocoloOutXML_NotasReg20Item: List[
        SdtConsultaNotasProtocoloOutXmlNotasReg20Item
    ] = field(
        default_factory=list,
        metadata={
            "name": "SDT_ConsultaNotasProtocoloOut.XML_Notas.Reg20Item",
            "type": "Element",
            "namespace": "NFe",
        },
    )


@dataclass
class ArrayOfSdtProcessarpsInSdtrpsReg20Item:
    class Meta:
        name = "ArrayOfSdt_ProcessarpsIn.SDTRPS.Reg20Item"

    Sdt_ProcessarpsInSDTRPSReg20Item: List[SdtProcessarpsInSdtrpsReg20Item] = (
        field(
            default_factory=list,
            metadata={
                "name": "Sdt_ProcessarpsIn.SDTRPS.Reg20Item",
                "type": "Element",
                "namespace": "NFe",
            },
        )
    )


@dataclass
class SdtConsultaNotasProtocoloOutXmlNotas:
    class Meta:
        name = "SDT_ConsultaNotasProtocoloOut.XML_Notas"

    CpfCnpj: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DtIni: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "nillable": True,
        },
    )
    DtFin: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "nillable": True,
        },
    )
    TipoArq: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Reg20: Optional["SdtConsultaNotasProtocoloOutXmlNotas.Reg20"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Reg90: Optional[SdtConsultaNotasProtocoloOutXmlNotasReg90] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )

    @dataclass
    class Reg20:
        Reg20Item: List[SdtConsultaNotasProtocoloOutXmlNotasReg20Item] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class SdtProcessarpsInSdtrps:
    class Meta:
        name = "Sdt_ProcessarpsIn.SDTRPS"

    Ano: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Mes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    CPFCNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DTIni: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DTFin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    TipoTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    DtAdeSN: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    AlqIssSN_IP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Reg20: Optional["SdtProcessarpsInSdtrps.Reg20"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Reg90: Optional[SdtProcessarpsInSdtrpsReg90] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )

    @dataclass
    class Reg20:
        Reg20Item: List[SdtProcessarpsInSdtrpsReg20Item] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class WsNfeCancelanotaeletronica:
    class Meta:
        name = "ws_nfe.CANCELANOTAELETRONICA"
        namespace = "NFe"

    Sdt_cancelanfe: Optional[SdtCancelaNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WsNfeCancelanotaeletronicaresponse:
    class Meta:
        name = "ws_nfe.CANCELANOTAELETRONICAResponse"
        namespace = "NFe"

    Sdt_retornocancelanfe: Optional[SdtRetornoCancelaNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WsNfeConsultanotasprotocolo:
    class Meta:
        name = "ws_nfe.CONSULTANOTASPROTOCOLO"
        namespace = "NFe"

    Sdt_consultanotasprotocoloin: Optional[SdtConsultaProtocoloIn] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WsNfeConsultaprotocolo:
    class Meta:
        name = "ws_nfe.CONSULTAPROTOCOLO"
        namespace = "NFe"

    Sdt_consultaprotocoloin: Optional[SdtConsultaProtocoloIn] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WsNfeConsultaprotocoloresponse:
    class Meta:
        name = "ws_nfe.CONSULTAPROTOCOLOResponse"
        namespace = "NFe"

    Sdt_consultaprotocoloout: Optional[SdtConsultaProtocoloOut] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WsNfeProcessarpsresponse:
    class Meta:
        name = "ws_nfe.PROCESSARPSResponse"
        namespace = "NFe"

    Sdt_processarpsout: Optional[SdtProcessarpsOut] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WsNfeVerficarpsresponse:
    class Meta:
        name = "ws_nfe.VERFICARPSResponse"
        namespace = "NFe"

    Sdt_processarpsout: Optional[SdtProcessarpsOut] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SdtConsultaNotasProtocoloOut:
    class Meta:
        name = "SDT_ConsultaNotasProtocoloOut"

    Retorno: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    Messages: Optional["SdtConsultaNotasProtocoloOut.Messages"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    XML_Notas: Optional[SdtConsultaNotasProtocoloOutXmlNotas] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )

    @dataclass
    class Messages:
        Message: List[SdtConsultaNotasProtocoloOutMessage] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class SdtProcessarpsIn:
    class Meta:
        name = "Sdt_ProcessarpsIn"

    Login: Optional[SdtProcessarpsInLogin] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )
    SDTRPS: Optional[SdtProcessarpsInSdtrps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "NFe",
            "required": True,
        },
    )


@dataclass
class WsNfeSoapPortCancelanotaeletronicaInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortCancelanotaeletronicaInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfeCANCELANOTAELETRONICA: Optional[WsNfeCancelanotaeletronica] = (
            field(
                default=None,
                metadata={
                    "name": "ws_nfe.CANCELANOTAELETRONICA",
                    "type": "Element",
                    "namespace": "NFe",
                },
            )
        )


@dataclass
class WsNfeSoapPortCancelanotaeletronicaOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortCancelanotaeletronicaOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfeCANCELANOTAELETRONICAResponse: Optional[
            WsNfeCancelanotaeletronicaresponse
        ] = field(
            default=None,
            metadata={
                "name": "ws_nfe.CANCELANOTAELETRONICAResponse",
                "type": "Element",
                "namespace": "NFe",
            },
        )
        Fault: Optional[
            "WsNfeSoapPortCancelanotaeletronicaOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsNfeSoapPortConsultanotasprotocoloInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortConsultanotasprotocoloInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfeCONSULTANOTASPROTOCOLO: Optional[WsNfeConsultanotasprotocolo] = (
            field(
                default=None,
                metadata={
                    "name": "ws_nfe.CONSULTANOTASPROTOCOLO",
                    "type": "Element",
                    "namespace": "NFe",
                },
            )
        )


@dataclass
class WsNfeSoapPortConsultaprotocoloInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortConsultaprotocoloInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfeCONSULTAPROTOCOLO: Optional[WsNfeConsultaprotocolo] = field(
            default=None,
            metadata={
                "name": "ws_nfe.CONSULTAPROTOCOLO",
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class WsNfeSoapPortConsultaprotocoloOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortConsultaprotocoloOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfeCONSULTAPROTOCOLOResponse: Optional[
            WsNfeConsultaprotocoloresponse
        ] = field(
            default=None,
            metadata={
                "name": "ws_nfe.CONSULTAPROTOCOLOResponse",
                "type": "Element",
                "namespace": "NFe",
            },
        )
        Fault: Optional["WsNfeSoapPortConsultaprotocoloOutput.Body.Fault"] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsNfeSoapPortProcessarpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortProcessarpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfePROCESSARPSResponse: Optional[WsNfeProcessarpsresponse] = field(
            default=None,
            metadata={
                "name": "ws_nfe.PROCESSARPSResponse",
                "type": "Element",
                "namespace": "NFe",
            },
        )
        Fault: Optional["WsNfeSoapPortProcessarpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsNfeSoapPortVerficarpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortVerficarpsOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfeVERFICARPSResponse: Optional[WsNfeVerficarpsresponse] = field(
            default=None,
            metadata={
                "name": "ws_nfe.VERFICARPSResponse",
                "type": "Element",
                "namespace": "NFe",
            },
        )
        Fault: Optional["WsNfeSoapPortVerficarpsOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsNfeConsultanotasprotocoloresponse:
    class Meta:
        name = "ws_nfe.CONSULTANOTASPROTOCOLOResponse"
        namespace = "NFe"

    Sdt_consultanotasprotocoloout: Optional[SdtConsultaNotasProtocoloOut] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
    )


@dataclass
class WsNfeProcessarps:
    class Meta:
        name = "ws_nfe.PROCESSARPS"
        namespace = "NFe"

    Sdt_processarpsin: Optional[SdtProcessarpsIn] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WsNfeVerficarps:
    class Meta:
        name = "ws_nfe.VERFICARPS"
        namespace = "NFe"

    Sdt_processarpsin: Optional[SdtProcessarpsIn] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class WsNfeSoapPortCancelanotaeletronica:
    style = "document"
    location = (
        "https://nfe.etransparencia.com.br/mg.varginha/webservice/aws_nfe.aspx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "NFeaction/AWS_NFE.CANCELANOTAELETRONICA"
    input = WsNfeSoapPortCancelanotaeletronicaInput
    output = WsNfeSoapPortCancelanotaeletronicaOutput


class WsNfeSoapPortConsultaprotocolo:
    style = "document"
    location = (
        "https://nfe.etransparencia.com.br/mg.varginha/webservice/aws_nfe.aspx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "NFeaction/AWS_NFE.CONSULTAPROTOCOLO"
    input = WsNfeSoapPortConsultaprotocoloInput
    output = WsNfeSoapPortConsultaprotocoloOutput


@dataclass
class WsNfeSoapPortConsultanotasprotocoloOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortConsultanotasprotocoloOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfeCONSULTANOTASPROTOCOLOResponse: Optional[
            WsNfeConsultanotasprotocoloresponse
        ] = field(
            default=None,
            metadata={
                "name": "ws_nfe.CONSULTANOTASPROTOCOLOResponse",
                "type": "Element",
                "namespace": "NFe",
            },
        )
        Fault: Optional[
            "WsNfeSoapPortConsultanotasprotocoloOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


@dataclass
class WsNfeSoapPortProcessarpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortProcessarpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfePROCESSARPS: Optional[WsNfeProcessarps] = field(
            default=None,
            metadata={
                "name": "ws_nfe.PROCESSARPS",
                "type": "Element",
                "namespace": "NFe",
            },
        )


@dataclass
class WsNfeSoapPortVerficarpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["WsNfeSoapPortVerficarpsInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        ws_nfeVERFICARPS: Optional[WsNfeVerficarps] = field(
            default=None,
            metadata={
                "name": "ws_nfe.VERFICARPS",
                "type": "Element",
                "namespace": "NFe",
            },
        )


class WsNfeSoapPortConsultanotasprotocolo:
    style = "document"
    location = (
        "https://nfe.etransparencia.com.br/mg.varginha/webservice/aws_nfe.aspx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "NFeaction/AWS_NFE.CONSULTANOTASPROTOCOLO"
    input = WsNfeSoapPortConsultanotasprotocoloInput
    output = WsNfeSoapPortConsultanotasprotocoloOutput


class WsNfeSoapPortProcessarps:
    style = "document"
    location = (
        "https://nfe.etransparencia.com.br/mg.varginha/webservice/aws_nfe.aspx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "NFeaction/AWS_NFE.PROCESSARPS"
    input = WsNfeSoapPortProcessarpsInput
    output = WsNfeSoapPortProcessarpsOutput


class WsNfeSoapPortVerficarps:
    style = "document"
    location = (
        "https://nfe.etransparencia.com.br/mg.varginha/webservice/aws_nfe.aspx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "NFeaction/AWS_NFE.VERFICARPS"
    input = WsNfeSoapPortVerficarpsInput
    output = WsNfeSoapPortVerficarpsOutput
