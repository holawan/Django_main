from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods,require_POST

@require_http_methods(['GET','POST'])
def login(request) :
    # 로그인 되어있으면 로그인 못하게 
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST' :
        #AuthenticationForm은 첫번째 인자로 request를 바음 
        form = AuthenticationForm(request,request.POST)
        if form.is_valid() :
            #인증이 되었다면 로그인 진행
            user = form.get_user()
            auth_login(request,user)
            return redirect(request.GET.get('next') or 'articles:index')
    
    else :
        #장고의 built-in login_form
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html',context)


@require_POST
def logout(request):
    if request.user.is_authenticated : 
        auth_logout(request)
    return redirect('articles:index')