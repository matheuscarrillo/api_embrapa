import pandas as pd

# Carregar o arquivo CSV (ajuste o caminho para o seu arquivo)
df = pd.read_csv("C:/Users/thais.r.carvalho/Documents/Pos Machine Learning/dados_opt_04_Comercialização.csv", sep=";")
# Exibir as primeiras linhas e colunas para diagnóstico
# print("Colunas do DataFrame:", df.columns)
if 'produto' in df.columns:
    df.rename(columns={'produto': 'Produto'}, inplace=True)
# Transformar o DataFrame para formato "long" (uma linha por produto e ano)
df_long = df.melt(id_vars=["id", "control", "Produto"], 
                  var_name="Ano", 
                  value_name="Quantidade")

# Adicionar a coluna "Categoria Principal" com base na coluna "control"
def categorizar_categoria(control):
    if "VINHO DE MESA" in control:
        return "Vinho de Mesa"
    elif "VINHO FINO DE MESA" in control:
        return "Vinho Fino de Mesa"
    elif "SUCO" in control:
        return "Suco"
    elif "DERIVADOS" in control:
        return "Derivados"
    else:
        return "Outros"
    
df_long['control'].fillna('valor_padrao', inplace=True)
df_long["Categoria Principal"] = df_long["control"].apply(categorizar_categoria)

# # Adicionar a coluna "Tipo de Vinho" com base na coluna "produto"
# def categorizar_tipo(produto):
#     if "Tinto" in produto:
#         return "Tinto"
#     elif "Branco" in produto:
#         return "Branco"
#     elif "Rosado" in produto:
#         return "Rosado"
#     elif "Espumante" in produto:
#         return "Espumante"
#     elif "Suco" in produto:
#         return "Suco"
#     elif "Mosto" in produto:
#         return "Mosto"
#     else:
#         return "Outros"

# df_long["Tipo de Vinho"] = df_long["produto"].apply(categorizar_tipo)

# Reorganizar colunas para facilitar a leitura
df_final = df_long[["Ano", "Categoria Principal", "Produto", "Quantidade"]]

# Salvar o resultado em um novo arquivo CSV
df_final.to_csv("C:/Users/thais.r.carvalho/Downloads/dados_opt_04_Comercialização.csv", index=False, sep=";")

# Exibir as primeiras linhas do resultado
print(df_final.head())