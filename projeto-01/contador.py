from collections import Counter
import re


def contar_palavras(caminho_arquivo):
    """
    Conta o total de palavras em um arquivo de texto e exibe as 10 palavras mais comuns.

    Args:
        caminho_arquivo (str): O caminho completo para o arquivo de texto.
    """
    try:
        # Abre o arquivo para leitura com codificação UTF-8
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            texto = f.read()
        # Encontra todas as "palavras" (sequências alfanuméricas) e converte para minúsculas
        palavras = re.findall(r"\w+", texto.lower())

        # Verifica se alguma palavra foi encontrada antes de processar
        if not palavras:
            print(f"Nenhuma palavra encontrada no arquivo: {caminho_arquivo}")
            return

        total_palavras = len(palavras)
        print(f"Total de palavras: {total_palavras}")

        print("\nTop 10 palavras mais comuns:")
        for palavra, contagem in Counter(palavras).most_common(10):
            print(f"- {palavra}: {contagem}")

    except FileNotFoundError:
        # Captura o erro se o arquivo não for encontrado
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado. Por favor, verifique o caminho.")
    except Exception as e:
        # Captura qualquer outro erro inesperado durante a leitura ou processamento
        print(f"Ocorreu um erro inesperado ao processar o arquivo: {e}")


if __name__ == "__main__":
    print("--- Contador de Palavras em Arquivo de Texto ---")
    caminho_do_arquivo_input = input("Digite o caminho completo para o arquivo de texto: ")
    contar_palavras(caminho_do_arquivo_input)
    print("\n--- Processamento concluído ---")
