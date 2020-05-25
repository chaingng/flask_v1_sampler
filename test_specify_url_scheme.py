import flask

def test_specify_url_scheme():
        app = flask.Flask(__name__)
        app.testing = True
        @app.route('/')
        def index():
            return flask.request.url

        ctx = app.test_request_context(url_scheme='https')
        assert ctx.request.url == 'https://localhost/'
