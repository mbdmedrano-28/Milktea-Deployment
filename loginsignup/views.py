from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login


def loginPage(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']

        user = authenticate(username=userName, password=password)

        if user is not None:
            login(request, user)
            return redirect("user/home")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("/")

    else:
        return render(request, 'loginsignup/login_page.html')


def signupPage(request):
    MyUser = get_user_model()
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        emailAdd = request.POST['emailAdd']
        mobileNo = request.POST['mobileNo']
        homeAdd = request.POST['homeAdd']
        userName = request.POST['userName']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if firstName == "" or lastName == "" or emailAdd == "" or mobileNo == "" or homeAdd == "" or userName == "" or password == "" or confirmation == "":
            messages.info(request, 'Complete All the Information')
            return redirect('/signup')
        if password == confirmation:
            if MyUser.objects.filter(username=userName).exists():
                messages.info(request, 'Username Taken')
                return redirect('/signup')
            elif MyUser.objects.filter(email=emailAdd).exists():
                messages.info(request, 'Email Taken')
                return redirect('/signup')
            elif MyUser.objects.filter(password=password).exists():
                messages.info(request, 'Password Taken')
                return redirect('/signup')
            elif len(mobileNo) != 11:
                messages.info(request, 'Invalid Contact Number')
                return redirect('/signup')
            else:
                user = MyUser.objects.create_user(first_name=firstName, last_name=lastName, email=emailAdd,
                                                mobile_no=mobileNo, home_add=homeAdd,
                                                username=userName, password=password)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'Password Do Not Match')
            return redirect('/signup')

    else:
        return render(request, 'loginsignup/signup_page.html')


def aboutPage(request):
    return render(request, 'loginsignup/about_page.html')