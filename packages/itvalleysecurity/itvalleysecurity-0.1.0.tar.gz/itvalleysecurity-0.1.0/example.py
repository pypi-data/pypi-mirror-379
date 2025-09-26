'''
Exemplo de uso do ITValleySecurity SDK com FastAPI
'''
from fastapi import FastAPI, Response, HTTPException, status, Depends
from itvalleysecurity.fastapi import login_response, require_access
from itvalleysecurity.fastapi.payloads import LoginPayloadWithPassword

# --- Funções de Exemplo (substitua pela sua lógica) ---

# Simula um banco de dados de usuários
FAKE_USERS_DB = {
    "user@example.com": {
        "id": "user@example.com",
        "email": "user@example.com",
        "password_hash": "$2b$12$E8.B3c5h9.B3c5h9.B3c5u.B3c5h9.B3c5h9.B3c5h9.B3c5h9.B3", # Exemplo de hash
        "status": "active",
    }
}

def get_user_from_db(sub: str):
    return FAKE_USERS_DB.get(sub)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Em um projeto real, use uma biblioteca como passlib
    # return pwd_context.verify(plain_password, hashed_password)
    return True # Simulação

# --- Aplicação FastAPI ---

app = FastAPI(title="ITValleySecurity Example", version="0.2.0")

@app.post("/login")
def login(body: LoginPayloadWithPassword, resp: Response):
    '''
    Endpoint de login que valida credenciais e emite tokens.
    '''
    # 1) Buscar usuário no banco
    user = get_user_from_db(body.sub)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário ou senha inválidos")

    # 2) Validar senha
    if not verify_password(body.password, user["password_hash"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário ou senha inválidos")

    # 3) Regras extras (usuário ativo, etc.)
    if user["status"] != "active":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuário inativo")

    # 4) Emitir tokens
    return login_response(
        resp,
        sub=user["id"],
        email=user["email"],
        set_cookies=True
    )

@app.get("/chat")
def chat(user = Depends(require_access)):
    '''Rota protegida que retorna informações do usuário autenticado.'''
    return {"hello": user["sub"]}

@app.get("/dashboard")
def dashboard(user = Depends(require_access)):
    '''Dashboard do usuário autenticado.'''
    return {"owner": user["sub"]}

if __name__ == "__main__":
    import uvicorn
    print("Para testar, execute: uvicorn example:app --reload")
    print("Acesse a documentação interativa em http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)

