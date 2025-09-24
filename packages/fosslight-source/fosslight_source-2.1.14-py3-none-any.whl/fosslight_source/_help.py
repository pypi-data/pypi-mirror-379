#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
from fosslight_util.help import PrintHelpMsg, print_package_version

_HELP_MESSAGE_SOURCE_SCANNER = """
    FOSSLight Source Scanner Usage: fosslight_source [option1] <arg1> [option2] <arg2>...

    FOSSLight Source Scanner uses ScanCode and SCANOSS, the source code scanners, to detect
    the copyright and license phrases contained in the file.
    Some files (ex- build script), binary files, directory and files in specific
    directories (ex-test) are excluded from the result.

    Options:
        Optional
            -p <source_path>\t   Path to analyze source (Default: current directory)
            -h\t\t\t   Print help message
            -v\t\t\t   Print FOSSLight Source Scanner version
            -m\t\t\t   Print additional information for scan result on separate sheets
            -e <path>\t\t   Path to exclude from analysis (file and directory)
            -o <output_path>\t   Output path (Path or file name)
            -f <format>\t\t   Output file formats (excel, csv, opossum, yaml). Multi formats are supported.
        Options only for FOSSLight Source Scanner
            -s <scanner>\t   Select which scanner to be run (scancode, scanoss, all)
            -j\t\t\t   Generate raw result of scanners in json format
            -t <float>\t\t   Stop scancode scanning if scanning takes longer than a timeout in seconds.
            -c <core>\t\t   Select the number of cores to be scanned with ScanCode or threads with SCANOSS.
            --no_correction\t   Enter if you don't want to correct OSS information with sbom-info.yaml
            --correct_fpath <path> Path to the sbom-info.yaml file"""


def print_version(pkg_name: str) -> None:
    print_package_version(pkg_name, "FOSSLight Source Scanner Version:")


def print_help_msg_source_scanner() -> None:
    helpMsg = PrintHelpMsg(_HELP_MESSAGE_SOURCE_SCANNER)
    helpMsg.print_help_msg(True)
