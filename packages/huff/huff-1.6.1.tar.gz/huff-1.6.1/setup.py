from setuptools import setup, find_packages
import os

def read_README():
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
        return f.read()
    
setup(
    name='huff',
    version='1.6.1',
    description='huff: Huff Model Market Area Analysis',
    packages=find_packages(include=["huff", "huff.tests"]),
    include_package_data=True,
    long_description=read_README(),
    long_description_content_type='text/markdown',
    author='Thomas Wieland',
    author_email='geowieland@googlemail.com',
    license_files=["LICENSE"],
    package_data={
        'huff': ['tests/data/*'],
    },
    install_requires=[
        'geopandas',
        'pandas',
        'numpy',
        'statsmodels==0.14.2',
        'scipy==1.15.3',
        'shapely',
        'requests',
        'matplotlib',
        'pillow',
        'contextily',
        'openpyxl'
    ],
    test_suite='tests',
)