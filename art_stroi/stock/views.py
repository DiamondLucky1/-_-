from django.shortcuts import render, redirect

from unicodedata import category
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login as auth_login


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'stock/index.html', {'title': 'Вход'})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user if user else 'oshibka')
        print(authenticate(request, username=username, password=password))
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            return redirect('vhod')
