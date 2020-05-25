from flask import Flask
from flask.cli import cli, ScriptInfo, find_best_app, locate_app

def test_find_best_app():
    script_info = ScriptInfo()

    class Module:
        @staticmethod
        def create_app(foo):
            return Flask('appname')
    assert isinstance(find_best_app(script_info, Module), Flask)
    assert find_best_app(script_info, Module).name == 'appname'

    class Module:
        @staticmethod
        def create_app(foo=None, script_info=None):
            return Flask('appname')
    assert isinstance(find_best_app(script_info, Module), Flask)
    assert find_best_app(script_info, Module).name == 'appname'
