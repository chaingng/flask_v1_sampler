import flask

def test_provide_automatic_options_kwarg():
    app = flask.Flask(__name__)

    def index():
        return flask.request.method

    def more():
        return flask.request.method

    app.add_url_rule('/', view_func=index, provide_automatic_options=False)

    c = app.test_client()
    assert c.get('/').data == b'GET'

    rv = c.post('/')
    assert rv.status_code == 405
    assert sorted(rv.allow) == ['GET', 'HEAD']

    # Older versions of Werkzeug.test.Client don't have an options method
    if hasattr(c, 'options'):
        rv = c.options('/')
    else:
        rv = c.open('/', method='OPTIONS')

    assert rv.status_code == 405