import pytest
import flask

def test_trapping_of_bad_request_key_errors():
    app = flask.Flask(__name__)
    client = app.test_client()

    @app.route('/fail')
    def fail():
        flask.request.form['missing_key']

    assert client.get('/fail').status_code == 400
    rv = client.get('/fail')
    assert rv.status_code == 400
    assert b'missing_key' not in rv.data

    app.config['TRAP_BAD_REQUEST_ERRORS'] = True

    with pytest.raises(KeyError) as e:
        client.get("/fail")

    assert e.errisinstance(BadRequest)
    assert 'missing_key' in e.value.description
