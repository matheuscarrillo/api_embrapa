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



logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(funcName)s:%(message)s")


router = APIRouter()
qt_rows = 0

@router.get("/exportacao_vinhos_mesa")
def exportacao_vinhos_mesa_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/exportacao/vinhos_mesa/dados_opt_06_Exportação_subopt_01.csv"
        client = storage.Client()
        # client = storage.Client.from_service_account_json('C:/Users/thais.r.carvalho/Downloads/credentials.json') 
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_exportacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_exportacao_eventos)
        if response_emprapa_exportacao_eventos:
                return Response(
                    content=response_emprapa_exportacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )
    
@router.get("/exportacao_espumantes")
def exportacao_espumantes_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/exportacao/espumantes/dados_opt_06_Exportação_subopt_02.csv"
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_exportacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_exportacao_eventos)
        if response_emprapa_exportacao_eventos:
                return Response(
                    content=response_emprapa_exportacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )

    
@router.get("/exportacao_uvas_frescas")
def exportacao_uvas_frescas_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/exportacao/uvas_frescas/dados_opt_06_Exportação_subopt_03.csv"
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_exportacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_exportacao_eventos)
        if response_emprapa_exportacao_eventos:
                return Response(
                    content=response_emprapa_exportacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )
    
@router.get("/exportacao_uvas_passas")
def exportacao_uvas_passas_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/exportacao/uvas_passas/dados_opt_06_Exportação_subopt_04.csv"
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_exportacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_exportacao_eventos)
        if response_emprapa_exportacao_eventos:
                return Response(
                    content=response_emprapa_exportacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )

@router.get("/exportacao_suco_uva")
def exportacao_suco_uva_eventos() -> Response:

    try:
        BUCKET_NAME = "embrapa_api"
        FILE_NAME = "raw/exportacao/suco_uva/dados_opt_06_Exportação_subopt_05.csv"
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        csv_content = blob.download_as_text()

        response_emprapa_exportacao_eventos = convert_json_to_df(csv_content)
        logging.info(f"Arquivo {FILE_NAME}.csv coletado com sucesso")
        logging.info(response_emprapa_exportacao_eventos)
        if response_emprapa_exportacao_eventos:
                return Response(
                    content=response_emprapa_exportacao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )