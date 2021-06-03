from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login


def ownerLogin(request):
    MyUser = get_user_model()
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']

        user = authenticate(username=userName, password=password)

        if user is not None:
            if MyUser.objects.get(username=userName).is_admin and MyUser.objects.get(username=userName).is_staff:
                login(request, user)
                return redirect("/owner/account/menu")
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect("/owner")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("/owner")
    else:
        return render(request, 'ownerlogin/admin_login.html')


