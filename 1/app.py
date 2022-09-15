import views
from flask import Flask

app = Flask(__name__)

# @app.route('/')
# ...
#
# @app.route("/power", defaults={'x': None, 'y': None})
# @app.route("/power/<int:x>", defaults={'y': 2})
# @app.route("/power/<int:x>/<int:y>")
# ...

app.add_url_rule('/', 'index', views.hello_world)
app.add_url_rule('/power/<int:x>/<int:y>', 'power', views.power)
