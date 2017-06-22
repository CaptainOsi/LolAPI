from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setting import *

engine = create_engine('mysql://' + MYSQL_USER_NAME + ':' + MYSQL_PWD + '@' + MYSQL_SERVER_NAME + ':3306/' + MYSQL_BDD, echo=False)
Session = sessionmaker(bind=engine)
session = Session()