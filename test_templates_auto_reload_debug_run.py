import flask
import werkzeug
from _pytest import monkeypatch

def test_templates_auto_reload_debug_run(monkeypatch):
    app = flask.Flask(__name__)

    def run_simple_mock(*args, **kwargs):
        pass

    monkeypatch.setattr(werkzeug.serving, 'run_simple', run_simple_mock)

    app.run()
    assert app.templates_auto_reload == False
    assert app.jinja_env.auto_reload == False

    app.run(debug=True)
    assert app.templates_auto_reload == True
    assert app.jinja_env.auto_reload == True
