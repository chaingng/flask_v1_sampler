import flask

def test_blueprint_prefix_slash():
    app = flask.Flask(__name__)
    client = app.test_client()

    bp = flask.Blueprint('test', __name__, url_prefix='/bar/')

    @bp.route('/foo')
    def foo():
        return '', 204

    app.register_blueprint(bp)
    app.register_blueprint(bp, url_prefix='/spam/')
    assert client.get('/bar/foo').status_code == 204
    assert client.get('/spam/foo').status_code == 204
