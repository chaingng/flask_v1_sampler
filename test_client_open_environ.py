import flask


def test_client_open_environ():
    app = flask.Flask(__name__)
    client = app.test_client()

    @app.route('/index')
    def index():
        return flask.request.remote_addr

    builder = flask.testing.make_test_environ_builder(app, path='/index', method='GET')

    rv = client.open(builder)
    assert rv.data == b'127.0.0.1'

    environ = builder.get_environ()
    client.environ_base['REMOTE_ADDR'] = '127.0.0.2'
    rv = client.open(environ)
    assert rv.data == b'127.0.0.2'
