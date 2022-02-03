from app.infra.sqlalchemy.repositories.user import UserRepository
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status
from app.infra.sqlalchemy.config.database import get_db
from app.infra.providers import token_provider
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_token_header(token: str = Depends(oauth2_schema),
                         session: Session = Depends(get_db)):
    
    # decodificar o token, pegar o telefone, buscar usuario no bd e retornar
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')

    try:
        cellphone = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not cellphone:
        raise exception

    user = UserRepository(session).get_by_param('cellphone',cellphone)

    if not user:
        raise exception

    return user