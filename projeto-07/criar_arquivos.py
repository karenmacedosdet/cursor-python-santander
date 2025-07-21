"""
Script para criar arquivos de exemplo com várias extensões
na raiz do projeto-07, com nomes aleatórios e sem repetição.
"""

import os
import uuid

EXTENSOES = [
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".pdf",
    ".docx",
    ".txt",
    ".xlsx",
    ".mp4",
    ".avi",
    ".mkv",
    ".mp3",
    ".wav",
]

PASTA_DESTINO = (
    r"c:/projetos/cursor/cursor-python-santander/projeto-07/Downloads"
)

arquivos_existentes = set(os.listdir(PASTA_DESTINO))

for ext in EXTENSOES:
    contador = 0
    while contador < 2:
        nome_arquivo = f"{uuid.uuid4().hex}{ext}"
        if nome_arquivo not in arquivos_existentes:
            caminho = os.path.join(PASTA_DESTINO, nome_arquivo)
            if not os.path.exists(caminho):
                with open(caminho, "wb"):
                    pass
                arquivos_existentes.add(nome_arquivo)
                contador += 1
