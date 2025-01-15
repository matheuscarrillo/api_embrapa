# from google.cloud import secretmanager


# def get_secret(project_id, secret_id, version_id="latest"):
#     """
#     Busca um secret do Google Secret Manager.

#     Args:
#         project_id (str): ID do projeto do Google Cloud.
#         secret_id (str): ID do secret no Secret Manager.
#         version_id (str): Versão do secret (padrão: "latest").

#     Returns:
#         str: Valor do secret.
#     """

#     # Cria o cliente com as credenciais
#     client = secretmanager.SecretManagerServiceClient()

#     # Forma o nome do recurso
#     # secret_name = "projects/791475264704/secrets/embrapa-api-password/versions/latest"
#     secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

#     # Acessa o payload do secret
#     response = client.access_secret_version(name=secret_name)
#     secret_payload = response.payload.data.decode("UTF-8")

#     return secret_payload