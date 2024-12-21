import json
import logging
import os

from datetime import datetime
from fastapi import APIRouter
from fastapi import Response
import sys
from datetime import datetime
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from routes.converte_dados_json import convert_json_to_df
from fastapi.responses import JSONResponse


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(funcName)s:%(message)s")


router = APIRouter()
qt_rows = 0


@router.get("/producao")
def producao_eventos() -> Response:

    try:
        filename = "dados_opt_02_Producao"
        logging.info(f"Coletando dados do arquivo {filename}.csv")
        path = f"C:\\Users\\thais.r.carvalho\\Documents\\Pos Machine Learning\\api_embrapa\\download\\{filename}.csv"
        criado_em = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_carga = datetime.now().strftime("%Y-%m-%d")
        response_emprapa_producao_eventos = convert_json_to_df(filename, path)
        logging.info(f"Arquivo {filename}.csv coletado com sucesso")
        logging.info(response_emprapa_producao_eventos)
        if response_emprapa_producao_eventos:
                return JSONResponse(
                    content=response_emprapa_producao_eventos,
                    status_code=200,
                    media_type="application/json",
                )
    except Exception as ex:
        return Response(
            content=json.dumps({"Status": "Error", "Msg": str(ex)}), status_code=500, media_type="application/json"
        )