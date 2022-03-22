from sqlalchemy import create_engine,MetaData

#especificar el puerto y a que bdd conectarte
engine = create_engine("mysql+pymysql://root:@localhost:3306/fastapi")
meta = MetaData()
conn = engine.connect()