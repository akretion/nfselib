from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://schemas.microsoft.com/2003/10/Serialization/"


@dataclass
class Qname:
    class Meta:
        name = "QName"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class AnyType:
    class Meta:
        name = "anyType"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AnyUri:
    class Meta:
        name = "anyURI"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[str] = field(
        default="",
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Base64Binary:
    class Meta:
        name = "base64Binary"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "nillable": True,
            "format": "base64",
        },
    )


@dataclass
class Boolean:
    class Meta:
        name = "boolean"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Byte:
    class Meta:
        name = "byte"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Char:
    class Meta:
        name = "char"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class DateTime:
    class Meta:
        name = "dateTime"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class DecimalType:
    class Meta:
        name = "decimal"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Double:
    class Meta:
        name = "double"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[float] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Duration:
    class Meta:
        name = "duration"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[str] = field(
        default="",
        metadata={
            "min_inclusive": "-P10675199DT2H48M5.4775808S",
            "max_inclusive": "P10675199DT2H48M5.4775807S",
            "pattern": r"\-?P(\d*D)?(T(\d*H)?(\d*M)?(\d*(\.\d*)?S)?)?",
            "nillable": True,
        },
    )


@dataclass
class Float:
    class Meta:
        name = "float"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[float] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Guid:
    class Meta:
        name = "guid"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[str] = field(
        default="",
        metadata={
            "pattern": r"[\da-fA-F]{8}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{12}",
            "nillable": True,
        },
    )


@dataclass
class Int:
    class Meta:
        name = "int"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Long:
    class Meta:
        name = "long"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class Short:
    class Meta:
        name = "short"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class String:
    class Meta:
        name = "string"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[str] = field(
        default="",
        metadata={
            "nillable": True,
        },
    )


@dataclass
class UnsignedByte:
    class Meta:
        name = "unsignedByte"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class UnsignedInt:
    class Meta:
        name = "unsignedInt"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class UnsignedLong:
    class Meta:
        name = "unsignedLong"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )


@dataclass
class UnsignedShort:
    class Meta:
        name = "unsignedShort"
        nillable = True
        namespace = "http://schemas.microsoft.com/2003/10/Serialization/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )
