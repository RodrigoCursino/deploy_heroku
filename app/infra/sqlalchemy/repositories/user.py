from app.schemas                        import schemas
from app.infra.sqlalchemy.models        import models
from sqlalchemy.orm                     import Session
from sqlalchemy.sql.expression          import select
from app.infra.providers                import hash_provider, token_provider
from fastapi                            import HTTPException, status

class UserRepository():
    
    def __init__(self, db: Session):
        self.db = db

    def list(self):
        return self.db.query(models.User).all()
    
    def get_by_param(self, param: str, value):
        return self.db.query(models.User).filter(getattr(models.User, param) == value).first()
    
    def get(self,id):
        #return self.db.query(models.User)\
        #        .join(models.RoleUser, models.RoleUser.id_user == models.User.id)\
        #            .join(models.Role, models.RoleUser.id_role == models.Role.id)\
        #                .filter(models.User.id == id)
       
        return self.db.query(models.User).filter(models.User.id == id).first()
        #query = select(models.User).where(models.User.id == id)
        #user = self.db.execute(query).scalar()
        #print("***************",user[0].username)
        #return user[0]

    def store(self, model: schemas.User):
        
        db_model = models.User(
            username=model.username,
            picture=model.picture,
            stars=model.stars,
            cellphone=model.cellphone, 
            password=model.password,
        )

        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)

        return db_model

    def login(self, model: schemas.UserLogin):
        
        db_model     = self.get_by_param('cellphone', model.cellphone)
        
        if not db_model:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                detail="Telefone ou senhas Incorretas"
            )

        senha_valida = hash_provider.hash_verify(model.password, db_model.password)
        
        if not senha_valida:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                detail="Telefone ou senhas Incorretas"
            )

        token = token_provider.create_access_token({'sub': db_model.cellphone})

        return {
            "user": db_model.username,
            "access_token": token
        }

    def update(self):
        pass
    
    def delete(self):
        pass