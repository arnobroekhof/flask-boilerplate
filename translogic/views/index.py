from flask.views import MethodView


class IndexView(MethodView):
    def get(self):
        marshaled_dict = {
            'status': 'ok',
            'page': 'index',
        }

        return marshaled_dict, 200
