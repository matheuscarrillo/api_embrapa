# Extração de Dados do Sistema Embrapa

Este script automatiza a extração e organização de dados do sistema **VitiBrasil** da Embrapa, utilizando o Selenium para realizar downloads e renomear arquivos de acordo com critérios definidos. 

## Requisitos

Certifique-se de que os seguintes pré-requisitos estão instalados:

1. **Python 3.x**
2. **Google Chrome** e **ChromeDriver** compatíveis com sua versão do navegador.
3. Bibliotecas Python:
   - `selenium`
   - `numpy`
   - `tqdm`

## Configuração do Ambiente

1. Instale as bibliotecas necessárias com:
   ```bash
   pip install selenium numpy tqdm
2. Altere o caminho do diretório de download na variável download_dir para refletir o local desejado no seu sistema:
python
   ```bash
   download_dir = r"C:\Users\SEU_USUARIO\Caminho\Para\Diretorio\Download"
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
