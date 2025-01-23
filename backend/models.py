from sqlalchemy import create_engine
from env_variables import DBUSER,DBPASSWORD,HOST,DBNAME
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base



DATABASE_URL = f"mysql+mysqlconnector://{DBUSER}:{DBPASSWORD}@{HOST}/{DBNAME}"


engine = create_engine(DATABASE_URL)
Base = declarative_base()



class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False )
    email = Column(String(80), nullable=False, unique=True)
    last_name = Column(String(80), nullable=False, unique=True)
    nick_name = Column(String(30), nullable=False, unique=True )
    #create_at = 