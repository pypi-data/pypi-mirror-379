from setuptools import setup, find_packages

setup(
    name='basitcrypto',
    version='0.1.0',
    packages=find_packages(),
    description='Simple encryption library (XOR, Caesar)',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Al-Junaid',
    author_email='Al-Junaid@google.com',
    url='https://github.com/yourusername/basitcrypto',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    
    python_requires='>=3.7'
     
)
