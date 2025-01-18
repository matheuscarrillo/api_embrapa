import json
import logging
from fastapi import APIRouter, Depends
from fastapi import Response, Query
from routes.auth import get_current_user

from google.cloud import bigquery
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(funcName)s:%(message)s")


router = APIRouter()

@router.get("/processamento_viniferas")
def processamento_viniferas_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    tipo_uva: str = Query(None, description="Tipo Uva"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.processamento_viniferas`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if tipo_uva:
            filters.append(f"lower(tipo_uva) = lower('{tipo_uva}')")

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
            content=json.dumps({"Status": "Error", "Msg": str(ex), "User": current_user}), status_code=500, media_type="application/json"
        )

@router.get("/processamento_americanas_e_hibridas")
def processamento_americanas_e_hibridas_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    tipo_uva: str = Query(None, description="Tipo Uva"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()
    
        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.processamento_americanas_e_hibridas`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if tipo_uva:
            filters.append(f"lower(tipo_uva) = lower('{tipo_uva}')")

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
            content=json.dumps({"Status": "Error", "Msg": str(ex), "User": current_user}), status_code=500, media_type="application/json"
        )


@router.get("/processamento_sem_classificacao")
def processamento_sem_classificacao_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    tipo_uva: str = Query(None, description="Tipo Uva"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.processamento_sem_classificacao`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if tipo_uva:
            filters.append(f"lower(tipo_uva) = lower('{tipo_uva}')")

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
            content=json.dumps({"Status": "Error", "Msg": str(ex), "User": current_user}), status_code=500, media_type="application/json"
        )
    

@router.get("/processamento_uvas_de_mesa")
def processamento_uvas_de_mesa_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    tipo_uva: str = Query(None, description="Tipo Uva"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()
 
        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.processamento_uvas_de_mesa`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if tipo_uva:
            filters.append(f"lower(tipo_uva) = lower('{tipo_uva}')")

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
            content=json.dumps({"Status": "Error", "Msg": str(ex), "User": current_user}), status_code=500, media_type="application/json"
        )


