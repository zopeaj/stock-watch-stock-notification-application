from sqlachemy.orm import sessionmaker
from sqlachemy import create_engine

engine = create_engine("sqlite:///", echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoFlush=False)
