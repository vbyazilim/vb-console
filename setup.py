import os

from setuptools import setup

CURRENT_WORKING_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_WORKING_DIRECTORY, 'README.md')) as fp:
    README = fp.read()

setup(
    name='vb-console',
    version='0.1.1',
    description='Logger and object inspector for Python',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/vbyazilim/vb-console',
    author='vb YAZILIM',
    author_email='hello@vbyazilim.com',
    license='MIT',
    python_requires='>=3.0',
    packages=['console'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    include_package_data=True,
)
