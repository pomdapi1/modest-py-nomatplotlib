from setuptools import setup

setup(
    name='modestpy',
    version='0.1',
    description='FMI-compliant model identification package',
    url='https://github.com/sdu-cfei/modest-py',
    keywords='fmi fmu optimization model identification estimation',
    author='Krzysztof Arendt, Center for Energy Informatics SDU',
    author_email='krzysztof.arendt@gmail.com, veje@mmmi.sdu.dk',
    license='BSD',
    platforms=['Windows', 'Linux'],
    packages=[
        'modestpy',
        'modestpy.estim',
        'modestpy.estim.ga_parallel',
        'modestpy.estim.ga',
        'modestpy.estim.ps',
        'modestpy.estim.scipy',
        'modestpy.fmi',
        'modestpy.utilities',
        'modestpy.test'],
    include_package_data=True,
    install_requires=[
        'fmpy[complete]',
        'scipy',
        'pandas',
        'numpy',
        'pyDOE',
        'modestga'
    ],
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)
