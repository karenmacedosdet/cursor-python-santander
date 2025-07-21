"""
Script para organizar arquivos em subpastas por categoria
na pasta Downloads.
"""

import os
import shutil

# Definição das categorias e extensões
CATEGORIAS = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
    "Outra": [],
}

PASTA_BASE = (
    r"C:\projetos\cursor\cursor-python-santander\projeto-07\Downloads"
)

# Arquivos que não devem ser movidos
ARQUIVOS_NAO_MOVER = {
    "organizar.py",
    "criar_arquivos.py",
    "__init__.py",
    "_init_.py",
}

# Cria um dicionário de extensão para categoria para busca rápida
ext_para_categoria = {}
for categoria, exts in CATEGORIAS.items():
    for ext in exts:
        ext_para_categoria[ext.lower()] = categoria

# Percorre todos os arquivos na pasta base
for nome_arquivo in os.listdir(PASTA_BASE):
    if nome_arquivo in ARQUIVOS_NAO_MOVER:
        continue
    caminho_arquivo = os.path.join(PASTA_BASE, nome_arquivo)
    if os.path.isfile(caminho_arquivo):
        _, ext = os.path.splitext(nome_arquivo)
        ext = ext.lower()
        categoria = ext_para_categoria.get(ext, "Outra")
        pasta_destino = os.path.join(PASTA_BASE, categoria)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        novo_caminho = os.path.join(pasta_destino, nome_arquivo)
        shutil.move(caminho_arquivo, novo_caminho)
