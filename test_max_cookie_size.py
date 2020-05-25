import flask


def test_max_cookie_size(recwarn):
    app = flask.Flask(__name__)
    client = app.test_client()

    app.config['MAX_COOKIE_SIZE'] = 100

    # outside app context, default to Werkzeug static value,
    # which is also the default config
    response = flask.Response()
    default = flask.Flask.default_config['MAX_COOKIE_SIZE']
    assert response.max_cookie_size == default

    # inside app context, use app config
    with app.app_context():
        assert flask.Response().max_cookie_size == 100

    @app.route('/')
    def index():
        r = flask.Response('', status=204)
        r.set_cookie('foo', 'bar' * 100)
        return r

    client.get('/')
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert 'cookie is too large' in str(w.message)

    app.config['MAX_COOKIE_SIZE'] = 0

    client.get('/')
    assert len(recwarn) == 0