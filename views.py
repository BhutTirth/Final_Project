# views.py
from django.shortcuts import render, redirect
from .models import Dev

def dev_login(request):
    error = None
    if request.method == 'POST':
        dev_username = request.POST['dev_username']
        dev_password = request.POST['dev_password']

        # Check if credentials match
        try:
            dev_user = Dev.objects.get(dev_username=dev_username, dev_password=dev_password)
            request.session['dev_id'] = dev_user.id  # Store dev login in session
            return redirect('user_management')  # Redirect to developer panel
        except Dev.DoesNotExist:
            error = "Invalid developer credentials"

    return render(request, 'dev_login.html', {'error': error})
