from sqlalchemy import Column, String
from app.db.session import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(unique=True, primary_key=True, autoincrement=True)
    name = Column(String(512))

    def __repr__(self):
        return (f"<User id={self.id} name={self.name}", ">")
