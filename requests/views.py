from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AccountRequest
from django.contrib.auth.models import User
from .forms import AccountRequestForm
from users.utils import isAdminUser, generatePassword
from utils.utils import paginateItems
from django.core.mail import send_mail
from django.conf import settings

def RequestAccount(request):
    
    if request.user.is_authenticated:
        return redirect('users')
    
    page = 'request'
    form = AccountRequestForm()
    
    if request.method == 'POST':
        form = AccountRequestForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'users/thank_you.html')
    
    context = { 'page':page, 'form':form}
    
    return render(request, 'users/login_request.html', context)

@login_required(login_url="login")
def AccountRequests(request):
    
    is_admin = isAdminUser(request)
    requests = AccountRequest.objects.all()
    total = AccountRequest.objects.count()
    
    custom_range, requests = paginateItems(request, requests, 10)
    
    context = {
        'is_admin': is_admin, 
        'requests':requests,
        'total_requests': total,
        'custom_range': custom_range, 
    }
    
    return render(request, 'requests/requests.html', context)




@login_required(login_url="login")
def SingleAccountRequest(request, pk):
    
    """ check if the user is an administrator """
    
    is_admin = isAdminUser(request)
    
    """ retrieve the account request object and total requests """   
    
    accountRequest = AccountRequest.objects.get(id=pk)
    total = AccountRequest.objects.count()
    
    if request.method == 'POST':
        
        if request.POST['choice'] == 'accept':
            
            # generate a random 8 character password
            genPassword = generatePassword()
            
            # create a user account from request account object with generated password
            user = User.objects.create_user(
                username=accountRequest.username,
                email=accountRequest.email,
                password=genPassword
            )
            
            user.save()
            accountRequest.delete()
            
            subject = 'MECDM Projects Portal account created'
            message = 'Hi ' + user.first_name + ',\n\nYou can log in to the system with your username and password:\n\nUsername: '+user.username+'Password: '+genPassword+'\n\nRegards,\nMECDM Projects Team'

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            
            messages.success(request,'New user added to the system.')
            
        
        # elif request.POST['choice'] == 'Reject':
        #     accountRequest.delete()
        #     return redirect('users')
    
    # context = {
    #     'is_admin':is_admin,
    #     'account_request':accountRequest, 
    #     'total_requests': total 
    # }
    return redirect('account-requests')
    
    #return render(request, 'users/request.html', context)
