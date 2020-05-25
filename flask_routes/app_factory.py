import flask

def create_app():
    app = flask.Flask(__name__)

    @app.route('/tasks', methods=['GET'])
    def list_all_tasks():
        return flask.request.method


    @app.route('/tasks/<int:taskid>', methods=['GET'])
    def show_task(taskid):
        return flask.request.method


    @app.route('/tasks/<int:taskid>', methods=['DELETE'])
    def delete_task(taskid):
        return flask.request.method

    @app.route('/tasks', methods=['POST'])
    def create_task():
        return flask.request.method


    @app.route('/tasks/<int:taskid>', methods=['PUT'])
    def update_task(taskid):
        return flask.request.method

    return app