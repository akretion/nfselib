from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://tempuri.org/"


@dataclass
class InfseServicesCancelarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesCancelarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse: Optional[str] = field(
            default=None,
            metadata={
                "name": "CancelarNfse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class InfseServicesCancelarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesCancelarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        cancelar_nfse_response: Optional[str] = field(
            default=None,
            metadata={
                "name": "CancelarNfseResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["InfseServicesCancelarNfseOutput.Body.Fault"] = field(
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
class InfseServicesConsultarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesConsultarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRps",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class InfseServicesConsultarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesConsultarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_lote_rps_response: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConsultarLoteRpsResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["InfseServicesConsultarLoteRpsOutput.Body.Fault"] = field(
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
class InfseServicesConsultarNfsePorRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesConsultarNfsePorRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rps: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorRps",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class InfseServicesConsultarNfsePorRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesConsultarNfsePorRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_por_rps_response: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConsultarNfsePorRpsResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["InfseServicesConsultarNfsePorRpsOutput.Body.Fault"] = field(
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
class InfseServicesConsultarNfseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesConsultarNfseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConsultarNfse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class InfseServicesConsultarNfseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesConsultarNfseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_nfse_response: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConsultarNfseResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["InfseServicesConsultarNfseOutput.Body.Fault"] = field(
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
class InfseServicesConsultarSituacaoLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesConsultarSituacaoLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRps",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class InfseServicesConsultarSituacaoLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesConsultarSituacaoLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        consultar_situacao_lote_rps_response: Optional[str] = field(
            default=None,
            metadata={
                "name": "ConsultarSituacaoLoteRpsResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["InfseServicesConsultarSituacaoLoteRpsOutput.Body.Fault"] = field(
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
class InfseServicesRecepcionarLoteRpsInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesRecepcionarLoteRpsInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps: Optional[str] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRps",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )


@dataclass
class InfseServicesRecepcionarLoteRpsOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["InfseServicesRecepcionarLoteRpsOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        recepcionar_lote_rps_response: Optional[str] = field(
            default=None,
            metadata={
                "name": "RecepcionarLoteRpsResponse",
                "type": "Element",
                "namespace": "http://tempuri.org/",
            }
        )
        fault: Optional["InfseServicesRecepcionarLoteRpsOutput.Body.Fault"] = field(
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


class InfseServicesCancelarNfse:
    uri = "#BasicHttpBinding_INfseServices_policy"
    style = "document"
    location = "https://www1.webiss.com.br/uberaba_wsnfse/NfseServices.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/INfseServices/CancelarNfse"
    input = InfseServicesCancelarNfseInput
    output = InfseServicesCancelarNfseOutput


class InfseServicesConsultarLoteRps:
    uri = "#BasicHttpBinding_INfseServices_policy"
    style = "document"
    location = "https://www1.webiss.com.br/uberaba_wsnfse/NfseServices.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/INfseServices/ConsultarLoteRps"
    input = InfseServicesConsultarLoteRpsInput
    output = InfseServicesConsultarLoteRpsOutput


class InfseServicesConsultarNfse:
    uri = "#BasicHttpBinding_INfseServices_policy"
    style = "document"
    location = "https://www1.webiss.com.br/uberaba_wsnfse/NfseServices.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/INfseServices/ConsultarNfse"
    input = InfseServicesConsultarNfseInput
    output = InfseServicesConsultarNfseOutput


class InfseServicesConsultarNfsePorRps:
    uri = "#BasicHttpBinding_INfseServices_policy"
    style = "document"
    location = "https://www1.webiss.com.br/uberaba_wsnfse/NfseServices.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/INfseServices/ConsultarNfsePorRps"
    input = InfseServicesConsultarNfsePorRpsInput
    output = InfseServicesConsultarNfsePorRpsOutput


class InfseServicesConsultarSituacaoLoteRps:
    uri = "#BasicHttpBinding_INfseServices_policy"
    style = "document"
    location = "https://www1.webiss.com.br/uberaba_wsnfse/NfseServices.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/INfseServices/ConsultarSituacaoLoteRps"
    input = InfseServicesConsultarSituacaoLoteRpsInput
    output = InfseServicesConsultarSituacaoLoteRpsOutput


class InfseServicesRecepcionarLoteRps:
    uri = "#BasicHttpBinding_INfseServices_policy"
    style = "document"
    location = "https://www1.webiss.com.br/uberaba_wsnfse/NfseServices.svc"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://tempuri.org/INfseServices/RecepcionarLoteRps"
    input = InfseServicesRecepcionarLoteRpsInput
    output = InfseServicesRecepcionarLoteRpsOutput
