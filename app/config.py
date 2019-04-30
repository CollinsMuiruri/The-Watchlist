class Config:
    '''
    General configuration parent class
    '''
    pass
class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: the parent configuration class with General configuration settings
    '''
class DevConfig(Config):
    '''
    Development configuration child class 
    Args:
        Config: the parent configuration class with General configuration settings
    '''

    DEBUG = True