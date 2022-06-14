# An intermidiater file between Api and databade
import database as _db
import sqlalchemy.orm as _orm
import models as _models
import schemas as _schemas

def create_database():
    return _db.Base.metadata.create_all(bind=_db.engine)

def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(db:_orm.Session,email:str):
    return db.query(_models.User).filter(_models.User.email==email).first()

def create_user(db:_orm.Session,user:_schemas.User_create):
    fake_hashed_password = user.password+"this is not secure"
    db_user = _models.User(email = user.email,hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db:_orm.Session, skip: int, limit: int):
    return db.query(_models.User).offset(skip).limit(limit).all()

def get_user(db: _orm.Session, user_id: int):
    return db.query(_models.User).filter(_models.User.id==user_id).first()

def create_post(db: _orm.Session, post: _schemas.Addess_create,user_id = int):
    post = _models.Address(**post.dict(), owner_id = user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
def get_posts(db: _orm.Session,skip: int, limit: int):
    return db.query(_models.Address).offset(skip).limit(limit).all()

def get_post(db: _orm.Session,address_id: int):
    return db.query(_models.Address).filter(_models.Address.id==address_id).first()

def delete_post(db: _orm.Session, address_id = int):
    db.query(_models.Address).filter(_models.Address.id==address_id).delete()
    db.commit()