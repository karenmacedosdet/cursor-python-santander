"""
Editor de notas simples com Tkinter para abrir e salvar
arquivos de texto.
"""

import tkinter as tk
from tkinter import filedialog, messagebox


def abrir_arquivo():
    """Abre um arquivo de texto e exibe o conteúdo na área de texto."""
    filepath = filedialog.askopenfilename(
        filetypes=[
            ("Arquivos de texto", "*.txt"),
            ("Todos os arquivos", "*.*"),
        ]
    )
    if not filepath:
        return
    try:
        with open(filepath, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        texto_area.delete(1.0, tk.END)
        texto_area.insert(tk.END, conteudo)
    except OSError as e:
        messagebox.showerror(
            "Erro", f"Não foi possível abrir o arquivo:\n{e}"
        )


def salvar_arquivo():
    """Salva o conteúdo da área de texto em um arquivo de texto."""
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Arquivos de texto", "*.txt"),
            ("Todos os arquivos", "*.*"),
        ],
    )
    if not filepath:
        return
    try:
        conteudo = texto_area.get(1.0, tk.END)
        with open(filepath, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except OSError as e:
        messagebox.showerror(
            "Erro", f"Não foi possível salvar o arquivo:\n{e}"
        )


# Funções para Editar
def copiar():
    """Copia o texto selecionado para a área de transferência."""
    texto_area.event_generate("<<Copy>>")


def colar():
    """Cola o texto da área de transferência."""
    texto_area.event_generate("<<Paste>>")


def recortar():
    """Recorta o texto selecionado para a área de transferência."""
    texto_area.event_generate("<<Cut>>")


root = tk.Tk()
root.title("Editor de Notas")
root.geometry("600x400")

texto_area = tk.Text(root)
texto_area.pack(expand=True, fill=tk.BOTH)

menubar = tk.Menu(root)
arquivo_menu = tk.Menu(menubar, tearoff=0)
arquivo_menu.add_command(label="Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
menubar.add_cascade(label="Arquivo", menu=arquivo_menu)

# Menu Editar com Recortar, Copiar, Colar
editar_menu = tk.Menu(menubar, tearoff=0)
editar_menu.add_command(label="Recortar", command=recortar)
editar_menu.add_command(label="Copiar", command=copiar)
editar_menu.add_command(label="Colar", command=colar)
menubar.add_cascade(label="Editar", menu=editar_menu)

root.config(menu=menubar)

root.mainloop()
