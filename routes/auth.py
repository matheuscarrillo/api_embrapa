from datetime import datetime, timedelta
from typing import Union
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from secret_manager import get_secret

# Carregar variáveis de ambiente


project_id = "river-handbook-446101-a0"
secret_id = "embrapa-api-password"

SECRET_KEY = get_secret(project_id, secret_id)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração para hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 esquema para extrair token do cabeçalho Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para validar o token JWT

fake_users_db = {
    "user1": {"username": "user1"}
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
