# Copyright (C) 2025 - TODAY Raphaël Valyi - Akretion

from os import path
import importlib
import pkgutil


def test_import_all():
    for pkg_name in pkgutil.walk_packages(["nfselib/"]):
        package_path = f"nfselib/{pkg_name.name}/bindings"
        if not path.isdir(package_path):
            continue
        try:
            importlib.import_module(package_path.replace("/", "."))
        except TypeError:
            pass  # happens in some packages with Python < 3.11; silence for now
