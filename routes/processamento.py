import json
import logging
import os

from fastapi import APIRouter
from fastapi import Response, Query
import sys
from datetime import datetime
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from google.cloud import bigquery
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(funcName)s:%(message)s")


router = APIRouter()

@router.get("/processamento_viniferas")
def processamento_viniferas(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    categoria_principal: str = Query(None, description="Tipo Uva")) -> Response:

    try:

        client = bigquery.Client()
        # client = bigquery.Client.from_service_account_json(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\credentials.json')

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.processamento_viniferas`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if categoria_principal:
            filters.append(f"lower(tipo_uva) = lower('{categoria_principal}')")

        # Adicionar cláusula WHERE apenas se houver filtros
        if filters:
            query += " WHERE " + " AND ".join(filters)

        # Executar a consulta
        query_job = client.query(query)
        results = [dict(row) for row in query_job]
        if not results:
            return JSONResponse(content={"Status": "No Data", "Msg": "Nenhum dado encontrado para os filtros fornecidos."}, headers={"Content-Type": "application/json"}, status_code=404)
        json_data = jsonable_encoder(results)

        return JSONResponse(content=json_data, headers={"Content-Type": "application/json"})
       
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )

@router.get("/processamento_americanas_e_hibridas")
def processamento_americanas_e_hibridas(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    categoria_principal: str = Query(None, description="Tipo Uva")) -> Response:

    try:

        client = bigquery.Client()
        # client = bigquery.Client.from_service_account_json(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\credentials.json')

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.processamento_americanas_e_hibridas`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if categoria_principal:
            filters.append(f"lower(tipo_uva) = lower('{categoria_principal}')")

        # Adicionar cláusula WHERE apenas se houver filtros
        if filters:
            query += " WHERE " + " AND ".join(filters)

        # Executar a consulta
        query_job = client.query(query)
        results = [dict(row) for row in query_job]
        if not results:
            return JSONResponse(content={"Status": "No Data", "Msg": "Nenhum dado encontrado para os filtros fornecidos."}, headers={"Content-Type": "application/json"}, status_code=404)
        json_data = jsonable_encoder(results)

        return JSONResponse(content=json_data, headers={"Content-Type": "application/json"})
       
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )


@router.get("/processamento_sem_classificacao")
def producao_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    categoria_principal: str = Query(None, description="Tipo Uva")) -> Response:

    try:

        client = bigquery.Client()
        # client = bigquery.Client.from_service_account_json(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\credentials.json')

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.processamento_sem_classificacao`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if categoria_principal:
            filters.append(f"lower(tipo_uva) = lower('{categoria_principal}')")

        # Adicionar cláusula WHERE apenas se houver filtros
        if filters:
            query += " WHERE " + " AND ".join(filters)

        # Executar a consulta
        query_job = client.query(query)
        results = [dict(row) for row in query_job]
        if not results:
            return JSONResponse(content={"Status": "No Data", "Msg": "Nenhum dado encontrado para os filtros fornecidos."}, headers={"Content-Type": "application/json"}, status_code=404)
        json_data = jsonable_encoder(results)

        return JSONResponse(content=json_data, headers={"Content-Type": "application/json"})
       
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )
    

@router.get("/processamento_uvas_de_mesa")
def producao_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    categoria_principal: str = Query(None, description="Tipo Uva")) -> Response:

    try:

        client = bigquery.Client()
       # client = bigquery.Client.from_service_account_json(r'C:\Users\mathe\OneDrive\Área de Trabalho\POS_TECH\api_embrapa\credentials.json')

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.processamento_uvas_de_mesa`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if categoria_principal:
            filters.append(f"lower(tipo_uva) = lower('{categoria_principal}')")

        # Adicionar cláusula WHERE apenas se houver filtros
        if filters:
            query += " WHERE " + " AND ".join(filters)

        # Executar a consulta
        query_job = client.query(query)
        results = [dict(row) for row in query_job]
        if not results:
            return JSONResponse(content={"Status": "No Data", "Msg": "Nenhum dado encontrado para os filtros fornecidos."}, headers={"Content-Type": "application/json"}, status_code=404)
        json_data = jsonable_encoder(results)

        return JSONResponse(content=json_data, headers={"Content-Type": "application/json"})
       
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )


