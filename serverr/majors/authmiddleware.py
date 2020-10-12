from collections import namedtuple
import json


class AuthMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):

        Auth = namedtuple('Auth', field_names=(
            'valid', 'type', 'user', 'valid_till'))
        request.auth = Auth(valid=True, type=1, user={'id': 1}, valid_till=100)
        if request.body != '':
            try:
                request.json = json.loads(request.body.decode('utf-8'))
            except Exception as e:
                print("Cant decode json", e)
        # To be executed before view call
        response = self.get_response(request)
        # To be executed after view call

        return response
