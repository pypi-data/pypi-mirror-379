from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='iissa-investimentpy',
    version='1.0.0',
    packages=find_packages(),
    description='Uma biblioteca para análise de investimentos',
    author='Ivan Alfredo Issa',
    author_email='ivanissa.dev@gmail.com',
    url='https://github.com/ivanissa/investimentpy',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown' 
)