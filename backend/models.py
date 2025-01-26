from sqlalchemy import create_engine, text
from env_variables import DBUSER,DBPASSWORD,HOST,DBNAME
from sqlalchemy import Column, Integer, String, DateTime,ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import bcrypt


DATABASE_URL = f"mysql+mysqlconnector://{DBUSER}:{DBPASSWORD}@{HOST}/{DBNAME}"


engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    user  = relationship("User")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False )
    email = Column(String(80), nullable=False, unique=True)
    last_name = Column(String(80), nullable=False, unique=True)
    nick_name = Column(String(30), nullable=False, unique=True )
    elo_points = Column(Integer, default=400)
    role = Column(Integer,ForeignKey("role.id"))
    _password = Column("password", String, nullable=False)
    create_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP') )
    update_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP') )
    last_coneccion = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    __table_args__ = (
        Index('idx_username_email', 'nick_name', 'email'),
        Index('idx_role', 'role'),
        Index('idx_elo', 'elo_points'),
    )

    @property
    def password (self):
        raise AttributeError("La contraseña no es accesible directamente.")
    
    @password.setter
    def password(self, plain_password):

        salt = bcrypt.gensalt()
        self._password = bcrypt.hashpw(plain_password.encode('utf-8'), salt).decode('utf-8')

    def check_pw(self, password):

        return bcrypt.checkpw(password.encode('utf-8'), self._password.encode('utf-8'))
    
    def verify_email(self, email):
        pass 
    def autenticate_user_by_email(self, email, password):
        pass
