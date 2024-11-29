import os
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm

#definindo dicionários das páginas
dict_options = {
    'opt_02':'Producao',
    'opt_03':'Processamento',
    'opt_04':'Comercialização',
    'opt_05':'Importação',
    'opt_06':'Exportação'
}
dict_suboptions = {
    'opt_02':[],
    'opt_03':['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04'],
    'opt_04':[],
    'opt_05':['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04', 'subopt_05'],
    'opt_06':['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04']
}
dict_namecsv = {
    'opt_02':['Producao.csv'],
    'opt_03':['ProcessaViniferas.csv', 'ProcessaAmericanas.csv', 'ProcessaMesa.csv', 'ProcessaSemclass.csv'],
    'opt_04':['Comercio.csv'],
    'opt_05':['ImpVinhos.csv', 'ImpEspumantes.csv', 'ImpFrescas.csv', 'ImpPassas.csv', 'ImpSuco.csv'],
    'opt_06':['ExpVinho.csv', 'ExpEspumantes.csv', 'ExpUva.csv', 'ExpSuco.csv']
}

# Configuração do diretório de download e renomeação
download_dir = r"C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\first_app\cursofiap\download"  # Altere para o seu diretório desejado

# Função para configurar o WebDriver com um diretório de download específico
def configurar_driver(download_dir):
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    return webdriver.Chrome(options=chrome_options)

# Inicializando o WebDriver
driver = configurar_driver(download_dir)

np.absolute()

def download_rename_file(url_pagina, option, descricao, suboption, namecsv):
    """
    download_rename_file(url_pagina, option, descricao, suboption, namecsv)
    
    A função download_rename_file faz o download do arquivo baseando na url, parâmetros da url (option, descricao, suboption) 
    e renomeia o arquivo com o nome definido pela variável namecsv, para um nome baseado nos parâmetros da URL.
    
    Parameters
    ----------
    url_pagina: str 
        URL da página que deseja realizar o acesso.
    option: str 
        Parâmetro da URL que define a aba acessada.
    descricao: str 
        Descrição do parâmetro ```option```
    suboption: str 
        Parâmetro da URL que define o subitem da aba acessada.
    namecsv: str 
        Nome do arquivo CSV por padrão, definido pelo site da extração.

    Returns
    -------
    A função não retorna nenhum objeto, apenas executa as ações.
    """
    
    arquivo = namecsv
    url_download = f"http://vitibrasil.cnpuv.embrapa.br/download/{namecsv}"

    # Definindo nome do arquivo
    if suboption!='':
        novo_nome = f"dados_{option}_{descricao}_{suboption}.csv"
    else:
        novo_nome = f"dados_{option}_{descricao}.csv"
    
    # Acessar o URL
    driver.get(url_pagina)
    
    # Aguarda carregar a pagina
    time.sleep(0.8)  # Ajuste o tempo conforme necessário
    
    driver.get(url_download)
    
    # espera arquivo baixar
    contador = 0
    while arquivo not in os.listdir(download_dir) or contador<10:
        time.sleep(1)
        contador+=1
    time.sleep(2)   

    print('   Download realizado!')
    
    # Aguarda downlod
    if arquivo in os.listdir(download_dir):
        # Renomear o arquivo baixado
        caminho_antigo = os.path.join(download_dir, arquivo)
        caminho_novo = os.path.join(download_dir, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f"   Arquivo renomeado para: {novo_nome}")

for option, descricao in tqdm(dict_options.items()):
    print(f'Iniciando extracao dos dados de: {descricao}')
    list_suboptions = dict_suboptions.get(option)
    list_namecsv = dict_namecsv.get(option)
    
    # Define a URL para download
    if list_suboptions !=[]:
        for i in range(0, len(list_suboptions)):
            suboption = list_suboptions[i]
            namecsv = list_namecsv[i]
            print(f'  Extraindo dados da opcao: {suboption}')
            url_pagina = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={option}&subopcao={suboption}"
            # Chama a função para fazer o download do arquivo
            download_rename_file(url_pagina, option, descricao, suboption, namecsv)
    else:
        print(f'  Extraindo dados...')
        namecsv = list_namecsv[0]
        suboption = ''
        url_pagina = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={option}"
        download_rename_file(url_pagina, option, descricao, suboption, namecsv)

# Encerra o google Chrome
driver.quit()