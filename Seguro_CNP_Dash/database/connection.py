from sqlalchemy import create_engine

DATABASE_URI = "mariadb+mariadbconnector://root:@localhost:3306/gecaf"
engine = create_engine(DATABASE_URI)
