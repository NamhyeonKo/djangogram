from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def main(request):
    if request.method == 'GET':
        return render(request, 'users/main.html')
    elif request.method == 'POST':
        uesrname = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=uesrname,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('posts:index'))
        else:
            return render(request, 'users/main.html')