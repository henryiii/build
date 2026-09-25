# SPDX-License-Identifier: MIT


def get_requires_for_build_sdist(config_settings=None):
    return ['sdist-dep']


def get_requires_for_build_wheel(config_settings=None):
    return ['wheel-dep', *(config_settings or {}).get('extra', '').split()]


def get_requires_for_build_editable(config_settings=None):
    return ['editable-dep']
