from django.views import View
from django.shortcuts import redirect

from .authentication import *

class UserLogin(View):
    # método deveria ser POST, pois deverá receber usuario e senha
    def get(self, request):
        user = authenticate(username='user', password='a1b2c3')
        if user:
            token = generateToken(user)
            response = redirect('Weather View')
            response.set_cookie('jwt', token)
            return response
        
        return redirect('Weather View')
    
class UserLogout(View):
    def get(self, request):
        response = redirect('Weather View')
        response.delete_cookie('jwt')
        return response