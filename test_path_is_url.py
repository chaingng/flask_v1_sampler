from flask.testing import make_test_environ_builder
import flask

def test_path_is_url():
    app = flask.Flask(__name__)
    eb = make_test_environ_builder(app, 'https://example.com/')
    assert eb.url_scheme == 'https'
    assert eb.host == 'example.com'
    assert eb.script_root == ''
    assert eb.path == '/'
