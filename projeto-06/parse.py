"""
Análise de vendas: carrega dados, calcula totais,
identifica produtos destaque e gera gráficos.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def carregar_dados():
    """1. Carregar dados CSV"""
    return pd.read_csv(
        os.path.join(os.path.dirname(__file__), "vendas.csv"),
        encoding="utf-8",
    )


def calcular_vendas_por_mes(df_parse):
    """2. Calcular o total de vendas por mês"""
    df_parse["data"] = pd.to_datetime(df_parse["data"])
    df_parse["mes"] = df_parse["data"].dt.to_period("M")
    df_parse["Valor"] = df_parse["quantidade"] * df_parse["preco"]
    vendas_por_mes_parse = df_parse.groupby("mes")["Valor"].sum()
    print("Vendas por mês:")
    print(vendas_por_mes_parse)
    print()
    return df_parse, vendas_por_mes_parse


def principais_produtos(df_parse):
    """3. Determinar o produto mais vendido e de maior receita"""
    df_parse["receita"] = df_parse["quantidade"] * df_parse["preco"]
    vendas_prod_parse = df_parse.groupby("produto").agg(
        {"quantidade": "sum", "receita": "sum"}
    )
    mais_vendido = vendas_prod_parse["quantidade"].idxmax()
    maior_receita = vendas_prod_parse["receita"].idxmax()
    print(
        f"Produto mais vendido em unidades: {mais_vendido} "
        f"(total {vendas_prod_parse.loc[mais_vendido, 'quantidade']})"
    )
    print(
        f"Produto com maior receita: {maior_receita} "
        f"(total {vendas_prod_parse.loc[maior_receita, 'receita']:.2f} €)"
    )
    print()
    return vendas_prod_parse


def grafico_vendas_por_mes(vendas_por_mes_parse):
    """4. Gráfico de vendas por mês"""
    vendas_por_mes_parse.plot(kind="bar")
    plt.title("Total de Vendas por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.show()


def grafico_top_produtos(df_parse):
    """5. Gráfico dos 5 principais produtos por receita"""
    top5_produtos_parse = (
        df_parse.groupby("produto")["Valor"].sum().nlargest(5)
    )
    print("Top 5 produtos por receita:")
    print(top5_produtos_parse)
    print()
    top5_produtos_parse.plot(kind="bar")
    plt.title("Top 5 Produtos por Receita")
    plt.xlabel("Produto")
    plt.ylabel("Receita")
    plt.tight_layout()
    plt.show()


# Execução
df_parse = carregar_dados()
df_parse, vendas_por_mes_parse = calcular_vendas_por_mes(df_parse)
vendas_prod_parse = principais_produtos(df_parse)
grafico_vendas_por_mes(vendas_por_mes_parse)
grafico_top_produtos(df_parse)
