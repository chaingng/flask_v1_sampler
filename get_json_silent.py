import flask
import pytest
from werkzeug.exceptions import BadRequest

app = flask.Flask(__name__)

def test_different_silent_on_bad_request(app):
    with app.test_request_context('/', method='POST', data='malformed',content_type='application/json'):
        assert flask.request.get_json(silent=True) is None
        with pytest.raises(BadRequest):
            flask.request.get_json(silent=False)


test_different_silent_on_bad_request(app)
