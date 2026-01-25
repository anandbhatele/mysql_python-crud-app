from sqlalchemy.orm import sessionmaker
from create_table import engine

sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
