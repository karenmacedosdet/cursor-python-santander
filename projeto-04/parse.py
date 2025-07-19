"""Script para ler o arquivo dados.csv usando pandas e calcular
estatísticas simples.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV com encoding explícito
df = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "dados.csv"), encoding="utf-8"
)

# Calcula as estatísticas
media = df.mean(numeric_only=True)
mediana = df.median(numeric_only=True)
desvio_padrao = df.std(numeric_only=True)

print("Média:\n", media)
print("\nMediana:\n", mediana)
print("\nDesvio padrão:\n", desvio_padrao)

# Gráfico de dispersão de coluna1 vs. coluna2
plt.scatter(df["coluna1"], df["coluna2"])
plt.xlabel("coluna1")
plt.ylabel("coluna2")
plt.title("Dispersão: coluna1 vs. coluna2")
plt.show()
