import flask

def test_stream_keeps_session():
    app = flask.Flask(__name__)
    client = app.test_client()

    @app.route('/')
    def index():
        flask.session['test'] = 'flask'

        @flask.stream_with_context
        def gen():
            yield flask.session['test']

        return flask.Response(gen())

    rv = client.get('/')
    assert rv.data == b'flask'
