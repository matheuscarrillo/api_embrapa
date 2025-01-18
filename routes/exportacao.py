import json
import logging
from fastapi import APIRouter, Depends
from fastapi import Response, Query
from google.cloud import bigquery
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from routes.auth import get_current_user

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(funcName)s:%(message)s")

router = APIRouter()

@router.get("/exportacao_vinhos_mesa")
def exportacao_vinhos_mesa_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.exportacao_vinhos_mesa`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if pais:
            filters.append(f"lower(pais) = lower('{pais}')")

        # Adicionar cláusula WHERE apenas se houver filtros
        if filters:
            query += " WHERE " + " AND ".join(filters)

        try:
            query_job = client.query(query)
        except Exception as e:
            logging.info(e, '\n')
        results = [dict(row) for row in query_job]
        
        if not results:
            return JSONResponse(content={"Status": "No Data", "Msg": "Nenhum dado encontrado para os filtros fornecidos."}, headers={"Content-Type": "application/json"}, status_code=404)
        json_data = jsonable_encoder(results)

        return JSONResponse(content=json_data, headers={"Content-Type": "application/json"})
       
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex), "User": current_user}), status_code=500, media_type="application/json"
        )

@router.get("/exportacao_espumantes")
def exportacao_espumantes_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.exportacao_espumantes`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if pais:
            filters.append(f"lower(pais) = lower('{pais}')")

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


@router.get("/exportacao_uvas_frescas")
def exportacao_uvas_frescas_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.exportacao_uvas_frescas`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if pais:
            filters.append(f"lower(pais) = lower('{pais}')")

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
    

@router.get("/exportacao_suco_uva")
def exportacao_suco_uva_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()
        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.exportacao_suco_uva`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if pais:
            filters.append(f"lower(pais) = lower('{pais}')")

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