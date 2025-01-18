from utils.utils import *
import yaml
import logging
import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(funcName)s:%(message)s")


logging.info('Realizando leitura de arquivo de configuração')
config = yaml.safe_load(open(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\src\python\transformacao\config.yaml', 'rb'))

for key, value in config.items():

    logging.info(f'inicializando variaveis {key}')
    caminho = value.get('caminho')
    caminho_p_storage = value.get('caminho_p_storage')
    tipo = value.get('tipo')
    ids = value.get('ids')
    ids_pivot = value.get('ids_pivot')
    var_name = value.get('var_name')
    var_name_pivot = value.get('var_name_pivot')
    value_name = value.get('value_name')
    col_cat = value.get('col_cat')
    ids_pivot = value.get('ids_pivot')
    var_name_pivot = value.get('var_name_pivot')

    
    for i in range(0, len(tipo)):
        logging.info(f'Processando arquivo {tipo[i]}')
        caminho_final = value.get('caminho_final')+'\\'+caminho[i].split('\\')[-1]
        
        destination_blob_name = caminho_p_storage[i].replace('gs://embrapa_api/', '')

        if tipo[i].split('_')[0] in ['importacao', 'exportacao']:
            logging.info('Rodando fluxo de importacao e exportacao')
            processamento = Processing(caminho[i], caminho_final, tipo[i], ids, ids_pivot, var_name, var_name_pivot, value_name, col_cat)
            X = processamento.melt_data()
            X = processamento.pivot_data(X)
            X = processamento.ajust_columns(X)
            X = processamento.generate_data(X)

            uploadtable = UploadTable(source_file_path=caminho_final, destination_blob_name=destination_blob_name, table_id=tipo[i], gcs_uri=caminho_p_storage[i])
            uploadtable = uploadtable.upload_file_and_load_csv_bigquery()
            if uploadtable:
                logging.info('Tabela ingerida no BigQuery')
            else:
                logging.info('Tabela não ingerida no BigQuery')

        else:
            logging.info('Rodando fluxo de produção, processamento e comercializacao')
            processamento = Processing(caminho[i], caminho_final, tipo[i], ids, ids_pivot, var_name, var_name_pivot, value_name, col_cat)
            X = processamento.melt_data()
            X = processamento.create_features(X)
            X = processamento.ajust_columns(X)
            X = processamento.generate_data(X)
            
            uploadtable = UploadTable(source_file_path=caminho_final, destination_blob_name=destination_blob_name, table_id=tipo[i], gcs_uri=caminho_p_storage[i])
            uploadtable = uploadtable.upload_file_and_load_csv_bigquery()
            if uploadtable:
                logging.info('Tabela ingerida no BigQuery')
            else:
                logging.info('Tabela não ingerida no BigQuery')
        


logging.info('Processamento finalizado')




