import json
import logging
import os

from fastapi import APIRouter
from fastapi import Response
import sys
from datetime import datetime
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from routes.converte_dados_json import convert_json_to_df
from google.cloud import storage
from google.cloud import bigquery



logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(funcName)s:%(message)s")


router = APIRouter()
qt_rows = 0

@router.get("/importacao_vinhos_mesa")
def importacao_vinhos_mesa_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/importacao/vinhos_mesa/dados_opt_05_Importação_subopt_01.csv"
        client = storage.Client()
        client = bigquery.Client.from_service_account_json(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\credentials.json')
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_importacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_importacao_eventos)
        if response_emprapa_importacao_eventos:
                return Response(
                    content=response_emprapa_importacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )
    
@router.get("/importacao_espumantes")
def importacao_espumantes_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/importacao/espumantes/dados_opt_05_Importação_subopt_02.csv"
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_importacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_importacao_eventos)
        if response_emprapa_importacao_eventos:
                return Response(
                    content=response_emprapa_importacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )


@router.get("/importacao_uvas_frescas")
def importacao_uvas_frescas_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/importacao/uvas_frescas/dados_opt_05_Importação_subopt_03.csv"
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_importacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_importacao_eventos)
        if response_emprapa_importacao_eventos:
                return Response(
                    content=response_emprapa_importacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )
    
@router.get("/importacao_uvas_passas")
def importacao_uvas_passas_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/importacao/uvas_passas/dados_opt_05_Importação_subopt_04.csv"
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_importacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_importacao_eventos)
        if response_emprapa_importacao_eventos:
                return Response(
                    content=response_emprapa_importacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )

@router.get("/importacao_suco_uva")
def importacao_suco_uva_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/importacao/suco_uva/dados_opt_05_Importação_subopt_05.csv"
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_importacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_importacao_eventos)
        if response_emprapa_importacao_eventos:
                return Response(
                    content=response_emprapa_importacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )