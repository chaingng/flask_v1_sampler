import flask


def test_session_using_samesite_attribute():
    app = flask.Flask(__name__)
    app.secret_key = 'testkey'

    @app.route('/')
    def set_session():
        flask.session['test'] = 'test'
        return ''

    app.config.update(SESSION_COOKIE_SAMESITE='Strict')
    rv = app.test_client().get('/')
    cookie = rv.headers['set-cookie'].lower()
    assert 'samesite=strict' in cookie

    app.config.update(SESSION_COOKIE_SAMESITE='Lax')
    rv = app.test_client().get('/')
    cookie = rv.headers['set-cookie'].lower()
    assert 'samesite=lax' in cookie