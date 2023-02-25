from django.shortcuts import render ,redirect 
from django.contrib.auth import logout , login  , authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request): 
    logout(request)
    return redirect('index.html')

def register(request): 
    "Register a new users. "
    if request.method =='POST': 
        form = UserCreationForm(data = request.POST)
        if form.is_valid(): 
            new_user = form.save() 

    # log the user in and then redirect to home page 
            authenticated_user = authenticate(username = new_user.username , password = request.POST['password1'])
            login(request, authenticated_user)
            return redirect('index.html')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request , 'users/register.html', context)