import flask

def test_attachment_with_utf8_filename():
    app = flask.Flask(__name__)

    with app.test_request_context():
        rv = flask.send_file('static/index.html', as_attachment=True, attachment_filename=u'Ñandú／pingüino.txt')
        content_disposition = set(rv.headers['Content-Disposition'].split('; '))
        assert content_disposition == set((
            'attachment',
            'filename="Nandu/pinguino.txt"',
            "filename*=UTF-8''%C3%91and%C3%BA%EF%BC%8Fping%C3%BCino.txt"
        ))
        rv.close()
