import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='dealcloud-api-wrapper',
    version='0.0.5',    
    description='A python wrapper for easily interacting with the Dealcloud REST API.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/geg2102/dealcloud_api_wrapper',
    author='Geoffrey Grossman',
    author_email='ggrossman1@gmail.com',
    license='MIT',
    packages= find_packages(),
    install_requires=['requests',
                      'requests_oauthlib',
                      'oauthlib'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
