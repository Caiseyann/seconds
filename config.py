import os

class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/second'


    #e- configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    """
    Production config child class

    Args:
        Config: The parent config class with general config classes
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/second'


class TestConfig(Config):
    """
    Testing config child class

    Args:
        Config: The parent config class with general config classes
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/second'
    DEBUG = True


class DevConfig(Config):
    '''
    Dev config child class

    Args:
        Config: The parent config class with general config settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/second'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}