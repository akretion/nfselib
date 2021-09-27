from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class KeyValueType:
    rsakey_value: Optional["KeyValueType.RsakeyValue"] = field(
        default=None,
        metadata={
            "name": "RSAKeyValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )

    @dataclass
    class RsakeyValue:
        modulus: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "Modulus",
                "type": "Element",
                "namespace": "http://www.w3.org/2000/09/xmldsig#",
                "required": True,
                "format": "base64",
            }
        )
        exponent: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "Exponent",
                "type": "Element",
                "namespace": "http://www.w3.org/2000/09/xmldsig#",
                "required": True,
                "format": "base64",
            }
        )


@dataclass
class SignatureValueType:
    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
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
class TransformType:
    xpath: List[str] = field(
        default_factory=list,
        metadata={
            "name": "XPath",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class X509DataType:
    x509_certificate: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class KeyInfoType:
    x509_data: Optional[X509DataType] = field(
        default=None,
        metadata={
            "name": "X509Data",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
class TransformsType:
    transform: List[TransformType] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceType:
    transforms: Optional[TransformsType] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_method: Optional["ReferenceType.DigestMethod"] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )

    @dataclass
    class DigestMethod:
        algorithm: Optional[str] = field(
            default=None,
            metadata={
                "name": "Algorithm",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class SignedInfoType:
    canonicalization_method: Optional["SignedInfoType.CanonicalizationMethod"] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_method: Optional["SignedInfoType.SignatureMethod"] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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

    @dataclass
    class CanonicalizationMethod:
        algorithm: Optional[str] = field(
            default=None,
            metadata={
                "name": "Algorithm",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SignatureMethod:
        algorithm: Optional[str] = field(
            default=None,
            metadata={
                "name": "Algorithm",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class SignatureType:
    signed_info: Optional[SignedInfoType] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_value: Optional[SignatureValueType] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    key_info: Optional[KeyInfoType] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
class Signature(SignatureType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
