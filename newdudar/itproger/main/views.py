from django.shortcuts import redirect, render
from django.contrib import auth
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('login')
    return render(request, 'main/contact.html')

