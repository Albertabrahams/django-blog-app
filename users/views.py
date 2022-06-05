from django.shortcuts import render, redirect
from django.contrib.auth import logout,login
from .forms import  UserForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from django.contrib.auth.decorators import login_required

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')

def register(request):
    
    form_user = UserForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)

        if form_user.is_valid():
            user = form_user.save()

            login(request, user)
            return redirect ('home')

    context = {
        'form_user' : form_user,
    }

    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    
    return render(request, 'users/login.html', {'form':form})

@login_required(login_url="/users/login/")
def profile(request, id):
    user = Profile.objects.get(id=id)
    form = ProfileForm(instance=user)
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            comment = form.save()
            comment.username_id = user.id
            comment.save()
            return redirect("profile", id)
    context = { 'form':form,
                'user': user}

    return render(request, 'users/profile.html', context)
