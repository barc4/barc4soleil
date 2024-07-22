from setuptools import setup, find_packages

setup(
    name='barc4soleil',
    version='0.1.0',
    author='Rafael Celestre',
    author_email='rafael.celestre@synchrotron-soleil.fr',
    description='An auxiliary Python package for calculations at Synchrotron SOLEIL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rafaelcelestre/barc4soleil',
    license='GPL-3.0',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)