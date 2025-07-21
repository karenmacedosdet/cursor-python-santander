"""Aplicativo Flask simples com rota principal de boas-vindas."""

import json
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []
PROXIMO_ID = [1]  # Use a list to hold the next id

ARQUIVO_DADOS = os.path.join(os.path.dirname(__file__), "tarefas.json")


def salvar_dado():
    """Salva as tarefas e o próximo id no arquivo tarefas.json."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(
            {"proximo_id": PROXIMO_ID[0], "tarefas": tarefas},
            f,
            ensure_ascii=False,
            indent=2,
        )


def adicionar_tarefa(texto: str) -> dict:
    """Adiciona uma nova tarefa à lista global."""
    tarefa = {"id": PROXIMO_ID[0], "texto": texto, "feito": False}
    tarefas.append(tarefa)
    PROXIMO_ID[0] += 1
    salvar_dado()
    return tarefa


def completar_tarefa(tarefa_id: int) -> bool:
    """Marca a tarefa com o id fornecido como completa."""
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["feito"] = True
            salvar_dado()
            return True
    return False


def carregar_dado():
    """Carrega as tarefas e o próximo id
    do arquivo tarefas.json, se existir.
    """
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dado = json.load(f)
            tarefas.clear()
            tarefas.extend(dado.get("tarefas", []))
            PROXIMO_ID[0] = dado.get("proximo_id", 1)
    except FileNotFoundError:
        pass


carregar_dado()


@app.route("/")
def index():
    """Página principal: exibe tarefas classificadas (incompletas primeiro)."""
    tarefas_classificadas = sorted(tarefas, key=lambda t: t["feito"])
    return render_template("index.html", tarefas=tarefas_classificadas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    """Adiciona uma nova tarefa a partir do formulário
    e redireciona para a página principal.
    """
    texto_tarefa = request.form.get("texto_tarefa")
    if texto_tarefa:
        adicionar_tarefa(texto_tarefa)
    return redirect("/")


@app.route("/completar/<int:tarefa_id>")
def completo(tarefa_id):
    """Marca a tarefa como concluída e redireciona para a página principal."""
    completar_tarefa(tarefa_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
