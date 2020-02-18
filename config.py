# config.py

# inbuilt imports
import os

class Config():
    """
    Global environment configs
    """

    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')

    # sqlalchemy configs
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DevelopmentConfig(Config):
    """
    Development environment configs
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production environment configs
    """


class TestingConfig(Config):
    """
    Testing environment configs
    """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
