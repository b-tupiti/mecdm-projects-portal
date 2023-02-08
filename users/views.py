from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from requests.models import AccountRequest
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .utils import isAdminUser, generatePassword
from utils.utils import paginateItems

# temporary home view
def home(request):
    is_admin = isAdminUser(request)
    total = AccountRequest.objects.count()
    context = {'is_admin':is_admin, 'total_requests':total}
    return render(request, 'home.html', context)

def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    page = 'login'
    context = { 'page':page}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_request.html', context)


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'User was logged out!')
    return redirect('login')






@login_required(login_url="login")
def Users(request):
    
    is_admin = isAdminUser(request)
    requests = AccountRequest.objects.all()
    users = UserProfile.objects.all()
    total_requests = AccountRequest.objects.count()
    total_users = UserProfile.objects.count()
    
    users_forms = []
    for user in users:
        form = UserProfileForm(instance=user)
        users_forms.append({'user': user, 'form':form})

    custom_range, users = paginateItems(request, users, 10)
    
    form = UserProfileForm()
    context = {
        'is_admin': is_admin, 
        'users': users,
        'requests':requests,
        'total_requests': total_requests,
        'total_users': total_users,
        'custom_range': custom_range,
        'users_forms': users_forms,
        'form': form
    }
    
    return render(request, 'users/users.html', context)
    


def SingleUser(request, pk):
    return render(request, 'users/users.html')

@login_required(login_url="login")
def AddUser(request):
    
    if isAdminUser(request) == False:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have added a new account: ')
            return redirect('users')
    return render(request, 'users/users.html')



@login_required(login_url="login")
def EditUser(request,pk):
   
    if isAdminUser(request) == False:
        return redirect('home')
    
    if request.method == 'POST':
        user  = UserProfile.objects.get(id=pk)
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully updated user account: ' + user.username)
            return redirect('users')
    
    return redirect('users')


@login_required(login_url="login")
def DeleteUser(request, pk):
    
    if isAdminUser(request) == False:
        return redirect('home')
    
    if request.method == 'POST':
        profile = UserProfile.objects.get(id=pk)
        profile.delete()
        messages.success(request, 'You have successfully deleted user: '+profile.username+'')
        obj = {'message': 'successful deletion'}
        return JsonResponse(obj)
    
    return redirect('users')


