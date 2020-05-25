import pytest
import flask

@pytest.mark.parametrize('matching', (False, True))
def test_subdomain_matching_other_name(matching):
    app = flask.Flask(__name__, subdomain_matching=matching)
    app.config['SERVER_NAME'] = 'localhost.localdomain:3000'
    client = app.test_client()

    @app.route('/')
    def index():
        return '', 204

    # ip address can't match name
    rv = client.get('/', 'http://127.0.0.1:3000/')
    assert rv.status_code == 404 if matching else 204

    # allow all subdomains if matching is disabled
    rv = client.get('/', 'http://www.localhost.localdomain:3000/')
    assert rv.status_code == 404 if matching else 204
