import pandas as pd

# Carregar o arquivo CSV (ajuste o caminho para o seu arquivo)
df = pd.read_csv("C:/Users/thais.r.carvalho/Documents/Pos Machine Learning/dados_opt_06_Exportação_subopt_04.csv", sep=";")
# Exibir as primeiras linhas e colunas para diagnóstico
# print("Colunas do DataFrame:", df.columns)

df_melted = pd.melt(df, id_vars=["Id", "País"], var_name="Ano e Tipo", value_name="Valor")

# Separar a coluna "Ano e Tipo" em "Ano" e "Tipo" (Quantidade ou Valor)
df_melted[["Ano", "Tipo"]] = df_melted["Ano e Tipo"].str.extract(r"(\d+)(.*)")

# Pivotar os dados para criar colunas separadas de Quantidade e Valor
df_pivot = df_melted.pivot(index=["Id", "País", "Ano"], columns="Tipo", values="Valor").reset_index()

# Renomear as colunas
df_pivot.columns = ["Id", "País", "Ano", "Quantidade (Kg)", "Valor (US$)"]
df_pivot.to_csv("C:/Users/thais.r.carvalho/Downloads/dados_opt_06_Exportação_subopt_04.csv", sep=";", index=False)

print("Arquivo reestruturado salvo com sucesso!")
