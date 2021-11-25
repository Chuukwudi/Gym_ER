

#########################################################
# Configuration details - Development Environment
#########################################################

class Config:
    '''set base flask configurations
    '''
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    TEMPLATES_AUTO_RELOAD = True 
    HOST="0.0.0.0"
    PORT="5000"    


#########################################################
# Configuration details - Configuration Object
#########################################################

class DevConfig(Config):
    '''set base Development configurations
    '''
    SECRET_KEY="dev"
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    
#########################################################
# Configuration details - Testing / Pre-Prod Environment
#########################################################

class TestingConfig(Config):
    SECRET_KEY="test"
    FLASK_ENV = 'Testing'
    TESTING = True
    DEBUG = True
    


#########################################################
# Configuration details - Production Environment
##########################################################

class ProdConfig(Config):
    SECRET_KEY="prod"
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

