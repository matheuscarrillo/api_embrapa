import pandas as pd

# Carregar o arquivo CSV (ajuste o caminho para o seu arquivo)
df = pd.read_csv("C:/Users/thais.r.carvalho/Documents/Pos Machine Learning/dados_opt_03_Processamento_subopt_01.csv", sep=";")
# Exibir as primeiras linhas e colunas para diagnóstico
# print("Colunas do DataFrame:", df.columns)
# Transformar o DataFrame para formato "long" (uma linha por produto e ano)
df_long = df.melt(id_vars=["id", "control", "cultivar"], 
                  var_name="Ano", 
                  value_name="Quantidade")

# Adicionar a coluna "Categoria Principal" com base na coluna "control"
def categorizar_categoria(control):
    if "TINTAS" in control:
        return "Tintas"
    elif "BRANCAS E ROSADAS" in control:
        return "Brancas e Rosadas"
    elif "BRANCAS" in control:
        return "Brancas"
    elif "DERIVADOS" in control:
        return "Derivados"
    else:
        return "Outros"
    
df_long['control'].fillna('valor_padrao', inplace=True)
df_long["Tipo Uva"] = df_long["control"].apply(categorizar_categoria)


# Reorganizar colunas para facilitar a leitura
df_final = df_long[["Ano", "Tipo Uva", "cultivar", "Quantidade"]]

# Salvar o resultado em um novo arquivo CSV
df_final.to_csv("C:/Users/thais.r.carvalho/Downloads/dados_opt_03_Processamento_subopt_03.csv", index=False, sep=";")

# Exibir as primeiras linhas do resultado
print(df_final.head())