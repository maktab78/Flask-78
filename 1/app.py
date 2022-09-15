from flask import Flask
from urls import routes
from core.utils import Router

app = Flask(__name__)
router = Router(app, routes)

# import views
#
# @app.route('/')
# ...
#
# @app.route("/power", defaults={'x': None, 'y': None})
# @app.route("/power/<int:x>", defaults={'y': 2})
# @app.route("/power/<int:x>/<int:y>")
# ...

# app.add_url_rule('/', 'index', views.hello_world)
# app.add_url_rule('/power/<int:x>/<int:y>', 'power', views.power)
# app.add_url_rule()

# @app.errorhandler(404)
# def not_found(e):
#     return "Not found error | Maktab 78", 404

# app.register_error_handler()
