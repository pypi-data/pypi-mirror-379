from setuptools import setup,find_packages

setup(
    name='aplicacion_ventas_hflores',# nombre unico
    version='0.1.0',
    author='Hugo Flores Mora',
    author_email='huflomo01@gmail.com',
    description='Paquete para gestionar ventas, precios, impuestos y descuentos',
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tu_usuario/gestor_ventas',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)