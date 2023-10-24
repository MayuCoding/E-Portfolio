# Create the base configurations for the application
class Config(object):
    """
    Base configuration class. Contains default configuration settings.
    """
    # Generate the  secrete key in the terminal
    # Go to the terminal : python3 to open teh python interpreter
    # import uuid (Universal Unique IDentifier)
    # print(uuid.uuid4().hex)
    SECRET_KEY = "7e3c045838ee4a8cb3ed078eb96b8b2f"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
    SQLALCHEMY_ECHO = False
    

class ProdConfig(Config):
    """
    Production configuarion class. Contains configuration settings for a production enviroment
    """
    DEBUG = False

class DevConfig(Config):
    """
    Development configuartion class. Contains configuarion settings for a development environment.
    """
    DEBUG = True