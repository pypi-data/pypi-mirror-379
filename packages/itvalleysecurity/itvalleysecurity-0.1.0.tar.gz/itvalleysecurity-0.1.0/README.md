'''
# ITValleySecurity – Documentação Rápida

Um SDK de autenticação JWT plug-and-play para APIs Python, projetado para ser **extremamente fácil de usar**. Funciona com Header Bearer ou Cookie HttpOnly, sem que você precise escrever a lógica de JWT.

O SDK carrega automaticamente as configurações de um arquivo `.env`, então você **não precisa** chamar `load_dotenv()` no seu código.

## 1. Instalação

Instalação super simples - tudo incluído:

```bash
pip install itvalleysecurity
```

Pronto! O FastAPI e todas as dependências já vêm junto automaticamente.

## 2. Configuração de Ambiente

Crie um arquivo `.env` na raiz do seu projeto. A única variável **obrigatória** é a `JWT_SECRET_KEY`.

```env
# OBRIGATÓRIO: Chave secreta com pelo menos 32 caracteres
JWT_SECRET_KEY=uma_chave_bem_grande_e_segura_com_mais_de_32_caracteres

# --- Opcionais (possuem valores padrão seguros) ---
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=15
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7
JWT_ISSUER=ITValley

# Origem do token: auto (padrão), bearer, ou cookie
EV_TOKEN_SOURCE=auto

# Política de validação do 'sub': any (padrão), email, ou uuid
EV_SUB_POLICY=any
```

> **Importante**: Se a `JWT_SECRET_KEY` não for definida, o SDK lançará um erro `ValueError` imediatamente para garantir que a aplicação não rode com uma configuração insegura.

## 3. Exemplo de Uso (FastAPI)

Este é um exemplo realista para um endpoint de login. O SDK cuida da emissão dos tokens e cookies; você só precisa focar na lógica de negócio (validar o usuário).

```python
from fastapi import FastAPI, Response, HTTPException, status, Depends
from itvalleysecurity.fastapi import login_response, require_access
from itvalleysecurity.fastapi.payloads import LoginPayloadWithPassword

# --- Lógica da sua aplicação (exemplo) ---

def get_user_from_db(username: str):
    # Implemente a busca do usuário no seu banco de dados
    pass

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Implemente a validação da senha (ex: com passlib)
    return True

# --- Aplicação FastAPI ---

app = FastAPI()

@app.post("/login")
def login(body: LoginPayloadWithPassword, resp: Response):
    # 1. Buscar usuário no banco
    user = get_user_from_db(body.sub)
    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha inválidos"
        )

    # 2. (Opcional) Validar regras de negócio
    if user.status != "active":
        raise HTTPException(status_code=403, detail="Usuário inativo")

    # 3. Emitir tokens (o SDK faz o resto)
    return login_response(
        resp,
        sub=user.id, # ou user.email
        email=user.email,
        set_cookies=True
    )

# Rota protegida: basta adicionar a dependência
@app.get("/profile")
def get_profile(current_user = Depends(require_access)):
    return {
        "message": f"Bem-vindo, {current_user['sub']}!",
        "user_details": current_user
    }

```

## 4. Funções do Core (Uso sem FastAPI)

Você também pode usar o núcleo do SDK para gerar e validar tokens em qualquer aplicação Python.

```python
from itvalleysecurity import issue_pair, verify_access

# Criar um par de tokens
pair = issue_pair(sub="user_id_123", email="user@example.com")
print("Access Token:", pair["access_token"])

# Validar um token de acesso
try:
    claims = verify_access(pair["access_token"])
    print("Token válido! Sub:", claims["sub"])
except InvalidToken as e:
    print("Token inválido:", e)
```

Com isso, a segurança da sua API se torna simples e robusta. Basta configurar o `.env` uma vez e usar `Depends(require_access)` nas suas rotas.
'''
