from pathlib import Path
from setuptools import setup, find_packages

# Read version from __init__.py
init_py = Path(__file__).parent / "crypt2file" / "__init__.py"
version = ""
with open(init_py, "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break
if not version:
    raise RuntimeError("Cannot find version information")

# Read README.md for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='crypt2file',
    version=version,
    description='A simple tool to encrypt/decrypt files using a machine-specific key.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Kyunghoon',
    author_email='aloecandy@gmail.com',
    url='https://github.com/aloecandy/crypt2file',
    keywords=['crypt', 'file', 'encrypt', 'decrypt', 'security'],
    install_requires=[
        'cryptography'
    ],
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'crypt2file=crypt2file:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)