from flask import Flask

def create_app(config_name='development'):
    app = Flask(__name__)
    if config_name == 'production':
        app.config.from_object('config.ProductionConfig')
        print('production mode')
    elif config_name == 'testing':
        app.config.from_object('config.TestingConfig')
        print('testing mode')
    else:
        app.config.from_object('config.DevelopmentConfig')
        print('development mode')

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app