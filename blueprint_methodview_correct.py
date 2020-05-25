from flask import Flask, Blueprint, request, abort
from flask.views import MethodView


app = Flask(__name__)
system = Blueprint('system', __name__, url_prefix='/system')

class UserView(MethodView):
    def get(self):
        return 'user list'


system.add_url_rule('/user', view_func=UserView.as_view('user_list'))

app.register_blueprint(system)

app.run()