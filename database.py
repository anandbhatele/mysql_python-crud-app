from sqlalchemy import create_engine,text
from sqlalchemy.orm import declarative_base


dtabase_name="mysql+pymysql://root@localhost"
engine=create_engine(dtabase_name,echo=True)
try:
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS fastapi_first"))
        print("Database are created.....")
except Exception as e:
    print("ERROR>>>>>>",e)

Base=declarative_base()



