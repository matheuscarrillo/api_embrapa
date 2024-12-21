import os
import pandas as pd
import json


def convert_json_to_df(nome_arquivo, caminho_arquivo):
    caminho_arquivo = f"C:\\Users\\thais.r.carvalho\\Documents\\Pos Machine Learning\\api_embrapa\\download\\{nome_arquivo}.csv"

    df = pd.read_csv(caminho_arquivo, delimiter=';')

    dados_estruturados = []

    for index, row in df.iterrows():
        dados = row.to_dict()
        dados_estruturados.append(dados)

    retorno = (json.dumps(dados_estruturados, ensure_ascii=False, indent=4))
    # print(retorno)
    return retorno

# nome_arquivo = "dados_opt_02_Producao"
# caminho_arquivo_json = f"C:\\Users\\thais.r.carvalho\\Downloads\\{nome_arquivo}.json"
# caminho_arquivo = f"C:\\Users\\thais.r.carvalho\\Documents\\Pos Machine Learning\\api_embrapa\\download\\{nome_arquivo}.csv"

# df = pd.read_csv(caminho_arquivo, delimiter=';')

# dados_estruturados = []

# for index, row in df.iterrows():
#     dados = row.to_dict()
#     dados_estruturados.append(dados)

# print(json.dumps(dados_estruturados, ensure_ascii=False, indent=4))

# Salvar os dados JSON em um arquivo
# with open(caminho_arquivo_json, "w", encoding="utf-8") as json_file:
#     json.dump(dados_estruturados, json_file, ensure_ascii=False, indent=4)
#
# print(f"Arquivo JSON salvo em: {caminho_arquivo_json}")
