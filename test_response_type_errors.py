import flask
import pytest

def test_response_type_errors():
    app = flask.Flask(__name__)
    app.testing = True

    @app.route('/none')
    def from_none():
        pass

    @app.route('/small_tuple')
    def from_small_tuple():
        return 'Hello',

    @app.route('/large_tuple')
    def from_large_tuple():
        return 'Hello', 234, {'X-Foo': 'Bar'}, '???'

    @app.route('/bad_type')
    def from_bad_type():
        return True

    @app.route('/bad_wsgi')
    def from_bad_wsgi():
        return lambda: None

    c = app.test_client()

    with pytest.raises(TypeError) as e:
        c.get('/none')
        assert 'returned None' in str(e)

    with pytest.raises(TypeError) as e:
        c.get('/small_tuple')
        assert 'tuple must have the form' in str(e)

    pytest.raises(TypeError, c.get, '/large_tuple')

    with pytest.raises(TypeError) as e:
        c.get('/bad_type')
        assert 'it was a bool' in str(e)

    pytest.raises(TypeError, c.get, '/bad_wsgi')
