import os

class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/second'


    #e-mail configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ("MAIL_USERNAME")
    MAIL_PASSWORD = os.envirot("MAIL_PASSWORD")


class ProdConfig(Config):
    """
    Production config child class

    Args:
        Config: The parent config clss with general config classes
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/second'
