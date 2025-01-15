from datetime import datetime, timedelta
from typing import Union
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Carregar variáveis de ambiente


project_id = "river-handbook-446101-a0"
secret_id = "embrapa-api-password"

from google.cloud import secretmanager


def get_secret(project_id, secret_id, version_id="latest"):
    """
    Busca um secret do Google Secret Manager.

    Args:
        project_id (str): ID do projeto do Google Cloud.
        secret_id (str): ID do secret no Secret Manager.
        version_id (str): Versão do secret (padrão: "latest").

    Returns:
        str: Valor do secret.
    """

    # Cria o cliente com as credenciais
    client = secretmanager.SecretManagerServiceClient()

    # Forma o nome do recurso
    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Acessa o payload do secret
    response = client.access_secret_version(name=secret_name)
    secret_payload = response.payload.data.decode("UTF-8")

    return secret_payload

SECRET_KEY = "b1ef9b3950bf58f79e00b9c09d9520cf3c13ddce9472732587e12261972e17fd"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração para hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 esquema para extrair token do cabeçalho Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para validar o token JWT
# secret_value = get_secret(project_id, secret_id)
fake_users_db = {
    "user1": {"username": "user1", "hashed_password": pwd_context.hash("password1")}
}

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica a senha fornecida com a senha hashada."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Gera um hash para a senha fornecida."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """Gera um token JWT."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    """Decodifica e valida o token JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")


def get_user(username: str):
    teste = fake_users_db.get(username)
    print(teste)
    return fake_users_db.get(username)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = get_user(username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
# import os
# import sys
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# from auth import create_access_token, get_user, verify_password

router = APIRouter()


@router.post("/token", response_model=dict)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Rota de login para obter o token JWT."""
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário ou senha incorretos",
        )
    # Cria o token JWT
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

