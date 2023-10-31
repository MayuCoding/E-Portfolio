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


def create_test_data(database):
    """
    Used to create test data in database.
    """
    # Admin User
    admin = User(username = "admin", email="admin@admin.mail", password = "admin", admin_status=True)

    # Other users
    user1 = User(username = "user1", email="user1@user1.mail", password = "admin", admin_status=True)
    user2 = User(username = "user2", email="Huh@questionmark.mail", password = "admin", admin_status=True)
    user3 = User(username = "user3", email="person@painter.mail", password = "admin", admin_status=True)
    user4 = User(username = "user4", email="LOL@userblah.mail", password = "admin", admin_status=True)
    user5 = User(username = "user5", email="friend@youandI.mail", password = "admin", admin_status=True)
    user6 = User(username = "user6", email="user6@another.mail", password = "admin", admin_status=True)

    existing_users = User.query.all()
    existing_user_emails = [user.email for user in existing_users]

    # Add the admin user 
    if admin not in existing_users and admin.email not in existing_user_emails:
        database.session.add(admin)
        
    # Add teh other users
    if user1 not in existing_users and user1.email not in existing_user_emails:
        database.session.add(user1)
    if user2 not in existing_users and user2.email not in existing_user_emails:
        database.session.add(user2)
    if user3 not in existing_users and user3.email not in existing_user_emails:
        database.session.add(user3)
    if user4 not in existing_users and user4.email not in existing_user_emails:
        database.session.add(user4)
    if user5 not in existing_users and user5.email not in existing_user_emails:
        database.session.add(user5)
    if user6 not in existing_users and user6.email not in existing_user_emails:
        database.session.add(user6)

    # Commit the changes to the database

    database.session.commit()