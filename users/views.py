from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import MyUserCreationForm,MyAuthenticationForm
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('movies:movies'))

def register(request):
    if request.method != 'POST':
        form = MyUserCreationForm()
    else:
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('movies:movies'))
    context = {'form':form}
    return render(request,'users/register.html',context)

class MyLoginView(LoginView):
    form_class = MyAuthenticationForm