from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods,require_POST
def login(request) :

    if request.method == 'POST' :
        form = AuthenticationForm(request,request.POST)
        if form.is_valid() :
            user = form.get_user()
            auth_login(request,user)
            return redirect('articles:index')
    
    else :
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html',context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')