import flask
from flask.sessions import SessionInterface

def test_session_error_pops_context():
    class SessionError(Exception):
        pass

    class FailingSessionInterface(SessionInterface):
        def open_session(self, app, request):
            raise SessionError()

    class CustomFlask(flask.Flask):
        session_interface = FailingSessionInterface()

    app = CustomFlask(__name__)

    @app.route('/')
    def index():
        # shouldn't get here
        assert False

    response = app.test_client().get('/')
    assert response.status_code == 500
    assert not flask.request
    assert not flask.current_app
