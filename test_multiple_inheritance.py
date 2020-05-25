def test_multiple_inheritance():
    app = flask.Flask(__name__)

    class GetView(flask.views.MethodView):
        def get(self):
            return 'GET'

    class DeleteView(flask.views.MethodView):
        def delete(self):
            return 'DELETE'

    class GetDeleteView(GetView, DeleteView):
        pass

    app.add_url_rule('/', view_func=GetDeleteView.as_view('index'))

    c = app.test_client()
    assert c.get('/').data == b'GET'
    assert c.delete('/').data == b'DELETE'
    assert sorted(GetDeleteView.methods) == ['DELETE', 'GET']
