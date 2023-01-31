from setuptools import setup, find_packages

setup(
    name='systeminfo',
    version='0.1',
    description='This package contains some sample code about system information.',
    author='Anastasiia Skrypnykova',
    url='https://github.com/natasiia/systeminfo',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sys_info_comp30380 = systeminfo.main:main',
        ],
    },

)