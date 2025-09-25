#Realização de um pacote Python para processamento de imagens
# Este pacote inclui funcionalidades para combinação, transformação, leitura, salvamento e visualização de imagens

from setuptools import setup, find_packages # Importa funções necessárias do setuptools

with open("README.md", "r") as f: # Abre o arquivo README.md para a descrição longa
    page_description = f.read() # Lê o conteúdo do arquivo

with open("requirements.txt") as f: # Abre o arquivo requirements.txt para as dependências
    requirements = f.read().splitlines() # Lê as dependências linha por linha

setup(
    name="img_processing_sid", # Nome do pacote
    version="0.0.1", # Versão do pacote
    author="Sidnei Silva", # Autor do pacote
    author_email="supersidnei@gmail.com", # Email do autor
    description="Pacote Python para processamento de imagens: combinação, transformação, leitura, salvamento e visualização.", # Descrição curta do pacote
    long_description=page_description, # Descrição longa do pacote
    long_description_content_type="text/markdown", # Tipo de conteúdo da descrição longa
    url="https://github.com/sidneifs/imageprocessingpackage", # URL do repositório do pacote
    packages=find_packages(), # Encontra todos os pacotes e subpacotes automaticamente
    install_requires=requirements, # Dependências do pacote
    python_requires='>=3.7', # Requer Python 3.7 ou superior
)