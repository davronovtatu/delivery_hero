from sqlalchemy.orm import declarative_base,create_session
from sqlalchemy import create_engine


Base=declarative_base()
session=create_session()

engine=create_engine("postgresql://postgres:6262@localhost/delivery_dbn",echo=True)

