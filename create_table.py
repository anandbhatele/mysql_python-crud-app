from database import Base
from sqlalchemy import Column , Integer , String,create_engine


class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True,index=True,nullable=True)
    name=Column(String(50))
    email=Column(String(50),unique=True,nullable=True)

engine = create_engine("mysql+pymysql://root@localhost/fastapi_first",echo=True)
Base.metadata.create_all(bind=engine)

