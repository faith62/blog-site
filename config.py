class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://faith:123456@localhost/watchlist'


class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True