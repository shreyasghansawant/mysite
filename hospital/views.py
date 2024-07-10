from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def dashboard_view(request):
    patients = CustomUser.objects.filter(is_doctor=False)
    doctors = CustomUser.objects.filter(is_doctor=True)
    me = request.user

    context = {
        'patients': patients,
        'doctors': doctors,
        'me': me,
    }
    
    return render(request, 'dashboard.html', context)