import flask

def test_blueprint_json_customization():
    class X(object):
        def __init__(self, val):
            self.val = val
    class MyEncoder(flask.json.JSONEncoder):
        def default(self, o):
            if isinstance(o, X):
                return '<%d>' % o.val
            return flask.json.JSONEncoder.default(self, o)
    class MyDecoder(flask.json.JSONDecoder):
        def __init__(self, *args, **kwargs):
            kwargs.setdefault('object_hook', self.object_hook)
            flask.json.JSONDecoder.__init__(self, *args, **kwargs)
        def object_hook(self, obj):
            if len(obj) == 1 and '_foo' in obj:
                return X(obj['_foo'])
            return obj

    blue = flask.Blueprint('blue', __name__)
    blue.json_encoder = MyEncoder
    blue.json_decoder = MyDecoder
    @blue.route('/bp', methods=['POST'])
    def index():
        return flask.json.dumps(flask.request.get_json()['x'])

    app = flask.Flask(__name__)
    app.testing = True
    app.register_blueprint(blue)

    c = app.test_client()
    rv = c.post('/bp', data=flask.json.dumps({
        'x': {'_foo': 42}
        }), content_type='application/json')
    assert rv.data == b'"<42>"'