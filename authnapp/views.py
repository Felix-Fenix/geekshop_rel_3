from re import T
from django.conf import settings
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse

from authnapp.forms import ShopUserEditForm, ShopUserLoginForm, ShopUserRegisterForm
from .utils import send_verify_mail
from .models import ShopUser
# from .forms import sa


def login(request):
    title = "вход"

    login_form = ShopUserLoginForm(data=request.POST or None)
    next_page = request.GET["next"] if "next" in request.GET.keys() else ""

    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if "next_page" in request.POST.keys():
                return HttpResponseRedirect(request.POST["next_page"])
            return HttpResponseRedirect(reverse("main"))

    content = {"title": title, "login_form": login_form, "next_page": next_page}
    return render(request, "authnapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


def register(request):
    title = "регистрация"

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        print('}}}}}}}}}}}')
        if register_form.is_valid():
            print(11111111111111111)
            user = register_form.save()
            print(user, '&&&&&&&&&&&&&&&&&&&&&')

            send_verify_mail(user)
            return HttpResponseRedirect(reverse("auth:login"))
    register_form = ShopUserRegisterForm()
    content = {"title": title, "register_form": register_form}
    return render(request, "authnapp/register.html", content)


def edit(request):
    title = "редактирование"

    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    edit_form = ShopUserEditForm(instance=request.user)
    content = {"title": title, "edit_form": edit_form, "media_url": settings.MEDIA_URL}
    return render(request, "authnapp/edit.html", content)


def verify(request, email, activation_key):
    print(email,'------', activation_key)
    user = get_object_or_404(ShopUser, email=email)
    print(user.activation_key, '+++++++')
    if user.activation_key == activation_key:
        
        user.is_active = True
        user.save()
        auth.login(request, user)
        return render(request, 'authnapp/verification.html')