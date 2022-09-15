import views
from core.utils import Route, Handler

routes = [
    Route("/", "hi", views.hello_world),
    Route("/hello/world/from/maktab", endpoint=None, view_func=views.hello_world),
    Route("/test", endpoint=None, view_func=views.test, methods=['POST']),
    Route("/info/<string:endpoint>", "information", views.info),
    Route("/power/<int:x>/<int:y>", "power", views.power),

    # Handlers:
    Handler(404, views.not_found)
]
