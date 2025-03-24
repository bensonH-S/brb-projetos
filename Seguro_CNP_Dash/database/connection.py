from sqlalchemy import create_engine
import os

# Você pode definir a variável DATABASE_URI via variável de ambiente ou deixar fixo.
DATABASE_URI = os.getenv("DATABASE_URI", "mariadb+mariadbconnector://root:@localhost:3306/gecaf")
engine = create_engine(DATABASE_URI)
