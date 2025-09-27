
from setuptools import setup, find_packages

setup(
    name='simple-calculator-walid-fawaz',
    version='0.1.0',
    author='Walid Fawaz',
    author_email='walid.fawaz@example.com', # Placeholder email
    description='A simple calculator package for basic math operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/walidfawaz/simple-calculator', # Placeholder URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

