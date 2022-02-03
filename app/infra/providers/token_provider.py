from datetime import datetime, timedelta
from jose     import jwt

SECRET_KEY     = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM      = 'HS256'
EXPIRES_IN_MIN = 3000

def create_access_token(data: dict):
    
    dados = data.copy()
    expirate = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    dados.update({'exp': expirate})

    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str):
    
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return payload.get('sub')


    