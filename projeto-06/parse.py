"""
Análise de vendas: carrega dados, calcula totais,
identifica produtos destaque e gera gráficos.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

"""1. Carregar dados CSV"""
df = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "vendas.csv"), encoding="utf-8"
)

"""2. Calcular o total de vendas por mês"""
df["Data"] = pd.to_datetime(df["Data"])
df["mes"] = df["Data"].dt.to_period("M")
df["Valor"] = df["quantidade"] * df["preco"]
vendas_por_mes = df.groupby("mes").apply(lambda d: d["Valor"].sum())
vendas_por_mes = vendas_por_mes.astype(float)
print("Vendas por mês:")
print(vendas_por_mes)
print()

"""3. Determinar o produto mais vendido e de maior receita"""
df["receita"] = df["quantidade"] * df["preco"]
vendas_prod = df.groupby("produto").agg(
    {"quantidade": "sum", "receita": "sum"}
)
mais_vendido = vendas_prod["quantidade"].idxmax()
maior_receita = vendas_prod["receita"].idxmax()
print(
    f"Produto mais vendido em unidades: {mais_vendido} "
    f"(total "
    f"{vendas_prod.loc[mais_vendido, 'quantidade']})"
)
print(
    f"Produto com maior receita: {maior_receita} "
    f"(total "
    f"{vendas_prod.loc[maior_receita, 'receita']:.2f} €)"
)
print()

"""4. Gráfico de vendas por mês"""
vendas_por_mes.plot(kind="bar")
plt.title("Total de Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Valor")
plt.tight_layout()
plt.show()

"""5. Gráfico dos 5 principais produtos por receita"""
top5_produtos = df.groupby("Produto")["Valor"].sum().nlargest(5)
print("Top 5 produtos por receita:")
print(top5_produtos)
print()
top5_produtos.plot(kind="bar")
plt.title("Top 5 Produtos por Receita")
plt.xlabel("Produto")
plt.ylabel("Receita")
plt.tight_layout()
plt.show()
