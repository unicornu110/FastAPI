# Api
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas
from typing import List

app = _fastapi.FastAPI()
_services.create_database()

@app.post("/users/",response_model=_schemas.User)
def create_user(user: _schemas.User_create,
                db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = _services.get_user_by_email(db=db,email=user.email)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="woops the email in use")
    return _services.create_user(db=db,user=user)

@app.get("/users/",response_model=List[_schemas.User])
def read_users(
        skip:int=0,
        limit:int=10,
        db:_orm.Session = _fastapi.Depends(_services.get_db),
):
    users = _services.get_users(db=db, skip = skip, limit = limit)
    return users

@app.get("/users/{user_id}",response_model=_schemas.User)
def read_user(user_id:int,
              db:_orm.Session = _fastapi.Depends(_services.get_db)):
    db_user=_services.get_user(db=db,user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(status_code=404,detail="Sorry this user does not exist")
    return db_user

@app.post("/users/{user_id}/Address/",response_model = _schemas.Address)
def create_post(
        user_id : int,
        address : _schemas.Addess_create,
        db : _orm.Session = _fastapi.Depends(_services.get_db)
):
    return _services.create_post(db=db, post=address, user_id=user_id)


@app.get("/posts/",response_model=List[_schemas.Address])
def read_posts(
        skip:int=0,
        limit:int=10,
        db:_orm.Session = _fastapi.Depends(_services.get_db)
):
    posts = _services.get_posts(db=db, skip = skip, limit = limit)
    return posts

@app.get("/posts/{post_id}",response_model=_schemas.Address)
def read_post(post_id:int, db:_orm.Session = _fastapi.Depends(_services.get_db)):
    postr = _services.get_post(db=db,address_id=post_id)
    if postr is None:
        raise _fastapi.HTTPException(status_code=404, detail="Sorry this Address does not exist")
    return postr

# to delete the address
@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_post(db=db,address_id=post_id)
    return {"message": f"{post_id} is deleted"}







