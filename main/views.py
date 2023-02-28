from django.shortcuts import render
from django.shortcuts import render, redirect
from main.models import MyUser, UserInfo
from main.forms import UserForm, UserUpdateForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "main/homepage.html")

def about(response):
    return render(response, "main/about.html", {})

def opport(response):
    return render(response, "main/opport.html", {})

def opportExc(response):
    return render(response, "main/opportExc.html", {})

def opportUniv(response):
    return render(response, "main/opportUniv.html", {})

def profile(request):
    if request.user.is_authenticated:
        currentUser = request.user
        user = MyUser.objects.get(pk = currentUser.id)

        return render(request, "main/profile.html", {"name": user.name, "birthday": user.date_of_birth, "school": user.school})

    return render(request, "main/login.html")

def edit(request):
    if request.method == "POST":
        info = UserInfo.objects.get(user_id = request.user.user_id)
        user_form = UserUpdateForm(request.POST, instance=info)

        print(user_form)

        if user_form.is_valid():
            user_form.save()

            return render(request, "main/profile.html", {})
        else:
            return render(request, "main/profile.html", {})
    else:
        user = UserInfo.objects.get(user_id = request.user.user_id)

        return render(request, "main/edit.html", {"info": user})

def company1(response):
    return render(response, "main/comp.html", {})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid() and form.clean():
            user = MyUser.objects.create_user(
                form.cleaned_data['user_id'],
                form.cleaned_data['name'],
                form.cleaned_data['date_of_birth'],
                form.cleaned_data['school'],
                form.cleaned_data['password'],
            )

            user.save()

            UserInfo(user_id = form.cleaned_data['user_id'], name = form.cleaned_data['name']).save()

            return redirect('login')

        else:
            messages.info(request, "All fields are required.")
            return render(request, 'main/signup.html')

    return render(request,'main/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        user = auth.authenticate(request, username=username, password=password)

        print(user)

        if user is not None:
            print("Aaa")
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect.")
            return render(request, 'main/login.html')

    else:
        return render(request, 'main/login.html')

def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return redirect('home')
    return render(request,'main/signup.html')
