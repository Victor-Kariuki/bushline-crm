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

    # mail configs
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('SENDGRID_API_KEY')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')


class DevelopmentConfig(Config):
    """
    Development environment configs
    """

    DEBUG = True


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


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
