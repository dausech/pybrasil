from distutils.core import setup

setup(
    name='pybrasil',
    version='0.0.0.1',
    packages=[
        'pybrasil',
        'pybrasil.ncm',
        'pybrasil.base',
        'pybrasil.data',
        'pybrasil.ibge',
        'pybrasil.valor',
        'pybrasil.feriado',
        'pybrasil.produto',
        'pybrasil.telefone',
        'pybrasil.template',
        'pybrasil.inscricao',
        'pybrasil.python_pt_BR'
    ],
    url='git@github.com:aricaldeira/pybrasil.git',
    license='',
    author='Aristides Caldeira',
    author_email='aristides.caldeira@tauga.com.br',
    description='',
    package_data = {
        '': ['*.txt'],
    },
    install_requires=[
        'python-dateutil',
        'pytz',
        'pyparsing',
        'mako'
    ],
)
