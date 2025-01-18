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

@router.get("/producao")
def producao_eventos(
    ano: int = Query(None, description="Filtrar pelo ano de exportação (1970 a 2023)"),
    categoria_principal: str = Query(None, description="Categoria Principal"),
    current_user: dict = Depends(get_current_user)) -> Response:

    try:

        client = bigquery.Client()

        query = """
            SELECT * FROM `river-handbook-446101-a0.embrapa.producao`
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
            content=json.dumps({"Status": "Error", "Msg": str(ex), "User": current_user}), status_code=500, media_type="application/json"
        )