

from setuptools import setup, find_packages

setup(
    name='simple-calculator-abdulqader-alalfi',
    version='0.1.0',
    author='Abdulqader Alalfi',
    author_email='abdulqader.alalfi@example.com', # Placeholder email
    description='A simple calculator package for basic math operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/abdulqader-alalfi/simple-calculator', # Placeholder URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


