import flask

def test_blueprint_with_subdomain():
    app = flask.Flask(__name__)
    app.testing = True
    app.config['SERVER_NAME'] = 'example.com:1234'
    app.config['APPLICATION_ROOT'] = '/foo'

    bp = flask.Blueprint('company', __name__, subdomain='xxx')
    @bp.route('/')
    def index():
        return flask.request.url
    app.register_blueprint(bp)

    ctx = app.test_request_context('/', subdomain='xxx')
    assert ctx.request.url == 'http://xxx.example.com:1234/foo/'
    with app.test_client() as c:
        rv = c.get('/', subdomain='xxx')
        assert rv.data == b'http://xxx.example.com:1234/foo/'
