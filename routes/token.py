from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, get_user, verify_password

app = FastAPI()


@app.post("/token", response_model=dict)
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
