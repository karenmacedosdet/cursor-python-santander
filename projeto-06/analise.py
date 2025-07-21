"""
Análise de vendas: imprime tabela de vendas por mês,
principais produtos e exibe gráficos.
"""

import os
import base64
import pandas as pd
import matplotlib.pyplot as plt


def carregar_dados():
    """1. Carregar dados CSV (preço em reais - R$)"""
    return pd.read_csv(
        os.path.join(os.path.dirname(__file__), "vendas.csv"),
        encoding="utf-8",
    )


def calcular_vendas_por_mes(df_val):
    """2. Calcular o total de vendas por mês"""
    df_val["data"] = pd.to_datetime(df_val["data"])
    df_val["mes"] = df_val["data"].dt.strftime("%m-%y")  # mes-aa
    df_val["Valor"] = df_val["quantidade"] * df_val["preco"]  # Valor em R$
    return df_val, df_val.groupby("mes")["Valor"].sum().astype(float)


def principais_produtos(df_val):
    """3. Principais produtos em unidades e receitas"""
    df_val["receita"] = (
        df_val["quantidade"] * df_val["preco"]
    )  # Receita em R$
    vendas_prod_val = df_val.groupby("produto").agg(
        {"quantidade": "sum", "receita": "sum"}
    )
    mais_vendido_nome = vendas_prod_val["quantidade"].idxmax()
    maior_receita_nome = vendas_prod_val["receita"].idxmax()
    return vendas_prod_val, mais_vendido_nome, maior_receita_nome


def gerar_grafico_vendas_por_mes(vendas_por_mes_val):
    """4. Gráfico de vendas por mês"""
    grafico1_path = os.path.join(
        os.path.dirname(__file__), "vendas_por_mes.png"
    )
    vendas_por_mes_val.index = vendas_por_mes_val.index.astype(str)
    plt.figure(figsize=(6, 4))
    vendas_por_mes_val.plot(kind="bar")
    plt.title("Vendas por mês")
    plt.xlabel("Mês")
    plt.ylabel("Vendas (R$)")
    plt.tight_layout()
    plt.savefig(grafico1_path)
    plt.show()
    plt.close()

    # Converter imagem para base64
    with open(grafico1_path, "rb") as file_obj:
        grafico1_b64_val = base64.b64encode(file_obj.read()).decode(
            "utf-8"
        )
    return grafico1_b64_val


def gerar_grafico_top_produtos(vendas_prod_val):
    """5. Gráfico dos 5 principais produtos por receita"""
    grafico2_path = os.path.join(
        os.path.dirname(__file__), "top5_produtos.png"
    )
    top5_produtos_val = vendas_prod_val.nlargest(5, "receita")
    print("Top 5 produtos por receita):")
    print(top5_produtos_val["receita"].apply(lambda x: f"{x:.2f}"))
    print()
    plt.figure(figsize=(6, 4))
    plt.bar(top5_produtos_val.index, top5_produtos_val["receita"])
    plt.title("Os 5 principais produtos por receita")
    plt.ylabel("Receita (R$)")
    plt.xlabel("Produto")
    plt.tight_layout()
    plt.savefig(grafico2_path)
    plt.show()
    plt.close()

    # Converter imagem para base64
    with open(grafico2_path, "rb") as file_obj:
        grafico2_b64_val = base64.b64encode(file_obj.read()).decode(
            "utf-8"
        )
    return grafico2_b64_val, top5_produtos_val


def gerar_relatorio(
    vendas_por_mes_val,
    vendas_prod_val,
    mais_vendido_nome,
    maior_receita_nome,
    grafico1_b64_val,
    grafico2_b64_val,
    top5_produtos_val,
):
    """Monta o conteúdo HTML do relatório"""
    destaques = (
        f"<p>Produto mais vendido em unidades: <b>{mais_vendido_nome}</b> "
        f"(total {vendas_prod_val.loc[mais_vendido_nome, 'quantidade']})</p>"
        f"<p>Produto com maior receita: <b>{maior_receita_nome}</b> "
        f"(total R$ "
        f"{vendas_prod_val.loc[maior_receita_nome, 'receita']:.2f})</p>"
    )
    top5_html = "<ul>"
    for produto, receita in top5_produtos_val["receita"].items():
        top5_html += f"<li>{produto}: R$ {receita:.2f}</li>"
    top5_html += "</ul>"
    html_report_str = f"""
<html>
<head><meta charset='utf-8'><title>Relatório de Vendas</title></head>
<body>
<h1>Relatório de Vendas</h1>
<h2>Tabela de vendas por mês</h2>
<pre>{vendas_por_mes_val.apply(lambda x: f'R$ {x:.2f}').to_string()}</pre>
<h2>Principais produtos</h2>
{destaques}
<h2>Gráfico de vendas por mês</h2>
<img src='data:image/png;base64,{grafico1_b64_val}'
     alt='Vendas por mês'/>
<h2>Top 5 produtos por receita</h2>
{top5_html}
<img src='data:image/png;base64,{grafico2_b64_val}'
     alt='Top 5 produtos por receita'/>
</body>
</html>
"""
    return html_report_str


# Exemplo de uso:
df = carregar_dados()
df, vendas_por_mes = calcular_vendas_por_mes(df)
vendas_prod, mais_vendido, maior_receita = principais_produtos(df)
grafico1_b64 = gerar_grafico_vendas_por_mes(vendas_por_mes)
grafico2_b64, top5_produtos = gerar_grafico_top_produtos(vendas_prod)
html_report = gerar_relatorio(
    vendas_por_mes,
    vendas_prod,
    mais_vendido,
    maior_receita,
    grafico1_b64,
    grafico2_b64,
    top5_produtos,
)

with open(
    os.path.join(os.path.dirname(__file__), "report.html"),
    "w",
    encoding="utf-8",
) as out_file:
    out_file.write(html_report)
print("Relatório gerado em report.html")
