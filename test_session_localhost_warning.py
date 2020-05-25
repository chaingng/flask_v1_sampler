import flask

def test_session_localhost_warning(recwarn):
    app = flask.Flask(__name__)
    app.config.update(
        SECRET_KEY='testing',
        SERVER_NAME='localhost:5000',
    )

    @app.route('/')
    def index():
        flask.session['testing'] = 42
        return 'testing'

    rv = app.test_client().get('/', 'http://localhost:5000/')
    assert 'domain' not in rv.headers['set-cookie'].lower()
    w = recwarn.pop(UserWarning)
    assert '"localhost" is not a valid cookie domain' in str(w.message)
