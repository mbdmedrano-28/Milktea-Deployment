from django.shortcuts import render, redirect
from .models import Drink, Cart, Orders
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import get_user_model, login


def homePage(request):
    return render(request, 'pages/home_page.html', {'title': 'Home'})


def menuPage(request):
    if request.method == 'POST':
        if Cart.objects.filter(username=request.user.username).count() >= 5:
            messages.info(request, 'Your cart is full. Checkout an order first!')
            return redirect('/user/myCart')
        else:
            price_medium = request.POST.get('medium')
            price_large = request.POST.get('large')
            item_name = request.POST.get('name')
            return render(request, 'pages/size_page.html',
                          {'title': 'Choose Size', 'price_medium': price_medium, 'price_large': price_large,
                           'item_name': item_name})
    else:
        drinks = Drink.objects.all()
        return render(request, 'pages/menu_page.html', {'drinks': drinks, 'title': 'Menu'})


def accountPage(request):
    MyUser = request.user
    return render(request, 'pages/account_page.html', {'title': MyUser.first_name})


def sizePage(request):
    if request.method == 'POST':
        drink_name = request.POST['drink_name']
        quantity = request.POST['quantity']

        if quantity == "" or 'size' not in request.POST:
            messages.info(request, 'Invalid inputs! Order again')
            return redirect('/user/menu')
        else:
            quantity = request.POST['quantity']
            size = request.POST['size']
            quantity = int(quantity)
            item_ind = str("item" + str(Cart.objects.filter(username=request.user.username).count() + 1))
            item_check = str("itemCheck" + str(Cart.objects.filter(username=request.user.username).count() + 1))
            if size == 'Medium':
                price = request.POST['mediumPrice']
                price = int(price)
                total = price * quantity
                Cart.objects.create(username=request.user.username,
                                    item_name=drink_name,
                                    quantity=quantity,
                                    size=size,
                                    price=total,
                                    item_ind=item_ind,
                                    item_check=item_check)
            elif size == 'Large':
                price = request.POST['largePrice']
                price = int(price)
                total = price * quantity
                Cart.objects.create(username=request.user.username,
                                    item_name=drink_name,
                                    quantity=quantity,
                                    size=size,
                                    price=total,
                                    item_ind=item_ind,
                                    item_check=item_check)
            return redirect("/user/myCart/")

    else:
        return render(request, 'pages/size_page.html',
                      {'title': 'Choose Size'})


def cartPage(request):
    global items, item1, item2, item3, item4, item5
    orders = []
    if request.method == 'POST':
        items = list(Cart.objects.filter(username=request.user.username))
        if 'itemCheck1' not in request.POST and 'itemCheck2' not in request.POST and 'itemCheck3' not in request.POST and 'itemCheck4' not in request.POST and 'itemCheck5' not in request.POST:
            messages.info(request, 'Select at least one box')
            return redirect("/user/myCart")
        else:
            if 'remove' in request.POST:
                if 'itemCheck1' in request.POST:
                    items[0].delete()
                if 'itemCheck2' in request.POST:
                    items[1].delete()
                if 'itemCheck3' in request.POST:
                    items[2].delete()
                if 'itemCheck4' in request.POST:
                    items[3].delete()
                if 'itemCheck5' in request.POST:
                    items[4].delete()

            if 'checkout' in request.POST:
                if 'itemCheck1' in request.POST:
                    item1 = []
                    item1.append(request.POST['quantity1'])
                    item1.append(request.POST['flavor1'])
                    item1.append(request.POST['size1'])
                    item1.append(request.POST['price1'])
                    orders.append(item1)
                if 'itemCheck2' in request.POST:
                    item2 = []
                    item2.append(request.POST['quantity2'])
                    item2.append(request.POST['flavor2'])
                    item2.append(request.POST['size2'])
                    item2.append(request.POST['price2'])
                    orders.append(item2)
                if 'itemCheck3' in request.POST:
                    item3 = []
                    item3.append(request.POST['quantity3'])
                    item3.append(request.POST['flavor3'])
                    item3.append(request.POST['size3'])
                    item3.append(request.POST['price3'])
                    orders.append(item3)
                if 'itemCheck4' in request.POST:
                    item4 = []
                    item4.append(request.POST['quantity4'])
                    item4.append(request.POST['flavor4'])
                    item4.append(request.POST['size4'])
                    item4.append(request.POST['price4'])
                    orders.append(item4)
                if 'itemCheck5' in request.POST:
                    item5 = []
                    item5.append(request.POST['quantity5'])
                    item5.append(request.POST['flavor5'])
                    item5.append(request.POST['size5'])
                    item5.append(request.POST['price5'])
                    orders.append(item5)

                return render(request, 'pages/information_page.html', {'orders': orders, 'title': 'Information'})

            return redirect("/user/myCart/")
    else:
        items = Cart.objects.filter(username=request.user.username)
        return render(request, 'pages/cart_page.html', {'items': items, 'title': 'My Cart'})


def infoPage(request):
    global items
    if request.method == 'POST':
        items = list(Cart.objects.filter(username=request.user.username))
        name = request.POST['nameInput']
        contact = request.POST['numberInput']
        email = request.POST['emailInput']
        address = request.POST['addressInput']

        if 'mode' not in request.POST or name == "" or contact == "" or email == "" or address == "":
            messages.info(request, 'Invalid inputs! Try again')
            return redirect("/user/myCart/")
        else:
            mode = request.POST['mode']
            if 'element11' in request.POST:
                quantity1 = request.POST['element11']
                flavor1 = request.POST['element12']
                size1 = request.POST['element13']
                price1 = request.POST['element14']
                Orders.objects.create(name=name, contact=contact, email=email,
                                      address=address, mode=mode, quantity=quantity1,
                                      flavor=flavor1, size=size1, price=price1, status="Pending")
                Cart.objects.get(username=request.user.username, quantity=quantity1,
                                 item_name=flavor1, price=price1).delete()
            if 'element21' in request.POST:
                quantity2 = request.POST['element21']
                flavor2 = request.POST['element22']
                size2 = request.POST['element23']
                price2 = request.POST['element24']
                Orders.objects.create(name=name, contact=contact, email=email,
                                      address=address, mode=mode, quantity=quantity2,
                                      flavor=flavor2, size=size2, price=price2, status="Pending")
                Cart.objects.get(username=request.user.username, quantity=quantity2,
                                 item_name=flavor2, price=price2).delete()
            if 'element31' in request.POST:
                quantity3 = request.POST['element31']
                flavor3 = request.POST['element32']
                size3 = request.POST['element33']
                price3 = request.POST['element34']
                Orders.objects.create(name=name, contact=contact, email=email,
                                      address=address, mode=mode, quantity=quantity3,
                                      flavor=flavor3, size=size3, price=price3, status="Pending")
                Cart.objects.get(username=request.user.username, quantity=quantity3,
                                 item_name=flavor3, price=price3).delete()
            if 'element41' in request.POST:
                quantity4 = request.POST['element41']
                flavor4 = request.POST['element42']
                size4 = request.POST['element43']
                price4 = request.POST['element44']
                Orders.objects.create(name=name, contact=contact, email=email,
                                      address=address, mode=mode, quantity=quantity4,
                                      flavor=flavor4, size=size4, price=price4, status="Pending")
                Cart.objects.get(username=request.user.username, quantity=quantity4,
                                 item_name=flavor4, price=price4).delete()
            if 'element51' in request.POST:
                quantity5 = request.POST['element51']
                flavor5 = request.POST['element52']
                size5 = request.POST['element53']
                price5 = request.POST['element54']
                Orders.objects.create(name=name, contact=contact, email=email,
                                      address=address, mode=mode, quantity=quantity5,
                                      flavor=flavor5, size=size5, price=price5, status="Pending")
                Cart.objects.get(username=request.user.username, quantity=quantity5,
                                 item_name=flavor5, price=price5).delete()
            return redirect("/user/myOrder/")
    else:
        return render(request, 'pages/information_page.html', {'title': 'Information'})


def orderPage(request):
    orders = Orders.objects.filter(email=request.user.email)
    return render(request, 'pages/order_page.html', {'title': 'My Orders', 'orders': orders})


def signOut(request):
    auth.logout(request)
    return redirect("/")


def settingsPage(request):
    MyUser = request.user
    Accounts = get_user_model()
    if request.method == 'POST':
        firstName = request.POST['fnType']
        lastName = request.POST['lnType']
        username = request.POST['unType']
        currPass = request.POST['pValue']
        newPass = request.POST['pType']
        confirmPass = request.POST['confirmPType']
        emailAdd = request.POST['emailType']
        mobileNo = request.POST['numType']
        homeAdd = request.POST['addType']

        if firstName != "":
            MyUser.first_name = firstName
        if lastName != "":
            MyUser.last_name = lastName
        if username != "":
            if Accounts.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/user/myAccount/settings')
            else:
                Cart.objects.filter(username=MyUser.username).update(username=username)
                MyUser.username = username
        if emailAdd != "":
            if Accounts.objects.filter(email=emailAdd).exists():
                messages.info(request, 'Email Taken')
                return redirect('/user/myAccount/settings')
            else:
                Orders.objects.filter(email=MyUser.email).update(email=emailAdd)
                MyUser.email = emailAdd
        if mobileNo != "":
            if len(mobileNo) != 11:
                messages.info(request, 'Invalid Contact Number')
                return redirect('/user/myAccount/settings')
            else:
                MyUser.mobile_no = mobileNo
        if homeAdd != "":
            MyUser.home_add = homeAdd

        if currPass != "" and newPass != "" and confirmPass != "":
            if MyUser.check_password(currPass):
                if newPass == confirmPass:
                    if Accounts.objects.filter(password=newPass).exists():
                        messages.info(request, 'Password Taken')
                        return redirect('/user/myAccount/settings')
                    else:
                        MyUser.set_password(newPass)
                else:
                    messages.info(request, 'Passwords Do Not Match')
                    return redirect('/user/myAccount/settings')
            else:
                messages.info(request, 'Incorrect Current Password')
                return redirect('/user/myAccount/settings')
        elif (currPass == "" and (newPass != "" or confirmPass != "")) or (currPass != "" and (newPass == "" or confirmPass == "")):
            messages.info(request, "Incomplete password fields")
            return redirect('/user/myAccount/settings')

        MyUser.save()
        login(request, MyUser)
        return render(request, 'pages/account_page.html', {'title': MyUser.first_name})

    else:
        return render(request, 'pages/settings_page.html', {'title': MyUser.first_name})
