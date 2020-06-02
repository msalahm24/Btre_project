from django.shortcuts import render,redirect
from django.contrib import messages , auth
from contacts.models import Contact
 ##### the default user model in django
from django.contrib.auth.models import User



def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user  is not None:
            auth.login(request,user)
            messages.success(request,'you are now  logged in ')
            return redirect('dashboard')
        else:
            messages.error(request,'user not found')
            return redirect('login')
    return render(request,'accounts/login.html')



def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        # password validation
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'This username already taken')
                return  redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This email already registered')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    # if you want to login user after register directly
                    #auth.login(request,user)
                    #messages.success(request,'loged in')
                    #return redirect('index')
                    user.save()
                    messages.success(request,'you are registered and you can login')
                    return redirect('login')

        else:
            messages.error(request,'Passwords does not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you are now logged out')
        return redirect('index')




def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contacts,
    }
    return render(request,'accounts/dashboard.html',context)
