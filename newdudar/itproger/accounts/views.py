from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Logged in')
            return redirect('news_home')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                print("Error. User already exist")
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, )
                user.save()
                return redirect('login')
    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('login')