# importing required lib
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread":False}
)

SessionLocal = _orm.create_session(autocommit = False, autoflush = False, bind = engine)

Base = _declarative.declarative_base()