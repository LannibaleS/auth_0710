from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        print(username, pwd)

        # 如何判断用户名密码对不对
        user = auth.authenticate(username=username, password=pwd)
        # 将登陆的用户封装到request.user
        # request.user = user_obj
        auth.login(request, user)

        if user:
            print(user)
            # return redirect(request, '/index.html/')
            return redirect('/index')
            # return HttpResponseRedirect('/index')

    return render(request, 'login.html')

# 要求登录装饰器，没有登录的话就进不去index
@login_required
def index(request):
    print(request.user.username)
    print(request.user.password)

    ret = request.user.is_authenticated
    print(ret)

    # ret = request.user.is_authenticated()
    # print(ret)

    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')


def register(request):
    from django.contrib.auth.models import User
    # User.objects.create_user(username='htz', password='htz123')

    user_obj = User.objects.create_user(username='htz1', password='htz123')

    # 检查密码
    ret = user_obj.check_password('htz123')
    print(ret)

    # 修改密码
    user_obj.set_password('htz1234')
    user_obj.save()

    return HttpResponse('ojbk')


'''
如果扩展自带的auth_user表
'''