from sqlalchemy import create_engine, MetaData


# SQLALCHEMY_DATABASE_URL ='mysql+pymysql://root:root@localhost:3306/database'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/database'
SQLALCHEMY_DATABASE_URL = 'sqlite:///./database.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
meta = MetaData()
conn = engine.connect()