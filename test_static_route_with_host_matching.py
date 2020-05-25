import flask
import pytest

def test_static_route_with_host_matching():
    app = flask.Flask(__name__, host_matching=True, static_host='example.com')
    c = app.test_client()
    rv = c.get('http://example.com/static/index.html')
    assert rv.status_code == 200
    rv.close()
    with app.test_request_context():
       rv = flask.url_for('static', filename='index.html', _external=True)
       assert rv == 'http://example.com/static/index.html'
    # Providing static_host without host_matching=True should error.
    with pytest.raises(Exception):
        flask.Flask(__name__, static_host='example.com')
    # Providing host_matching=True with static_folder but without static_host should error.
    with pytest.raises(Exception):
        flask.Flask(__name__, host_matching=True)
    # Providing host_matching=True without static_host but with static_folder=None should not error.
    flask.Flask(__name__, host_matching=True, static_folder=None)
