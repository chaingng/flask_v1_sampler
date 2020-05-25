import flask
from werkzeug.exceptions import Forbidden,HTTPException,NotFound

def test_default_error_handler():
    bp = flask.Blueprint('bp', __name__)

    @bp.errorhandler(HTTPException)
    def bp_exception_handler(e):
        assert isinstance(e, HTTPException)
        assert isinstance(e, NotFound)
        return 'bp-default'

    @bp.errorhandler(Forbidden)
    def bp_exception_handler(e):
        assert isinstance(e, Forbidden)
        return 'bp-forbidden'

    @bp.route('/undefined')
    def bp_registered_test():
        raise NotFound()

    @bp.route('/forbidden')
    def bp_forbidden_test():
        raise Forbidden()

    app = flask.Flask(__name__)

    @app.errorhandler(HTTPException)
    def catchall_errorhandler(e):
        assert isinstance(e, HTTPException)
        assert isinstance(e, NotFound)
        return 'default'

    @app.errorhandler(Forbidden)
    def catchall_errorhandler(e):
        assert isinstance(e, Forbidden)
        return 'forbidden'

    @app.route('/forbidden')
    def forbidden():
        raise Forbidden()

    app.register_blueprint(bp, url_prefix='/bp')

    c = app.test_client()
    assert c.get('/bp/undefined').data == b'bp-default'
    assert c.get('/bp/forbidden').data == b'bp-forbidden'
    assert c.get('/undefined').data == b'default'
    assert c.get('/forbidden').data == b'forbidden'
