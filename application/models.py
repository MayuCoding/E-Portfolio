from sqlalchemy import Integer,String,Boolean
from sqlalchemy.orm import Mapped, mapped_column
from application import db

# Define the User class
class User(db.Model):
    """
    The user model. Contains the following columns:
    > Id
    > Email
    > Username
    > Password
    > Admin Status


    ORM => Object Relational Mapping
    SQL => Sttrucutured Query Language

    Python => (needs ORM as aninterepreter) => SQL => DB (Database)
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username : Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    password:Mapped[str] = mapped_column(String(50))
    admin_status : Mapped[bool] = mapped_column(Boolean, default=False)

# Add the Admin class here
class Admin(User):
    """
    Admin model. Inherits from User. Contains the following columns:
    """
    
    status: Mapped [ str] = mapped_column(String(10), default = "admin")

    def __repr__(self) -> str: 
        return f"User<{self.username}, {self.email}, {self.admin_status}>"
    
    
    def __str__(self) -> str:
        return f"User<{self.username}, {self.email}, {self.admin_status}"
        