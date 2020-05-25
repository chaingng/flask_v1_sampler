import flask

def test_session_vary_cookie():
    app = flask.Flask(__name__)
    app.secret_key = 'testkey'

    @app.route('/set')
    def set_session():
        flask.session['test'] = 'test'
        return ''

    @app.route('/get')
    def get():
        return flask.session.get('test')

    @app.route('/getitem')
    def getitem():
        return flask.session['test']

    @app.route('/setdefault')
    def setdefault():
        return flask.session.setdefault('test', 'default')

    @app.route('/no-vary-header')
    def no_vary_header():
        return ''

    c = app.test_client()

    def expect(path, header=True):
        rv = c.get(path)

        if header:
            assert rv.headers['Vary'] == 'Cookie'
        else:
            assert 'Vary' not in rv.headers

    expect('/set')
    expect('/get')
    expect('/getitem')
    expect('/setdefault')
    expect('/no-vary-header', False)


if __name__ == '__main__':
    test_session_vary_cookie()