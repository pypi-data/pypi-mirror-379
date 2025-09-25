from struct import pack
from setuptools import setup, find_packages

setup(
    name ='mensajes-jcorredor',
    version = '6.0',
    description = 'Un paquete para saludar y despedir',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type = 'text/markdown',
    author = 'Zotyx',
    author_email = 'zotyxdk@gmail.com',
    url = 'https://www.google.com',
    license_files = ['LICENSE'],
    packages = find_packages(),
    scripts = [],
    test_suite = 'tests',
    install_requires = [paquete.strip() 
                        for paquete in open("requirements.txt").readlines()],
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.13'
    ]

)
