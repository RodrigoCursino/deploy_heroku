from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session

from app.infra.sqlalchemy.repositories.user import UserRepository
from app.infra.sqlalchemy.config.database   import get_db
from app.schemas.schemas import User
from app.infra.providers.oauth_provider    import get_token_header

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post('', status_code=status.HTTP_201_CREATED, response_model=User)
def store(model: User, db: Session = Depends(get_db)):
    
    # verificar se o usuário já existe
    model = UserRepository.get_by_param('cellphone', model.cellphone)

    if model: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Já temos um usuário com esse celular cadastrado"
        )
    
    return UserRepository(db).store(model)

@router.get('')
def list_all(db: Session = Depends(get_db)):
    return UserRepository(db).list()

@router.get('/get')
def list_all(id:int, db: Session = Depends(get_db)):
    user = UserRepository(db).get(id)
    if not user:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User Not Found'
        )
    return user