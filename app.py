import json
import os

import uvicorn

from routes import auth
from fastapi import FastAPI
from fastapi import Response
from routes import producao
from routes import processamento
from routes import comercializacao
from routes import importacao
from routes import exportacao


app = FastAPI()

app.include_router(auth.router)
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(exportacao.router)
app.include_router(importacao.router)


@app.get("/")
async def root() -> Response:
    return Response(content=json.dumps({"Status": "OK"}), media_type="application/json", status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))