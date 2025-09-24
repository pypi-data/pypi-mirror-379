# Copyright (c) OpenMMLab. All rights reserved.
from mim.commands.list import list_package
from mim.utils.default import OFFICIAL_MODULES


def get_installed_package(ctx, args, incomplete):
    pkgs = []
    for pkg, _, _ in list_package():
        pkgs.append(pkg)
    return pkgs


def get_downstream_package(ctx, args, incomplete):
    pkgs = []
    for pkg, _, _ in list_package():
        if pkg == 'onedl-mmcv':
            continue
        pkgs.append(pkg)
    return pkgs


def get_official_package(ctx=None, args=None, incomplete=None):
    return OFFICIAL_MODULES
