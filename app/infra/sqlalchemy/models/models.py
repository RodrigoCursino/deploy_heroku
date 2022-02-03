from app.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm                       import relationship
from sqlalchemy                           import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.infra.providers                  import hash_provider


class User(Base):
    __tablename__ = "users"
    id         = Column(Integer, primary_key=True, autoincrement=True)
    username   = Column(String(100))
    picture    = Column(String(800))
    stars      = Column(Integer)
    cellphone  = Column(String(20), unique=True)
    password   = Column(String(255))
    activate   = Column(Boolean, default=True)

    def __init__(self, username, picture, stars, cellphone, password, activate=True):
        self.username  = username
        self.picture   = picture
        self.stars     = stars
        self.cellphone = cellphone
        self.activate  = activate
        self.password  = hash_provider.get_hash(password)
