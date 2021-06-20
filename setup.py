# Standard Library
import os

# Third Party
from setuptools import find_packages, setup

CURRENT_WORKING_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_WORKING_DIRECTORY, 'README.md')) as fp:
    README = fp.read()

setup(
    name='vb-console',
    version='1.1.0',
    description='Logger and object inspector for Python',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/vbyazilim/vb-console',
    author='vb YAZILIM',
    author_email='hello@vbyazilim.com',
    license='MIT',
    python_requires='>=3.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=['tests', 'examples']),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='vbyazilim, console, debug, log, test',
    project_urls={
        'VB YAZILIM': 'https://vbyazilim.com',
        'Source': 'https://github.com/vbyazilim/vb-console',
    },
    include_package_data=True,
)
