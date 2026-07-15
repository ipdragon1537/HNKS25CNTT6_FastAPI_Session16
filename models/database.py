from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
db_url = "mysql+pymysql://root:123456@localhost:3306/demo_test"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False,autocommit = False,bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
