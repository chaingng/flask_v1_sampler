import flask

def test_url_for_passes_special_values_to_build_error_handler():
    app = flask.Flask(__name__)

    @app.url_build_error_handlers.append
    def handler(error, endpoint, values):
        assert values == {
            '_external': False,
            '_anchor': None,
            '_method': None,
            '_scheme': None,
        }
        return 'handled'

    with app.test_request_context():
        flask.url_for('/')