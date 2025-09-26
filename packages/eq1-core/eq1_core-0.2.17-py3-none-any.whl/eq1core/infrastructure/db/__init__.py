from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

import os


SQLALCHEMY_DATABASE_URL = os.getenv('DB_URL')
if SQLALCHEMY_DATABASE_URL is None:
    SQLALCHEMY_DATABASE_URL = ("mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
                               .format(db_user=os.getenv("DB_USER"),
                                       db_password=os.getenv("DB_PASSWORD"),
                                       db_host=os.getenv('DB_HOST'),
                                       db_port=os.getenv('DB_PORT'),
                                       db_name=os.getenv('DB_NAME')
                                       )
                               )

# SessionLocal을 None으로 초기화
SessionLocal = None
engine = None
Base = declarative_base()

try:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        # isolation_level="AUTOCOMMIT",
        echo=False,
        pool_pre_ping=True  # 연결이 유효한지 확인
    )

    SessionLocal = scoped_session(
        sessionmaker(
            autoflush=False,
            bind=engine
        )
    )
except (ValueError, Exception) as e:
    print(f"Database connection error: {e}")
    print("DB_URL is not set. Please set DB_URL environment variable.")
    # SessionLocal은 None으로 유지

def create_all_table():
    if engine:
        Base.metadata.create_all(bind=engine)

def drop_all_table():
    if engine:
        Base.metadata.drop_all(bind=engine)
