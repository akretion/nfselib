# Copyright (C) 2023 - TODAY Raphaël Valyi - Akretion

import os
import sys
from os import path
import importlib
import inspect
from enum import EnumMeta
from xmldiff import main

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pathlib import Path
import pkgutil


def visit_nested_classes(cls, classes):
    classes.add(cls)
    for attr in dir(cls):
        if attr == "__abstractmethods__":
            continue
        nested = getattr(cls, attr)
        if (
            not inspect.isclass(nested)
            or nested.__name__ == "type"
            or nested.__name__.endswith(".Meta")
        ):
            continue
        visit_nested_classes(nested, classes)


def test_init_all():
    for provider in pkgutil.walk_packages(["nfselib"]):
        provider_path = "nfselib/" + provider.name
        for modpkg in pkgutil.walk_packages([provider_path]):
            mod_name = "nfselib.%s.%s" % (
                provider.name,
                modpkg.name,
            )
            mod = importlib.import_module(mod_name)

            for _klass_name, klass in mod.__dict__.items():
                if isinstance(klass, type) and type(klass) != EnumMeta:
                    classes = set()
                    visit_nested_classes(klass, classes)
                    for cls in classes:
                        if cls.__name__ in (
                            "XmlDateTime",
                            "XmlDate",
                            "XmlPeriod",
                            "ABCMeta",
                        ):
                            continue
                        cls()
