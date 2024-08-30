from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.views.decorators.cache import cache_control
from django.http import Http404
# Create your views here.


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_login(request):
    result = ""
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            request.session['username'] = username
            return redirect(home)
        else:
            result = "invalid usrname or password"
            
    return render(request, 'login.html',{'error':result})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def home(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    else:
        return redirect(user_login)

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_logout(request):
    if request.method != 'POST':
        raise Http404()
    if 'username' in request.session:
        request.session.flush()
    return redirect(user_login)