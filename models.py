import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _db

class User(_db.Base):
    __tablename__ = "user"
    id = _sql.Column(_sql.Integer, primary_key = True, index = True)
    email = _sql.Column(_sql.String, unique = True, index = True)
    hashed_password = _sql.Column(_sql.String)
    is_active = _sql.Column(_sql.Boolean, default = True)

    add = _orm.relationship("Address", back_populates = "place")


class Address(_db.Base):
    __tablename__ = "address"
    id = _sql.Column(_sql.Integer, primary_key = True, index = True)
    country = _sql.Column(_sql.String, index = True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("user.id"))
    state = _sql.Column(_sql.String, index = True)
    city = _sql.Column(_sql.String, index = True)
    pincode = _sql.Column(_sql.Integer, index = True)
    address = _sql.Column(_sql.String, index = True)

    place = _orm.relationship("User", back_populates = "add")

