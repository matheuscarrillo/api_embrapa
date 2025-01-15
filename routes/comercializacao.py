import json
import logging
from fastapi import APIRouter, status, Depends
from fastapi import Response, Query
import sys
from datetime import datetime
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from google.cloud import bigquery
from routes.auth import get_current_user

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(funcName)s:%(message)s")


router = APIRouter()


@router.get("/comercializacao")
def comercializacao_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    categoria_principal: str = Query(None, description="Categoria Principal")) -> Response:

    try:

        client = bigquery.Client()
        # client = bigquery.Client.from_service_account_json('C:/Users/thais.r.carvalho/Downloads/credentials.json')

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.comercializacao`
        """
        filters = []

        if ano:
            filters.append(f"ano = {ano}")
        if categoria_principal:
            filters.append(f"lower(categoria_principal) = lower('{categoria_principal}')")

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