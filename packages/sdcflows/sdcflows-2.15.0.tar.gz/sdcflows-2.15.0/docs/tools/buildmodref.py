#!/usr/bin/env python
"""Script to auto-generate API docs."""

# stdlib imports
import sys

# version comparison
from distutils.version import LooseVersion as V

# local imports
from apigen import ApiDocWriter

# *****************************************************************************


def abort(error):
    print(f'*WARNING* API documentation not generated: {error}')
    exit()


def writeapi(package, outdir, source_version, other_defines=True):
    # Check that the package is available. If not, the API documentation is not
    # (re)generated and existing API documentation sources will be used.

    try:
        __import__(package)
    except ImportError:
        abort('Can not import ' + package)

    module = sys.modules[package]

    # Check that the source version is equal to the installed
    # version. If the versions mismatch the API documentation sources
    # are not (re)generated. This avoids automatic generation of documentation
    # for older or newer versions if such versions are installed on the system.

    installed_version = V(module.__version__)
    if source_version != installed_version:
        abort('Installed version does not match source version')

    docwriter = ApiDocWriter(package, rst_extension='.rst', other_defines=other_defines)

    docwriter.package_skip_patterns += [
        rf'\.{package}$',
        r'.*test.*$',
        r'\.version.*$',
    ]
    docwriter.write_api_docs(outdir)
    docwriter.write_index(outdir, 'index', relative_to=outdir)
    print(f'{len(docwriter.written_modules)} files written')


if __name__ == '__main__':
    package = sys.argv[1]
    outdir = sys.argv[2]
    try:
        other_defines = sys.argv[3]
    except IndexError:
        other_defines = True
    else:
        other_defines = other_defines in ('True', 'true', '1')

    writeapi(package, outdir, other_defines=other_defines)
