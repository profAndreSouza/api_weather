from django.views import View
from django.http.response import HttpResponse

from .authentication import *

class UserTokenizer(View):
    # método deveria ser POST, pois deverá receber usuario e senha
    def get(self, request):
        user = authenticate(username='user', password='a1b2c3')
        if user:
            return HttpResponse(generateToken(user))
        return HttpResponse('Username and/or password incorret')