import pandas as pd
from unidecode import unidecode
from google.cloud import bigquery
from google.cloud import storage


def categorizar_categoria(control, tipo):
    if tipo.split('_')[0]=='processamento':
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
    
    if tipo=='comercializacao' or tipo=='producao':
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

class Processing:
    def __init__(self, caminho, caminho_final, tipo, ids, ids_pivot, var_name, var_name_pivot, value_name, col_cat):
        self.df = pd.read_csv(caminho, sep=";")
        if len(self.df.columns)<=1:
            self.df = pd.read_csv(caminho, sep="\t")
        
        self.caminho_final = caminho_final
        self.tipo = tipo
        self.ids = ids
        self.ids_pivot = ids_pivot
        self.var_name = var_name
        self.var_name_pivot = var_name_pivot
        self.value_name = value_name
        self.col_cat = col_cat
    
    def melt_data(self):
        if 'produto' in [x.lower() for x in self.df.columns]:
            self.df.rename(columns={'produto': 'Produto'}, inplace=True)
            self.col_prod = 'Produto'
        else:
            self.col_prod = "cultivar"

        
        df_long = self.df.melt(
                        id_vars=self.ids, 
                        var_name=self.var_name, 
                        value_name=self.value_name
                        )
        return df_long
    
    def pivot_data(self, df_melted):
        df_melted[["Ano", "Tipo"]] = df_melted["Ano e Tipo"].str.extract(r"(\d+)(.*)")
        df_pivot = df_melted.pivot(index=self.ids_pivot, columns=self.var_name_pivot, values="Valor").reset_index()
        df_pivot.columns = ["Id", "País", "Ano", "Quantidade (Kg)", "Valor (US$)"]
        
        return df_pivot

    
    def create_features(self, df_long):
        df_long['control'].fillna('valor_padrao', inplace=True)
        df_long[self.col_cat] = df_long["control"].apply(lambda row: categorizar_categoria(row, self.tipo))
        df_long = df_long[["Ano", self.col_cat, self.col_prod, "Quantidade"]]

        df_long[self.col_prod] = df_long[self.col_prod].str.strip()

        return df_long
    
    def ajust_columns(self, df_long):
        colunas = []
        for coluna in df_long.columns:
            colunas.append(unidecode(coluna.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('$', '')))
        
        df_long.columns = colunas

        return df_long
    
    def generate_data(self, df_long):
        df_long.to_csv(self.caminho_final, index=False, sep=";")




class UploadTable:
    def __init__(self, source_file_path, destination_blob_name, table_id, gcs_uri):
        
        self.bucket_name = "embrapa_api"
        self.project_id = "river-handbook-446101-a0"
        self.dataset_id = "embrapa"
        
        self.source_file_path = source_file_path
        self.destination_blob_name = destination_blob_name
        self.table_id = table_id
        self.gcs_uri = gcs_uri


    def load_csv_to_bigquery(self, project_id, dataset_id, table_id, gcs_uri):
        """
        Loads a CSV file from Google Cloud Storage into a BigQuery table.

        Args:
            project_id (str): Your Google Cloud project ID.
            dataset_id (str): The dataset ID in BigQuery where the table resides.
            table_id (str): The name of the table in BigQuery.
            gcs_uri (str): The URI of the CSV file in GCS (e.g., gs://bucket_name/file_name.csv).
        """
        # Initialize the BigQuery client
        client = bigquery.Client.from_service_account_json(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\credentials.json')

        # Specify the dataset and table
        table_ref = client.dataset(dataset_id).table(table_id)

        # Configure the load job
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,  # Skip the header row
            autodetect=True,      # Automatically infer schema
        )

        # Start the load job
        print(f"Starting job to load data from {gcs_uri} into {dataset_id}.{table_id}...")
        load_job = client.load_table_from_uri(
            gcs_uri, table_ref, job_config=job_config
        )

        # Wait for the load job to complete
        load_job.result()
        print(f"Data successfully loaded into {dataset_id}.{table_id}.")


    def upload_file_to_gcs(self):
        """
        Uploads a file to a specified Google Cloud Storage bucket.

        Args:
            bucket_name (str): The name of the bucket to upload to.
            source_file_path (str): The local path to the file to upload.
            destination_blob_name (str): The desired name of the file in the bucket.
        """
        # Initialize the Google Cloud Storage client
        storage_client = storage.Client.from_service_account_json(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\credentials.json')

        # Get the bucket
        bucket = storage_client.bucket(self.bucket_name)

        # Create a blob (file object) in the bucket
        blob = bucket.blob(self.destination_blob_name)

        # Upload the file to the bucket
        blob.upload_from_filename(self.source_file_path)

        print(f"File {self.source_file_path} uploaded to {self.destination_blob_name} in bucket {self.bucket_name}.")

        

    def load_csv_to_bigquery(self):
        """
        Loads a CSV file from Google Cloud Storage into a BigQuery table.

        Args:
            project_id (str): Your Google Cloud project ID.
            dataset_id (str): The dataset ID in BigQuery where the table resides.
            table_id (str): The name of the table in BigQuery.
            gcs_uri (str): The URI of the CSV file in GCS (e.g., gs://bucket_name/file_name.csv).
        """
        # Initialize the BigQuery client
        client = bigquery.Client.from_service_account_json(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\credentials.json')

        # Specify the dataset and table
        table_ref = client.dataset(self.dataset_id).table(self.table_id)

        
        # Check if the table exists by getting its metadata
        try:
            client.get_table(table_ref)
            print(f"Table {table_ref} exists.")
            # client.delete_table(table_ref)
            return True
        except:
            print(f"Table {table_ref} does not exist.")
            pass

        # Configure the load job
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,  # Skip the header row
            autodetect=True,      # Automatically infer schema
            field_delimiter=';'
        )

        # Start the load job
        print(f"Starting job to load data from {self.gcs_uri} into {self.dataset_id}.{self.table_id}...")
        load_job = client.load_table_from_uri(
            self.gcs_uri, table_ref, job_config=job_config
        )

        # Wait for the load job to complete
        load_job.result()
        print(f"Data successfully loaded into {self.dataset_id}.{self.table_id}.")

        return True

    def upload_file_and_load_csv_bigquery(self):
        # Replace these values with your bucket and file details
        
        # source_file_path = r"C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\download\processadas\dados_opt_03_Processamento_subopt_02.csv"
        # destination_blob_name = "raw/processamento/americanas_e_hibridas/dados_opt_03_Processamento_subopt_02.csv"

        # Replace with your project, dataset, table, and GCS file details
        
        # table_id = "processamento_americanas_e_hibridas"
        # gcs_uri = gcs_uri

        # Upload the file
        self.upload_file_to_gcs()
        uploadfile = self.load_csv_to_bigquery()

        return uploadfile

    
    


