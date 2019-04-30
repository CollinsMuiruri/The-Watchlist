class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = https://api.themoviedb.org/3/movie/550?api_key=52c40cdeb693f66cf9801ff9af468154
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