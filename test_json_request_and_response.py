import flask
from flask import jsonify


def test_json_request_and_response():
    app = flask.Flask(__name__)
    client = app.test_client()

    @app.route('/echo', methods=['POST'])
    def echo():
        return jsonify(flask.request.get_json())

    with client:
        json_data = {'drink': {'gin': 1, 'tonic': True}, 'price': 10}
        rv = client.post('/echo', json=json_data)

        # Request should be in JSON
        assert flask.request.is_json
        assert flask.request.get_json() == json_data

        # Response should be in JSON
        assert rv.status_code == 200
        assert rv.is_json
        assert rv.get_json() == json_data
