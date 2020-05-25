import flask

def test_session_ip_warning(recwarn):
    app = flask.Flask(__name__)
    app.config.update(
        SECRET_KEY='testing',
        SERVER_NAME='127.0.0.1:5000',
    )

    @app.route('/')
    def index():
        flask.session['testing'] = 42
        return 'testing'

    rv = app.test_client().get('/', 'http://127.0.0.1:5000/')
    assert 'domain=127.0.0.1' in rv.headers['set-cookie'].lower()
    w = recwarn.pop(UserWarning)
    assert 'cookie domain is an IP' in str(w.message)
