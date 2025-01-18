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

@router.get("/importacao_vinhos_mesa")
def importacao_vinhos_mesa_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.importacao_vinhos_mesa`
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

@router.get("/importacao_espumantes")
def importacao_espumantes_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.importacao_espumantes`
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


@router.get("/importacao_uvas_frescas")
def importacao_uvas_frescas_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.importacao_uvas_frescas`
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
    

@router.get("/importacao_uvas_passas")
def importacao_uvas_passas_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()
        
        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.importacao_uvas_passas`
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

@router.get("/importacao_suco_uva")
def importacao_suco_uva_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    pais: str = Query(None, description="País"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.importacao_suco_uva`
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


