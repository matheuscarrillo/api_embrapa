# API EMBRAPA

# Requisitos

Certifique-se de que os seguintes pré-requisitos estão instalados:

1. **Python 3.12**
2. **Google Chrome** e **ChromeDriver** compatíveis com sua versão do navegador.
3. Bibliotecas Python:
   - `requirements.txt`

# Extração de Dados do Sistema Embrapa

Este script automatiza a extração e organização de dados do sistema **VitiBrasil** da Embrapa, utilizando o Selenium para realizar downloads e renomear arquivos de acordo com critérios definidos. 

## Configuração do Ambiente

1. Instale as bibliotecas necessárias com:
   ```bash
   pip install selenium numpy tqdm
2. Altere o caminho do diretório de download na variável download_dir para refletir o local desejado no seu sistema:
python
   ```bash
   download_dir = r"C:\Users\SEU_USUARIO\Caminho\Para\Diretorio\Download"
   ```
## Descrição do Script
### 1. Dicionários de Configuração
Os dicionários dict_options, dict_suboptions e dict_namecsv definem as opções e subopções de extração, assim como os nomes dos arquivos CSV correspondentes.

### 2. Configuração do WebDriver
A função `configurar_driver` inicializa o Selenium WebDriver e configura o comportamento de download:

- Define o diretório de download.
- Desabilita prompts de confirmação para downloads.
- Garante segurança do navegador habilitada.
### 3. Função `download_rename_file`
Essa função executa o download dos arquivos e os renomeia com base nos parâmetros fornecidos:
- Navega até a página de download usando a URL formatada.
- Aguarda a conclusão do download.
- Renomeia o arquivo baixado para um nome estruturado, como `dados_{option}_{descricao}_{suboption}.csv`.
### 4. Extração de Dados
O script itera pelas opções definidas no dicionário `dict_options`:
- Para cada opção e subopção, constrói a URL da página de download.
- Chama a função `download_rename_file` para realizar o download e renomear o arquivo.
- Utiliza a biblioteca `tqdm` para exibir o progresso.
### 5. Encerramento
Após a conclusão de todas as extrações, o script finaliza o WebDriver com driver.quit().

## Como Executar
1. Execute o script diretamente com:

```bash
python extract_data_embrapa.py
```
2. Durante a execução, o progresso das etapas será exibido no terminal. Após a conclusão, os arquivos estarão no diretório configurado, com nomes padronizados.

## Estrutura do Arquivo
Os arquivos extraídos serão organizados de acordo com a estrutura de nomenclatura:

- Para opções sem subopções:
```bash
dados_{option}_{descricao}.csv
```
- Para opções com subopções:
```bash
dados_{option}_{descricao}_{suboption}.csv
```
Exemplo:
- `dados_opt_03_Processamento_subopt_02.csv`
## Observações
- Ajuste o tempo de espera (time.sleep) conforme necessário, dependendo da velocidade de sua conexão e do site.
- Certifique-se de que o diretório de download tem permissões adequadas para leitura e escrita.

## Solução de Problemas
1. Erro de compatibilidade com o ChromeDriver
- Baixe a versão correspondente do ChromeDriver para seu navegador em: ChromeDriver Downloads.

2. Arquivos não renomeados
3. - Verifique se o nome padrão do arquivo corresponde ao esperado (consulte `namecsv`).

# Processamento de Tabelas com Google Cloud

Este repositório contém scripts para processar dados tabulares e salvá-los no Google Cloud Storage e no BigQuery. O fluxo principal consiste em:

1. Leitura de arquivos de configuração `config.yaml`.
2. Processamento das tabelas de entrada usando classes e funções definidas no arquivo `utils.py`.
3. Upload dos arquivos processados para o Google Cloud Storage.
4. Criação ou sobrescrita de tabelas no BigQuery com os dados processados.

## Estrutura do Repositório

- **`transformers.py`**: Script principal para execução do pipeline de processamento.
- **`utils.py`**: Biblioteca de funções auxiliares e classes para manipulação e upload de dados.
- **`config.yaml`**: Arquivo de configuração contendo informações sobre os caminhos dos arquivos de entrada, saída e detalhes de processamento.

## Passo a Passo para Execução

### 1. Configuração do Ambiente

Certifique-se de que as dependências necessárias estão instaladas. Execute:

```bash
pip install -r requirements.txt
```

### 2. Estrutura do Arquivo de Configuração (`config.yaml`)

O arquivo `config.yaml` deve conter os detalhes de configuração no seguinte formato:

```yaml
nome_dataset:
  caminho: ["caminho/para/arquivo1.csv", "caminho/para/arquivo2.csv"]
  caminho_p_storage: ["gs://bucket/arquivo1.csv", "gs://bucket/arquivo2.csv"]
  tipo: ["importacao", "exportacao"]
  ids: ["coluna1", "coluna2"]
  ids_pivot: ["coluna_pivot1", "coluna_pivot2"]
  var_name: "variavel"
  var_name_pivot: "pivot_var"
  value_name: "valor"
  col_cat: "categoria"
```

### 3. Execução do Script Principal

Execute o script principal `transformers.py`:

```bash
python transformers.py
```

O script irá:
- Ler o arquivo `config.yaml`.
- Processar os dados utilizando classes do `utils.py`.
- Fazer upload para o Google Cloud Storage.
- Atualizar ou criar as tabelas no BigQuery.

### 4. Detalhes Técnicos

#### Processamento dos Dados
- Os dados são transformados com a função `melt_data`.
- Em seguida, dependendo do tipo, os dados são pivotados ou enriquecidos com novas features usando `pivot_data` ou `create_features`.
- Por fim, as colunas são ajustadas com nomes padronizados por `ajust_columns`, e os dados processados são salvos localmente.

#### Upload e Carga no BigQuery
- Os arquivos processados são enviados para o Google Cloud Storage pela classe `UploadTable`.
- A tabela correspondente é criada ou atualizada no BigQuery.

### 5. Testes

Para verificar a execução:
- Certifique-se de que o arquivo `credentials.json` para autenticação no Google Cloud está configurado corretamente.
- Execute o script com arquivos de exemplo configurados no `config.yaml`.
- Valide os resultados verificando:
  - Os arquivos no Google Cloud Storage.
  - A existência e os dados nas tabelas do BigQuery.

# API de Consulta de Dados com FastAPI e Google BigQuery

Este projeto implementa uma API utilizando **FastAPI** para consultar dados armazenados no Google BigQuery. A partir desses dados será possível construir um modelo preditivo para estimar tendências de produção e consumo de produtos vitivinícolas, permitindo suporte à decisão para produtores e comerciantes do setor.



## Arquitetura do Projeto

![Arquitetura Tech Challenge ARQUITETURA](https://github.com/user-attachments/assets/0bbc208c-3fa7-4f72-ab89-fe4294999f35)

1. Extração da fonte de dados do Embrapa. Para isso foi criado um script em python, usando biblioteca do selenium webdriver, que irá fazer o processo de webscrapping de cada uma das abas (Produção, Processamento, Comercialização, Importação e Exportação) e os arquivos gerados serão salvos em formato csv no ambiente local. 

2. Em seguida será executada a tarefa de realizar a transformação dos dados, de fazer o pivot das colunas de anos, se transformarem em linhas e também da retirada de espaço em brancos, após essa transformação os dados são salvos no Cloud Storage e em seguida fazemos a criação das tabelas no banco de dados BigQuery, sendo criada uma tabela para cada arquivo gerado no processo de extração dos dados. 

3. Para a disponibilização de consulta dos dados, foi criada uma API utilizando o framework FastAPI. Essa API permite que os usuários consultem os dados de maneira eficiente e estruturada. O FastAPI é uma ferramenta moderna e performática para a construção de APIs em Python, reconhecida pela sua simplicidade, validação automática de dados e integração com ferramentas de documentação interativa, como o Swagger. Essa api possui autenticação JWT(JSON Web Token). O JWT é um padrão de autenticação seguro e amplamente utilizado para verificar a identidade dos usuários. No processo:

   - i. O cliente envia suas credenciais (como nome de usuário e senha) para a API.
   - ii. Após validação, a API retorna um token JWT assinado.
   - iii. Este token é enviado pelo cliente em cada solicitação subsequente, permitindo à API verificar a identidade do usuário sem a necessidade de reenviar as credenciais.
   
   A API foi publicada no Google Cloud Run, um serviço gerenciado pelo Google Cloud que permite executar contêineres em escala. Isso significa que a API roda em um ambiente isolado e escalável, garantindo alta disponibilidade e desempenho. Além disso, possui custo eficiente, é cobrado apenas pelo tempo de execução da API e pela quantidade de recursos usados.

   As credenciais para autenticação da API foram salvas no Secret Manager e a imagem docker no repositório de Artifactory Registry.

4. Treinamento do Modelo: O Vertex AI utiliza os dados do BigQuery para treinar modelos de aprendizado de máquina. Esses modelos podem ser usados para prever tendências, identificar padrões ou tomar decisões automatizadas com base nos dados da Embrapa.

## Ideia de Arquitetura Futura

![Arquitetura Tech Challenge- 2 drawio](https://github.com/user-attachments/assets/11e82b51-3e16-444e-8719-a2f92d6189be)



## Estrutura do Projeto

- **`main.py`**: Configura a aplicação FastAPI e inclui as rotas definidas nos módulos correspondentes.
- **`routes/*.py`**: Implementa a rota `*` que permite consultas filtradas por ano e categoria principal.

## Códigos Utilizados para o Deploy da API
### 1. Criação da Imagem no Docker (Build)
```bash 
docker build -t gcr.io/river-handbook-446101-a0/api-embrapa-events:<version>
```

### 2. Salvar a imagem criada no Artifactory Registry (Repositório)
```bash 
docker push gcr.io/river-handbook-446101-a0/api-embrapa-events:<version>
```

### 3. Deploy da API via GCP Client
```bash
gcloud run deploy api-embrapa-events --image gcr.io/river-handbook-446101-a0/api-embrapa-events:<version> --platform managed --region us-central1 --allow-unauthenticated --set-secrets embrapa-api-password=embrapa-api-password:latest,secret-key-empbrapa-api=secret-key-empbrapa-api:latest
```

## Estrutura de Pastas da API

```plaintext
.
├── app.py
├── DockerFile
├── requirements.txt
└── routes/
    ├── auth.py
    ├── comercializacao.py
    ├── exportacao.py
    ├── importacao.py
    ├── processamento.py
    └── producao.py

```
## URL da API publicada

``` bash
https://api-embrapa-events-791475264704.us-central1.run.app/docs
```

Além da api poder ser testada via Swagger, é possível realizar requisições via Postman, Insomnia, por exemplo.
