from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users')
        else :
            return render(request, 'new_user.html', {'reg_form': form})
    else:
        form = UserCreationForm()
        registration =  {'reg_form': form}
        return render(request, 'new_user.html', registration)