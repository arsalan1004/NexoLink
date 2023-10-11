from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


# Home page Controller ( python view )
def home(request):
    # Getting records
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, Please try again!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


# Logout Controller ( python view )
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


# Register page Controller ( python view )
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

# Individual record Controller
def customer_records(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        messages.success(request, "Record tracked successfully!")
        return render(request, 'record.html', {'customer_records': record})
    messages.success(request, "You must be logged in to view records")
    return redirect('home')

# Adding Record Controller
def add_record(request):
    return render(request, 'add_record.html', {})

# Deleting Record Controller
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record Deleted Successfully.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete this record")
        return redirect('home')

