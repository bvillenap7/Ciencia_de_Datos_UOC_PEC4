from setuptools import setup, find_packages


setup(
    name='PEC4_Borja_Villena_Pardo',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'contourpy==1.2.0',
        'cycler==0.12.1',
        'fonttools==4.47.2',
        'kiwisolver==1.4.5',
        'matplotlib==3.8.2',
        'numpy==1.26.3',
        'packaging==23.2',
        'pandas==2.1.4',
        'pillow==10.2.0',
        'pyparsing==3.1.1',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'setuptools==69.0.3',
        'six==1.16.0',
        'tzdata==2023.4'
    ],
    author='Borja Villena Pardo',
    author_email='bvillenap@uoc.edu',
    description='Entregable para la PEC4 de la asignatura Programación '
                'para la Ciencia de Datos, Grado en Ingeniería para Ciencia '
                'de Datos Aplicada. Universidad Oberta de Catalunya, UOC',
    url='https://github.com/bvillenap7/UOC_PEC4',
)
