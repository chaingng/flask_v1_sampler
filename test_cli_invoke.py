import flask
import click

def test_cli_invoke():
    app = flask.Flask(__name__)

    @app.cli.command('hello')
    def hello_command():
        click.echo('Hello, World!')

    runner = app.test_cli_runner()
    # invoke with command name
    result = runner.invoke(args=['hello'])
    assert 'Hello' in result.output
    # invoke with command object
    result = runner.invoke(hello_command)
    assert 'Hello' in result.output
