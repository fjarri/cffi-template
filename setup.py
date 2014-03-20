import sys
from setuptools import setup, Extension

try:
    import cffi
except ImportError:
    sys.stderr.write('Error: CFFI (required for setup) is not available.\n')
    sys.stderr.write('Please use "pip install cffi", or equivalent.\n')
    sys.exit(1)

import cffitest._wrapper as wrapper


setup(
    name='cffitest',
    version="0.1.0",
    author='Bogdan Opanchuk',
    author_email='bogdan@opanchuk.net',
    description='CFFI distribution test',
    install_requires=[
        "cffi>=0.8",
        ],
    packages=['cffitest'],
    provides=['cffitest'],
    package_data={wrapper.package: wrapper.create_api_header()},
    ext_package=wrapper.package,
    ext_modules=[
        wrapper.get_extension()
        ],
    zip_safe=False, # cffi requirement for setuptools
    )
