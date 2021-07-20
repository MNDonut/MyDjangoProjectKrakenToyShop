from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to page login with its context(form)
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    
    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def home(request):
    return render(request, 'common/navbar.html')