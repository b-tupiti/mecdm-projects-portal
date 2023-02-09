from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from users.utils import isAdminUser
from django.shortcuts import redirect

@login_required(login_url='login')
def Projects(request):
    
    if not isAdminUser(request):
        return redirect('home')
    
    context = {}
    
    return render(request,'projects/projects.html', context)