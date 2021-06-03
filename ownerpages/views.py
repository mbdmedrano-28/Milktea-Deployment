from datetime import date
from django.shortcuts import render, redirect
from pages.models import Drink, Orders
from .models import Slot, Sales
from django.contrib import messages
from django.contrib.auth.models import auth


def editMenu(request):
    drinks = Drink.objects.all()
    if request.method == 'POST':
        if 'item1' in request.POST:
            offer1 = Drink.objects.get(id=1)
            offer1.offer = True
            offer1.save()
        else:
            offer1 = Drink.objects.get(id=1)
            offer1.offer = False
            offer1.save()

        if 'item2' in request.POST:
            offer2 = Drink.objects.get(id=2)
            offer2.offer = True
            offer2.save()
        else:
            offer2 = Drink.objects.get(id=2)
            offer2.offer = False
            offer2.save()

        if 'item3' in request.POST:
            offer3 = Drink.objects.get(id=3)
            offer3.offer = True
            offer3.save()
        else:
            offer3 = Drink.objects.get(id=3)
            offer3.offer = False
            offer3.save()

        if 'item4' in request.POST:
            offer4 = Drink.objects.get(id=4)
            offer4.offer = True
            offer4.save()
        else:
            offer4 = Drink.objects.get(id=4)
            offer4.offer = False
            offer4.save()

        if 'item5' in request.POST:
            offer5 = Drink.objects.get(id=5)
            offer5.offer = True
            offer5.save()
        else:
            offer5 = Drink.objects.get(id=5)
            offer5.offer = False
            offer5.save()

        if 'item6' in request.POST:
            offer6 = Drink.objects.get(id=6)
            offer6.offer = True
            offer6.save()
        else:
            offer6 = Drink.objects.get(id=6)
            offer6.offer = False
            offer6.save()

        if 'item7' in request.POST:
            offer7 = Drink.objects.get(id=7)
            offer7.offer = True
            offer7.save()
        else:
            offer7 = Drink.objects.get(id=7)
            offer7.offer = False
            offer7.save()

        if 'item8' in request.POST:
            offer8 = Drink.objects.get(id=8)
            offer8.offer = True
            offer8.save()
        else:
            offer8 = Drink.objects.get(id=8)
            offer8.offer = False
            offer8.save()

        if 'item9' in request.POST:
            offer9 = Drink.objects.get(id=9)
            offer9.offer = True
            offer9.save()
        else:
            offer9 = Drink.objects.get(id=9)
            offer9.offer = False
            offer9.save()

        if 'item10' in request.POST:
            offer10 = Drink.objects.get(id=10)
            offer10.offer = True
            offer10.save()
        else:
            offer10 = Drink.objects.get(id=10)
            offer10.offer = False
            offer10.save()

        if 'item11' in request.POST:
            offer11 = Drink.objects.get(id=11)
            offer11.offer = True
            offer11.save()
        else:
            offer11 = Drink.objects.get(id=11)
            offer11.offer = False
            offer11.save()

        if 'item12' in request.POST:
            offer12 = Drink.objects.get(id=12)
            offer12.offer = True
            offer12.save()
        else:
            offer12 = Drink.objects.get(id=12)
            offer12.offer = False
            offer12.save()
        return render(request, 'ownerpages/editmenu_page.html', {'drinks': drinks, 'title': 'Edit Menu'})
    else:
        return render(request, 'ownerpages/editmenu_page.html', {'drinks': drinks, 'title': 'Edit Menu'})


def signOut(request):
    auth.logout(request)
    return redirect("/owner")


def inventoryPage(request):
    slots = Slot.objects.all()
    if request.method == 'POST':
        slot1 = Slot.objects.get(id=1)
        slot2 = Slot.objects.get(id=2)
        slot3 = Slot.objects.get(id=3)
        slot4 = Slot.objects.get(id=4)
        slot5 = Slot.objects.get(id=5)
        slot6 = Slot.objects.get(id=6)
        slot7 = Slot.objects.get(id=7)
        slot8 = Slot.objects.get(id=8)
        slot9 = Slot.objects.get(id=9)
        slot10 = Slot.objects.get(id=10)

        nameType1 = request.POST['nameType1']
        nameType2 = request.POST['nameType2']
        nameType3 = request.POST['nameType3']
        nameType4 = request.POST['nameType4']
        nameType5 = request.POST['nameType5']
        nameType6 = request.POST['nameType6']
        nameType7 = request.POST['nameType7']
        nameType8 = request.POST['nameType8']
        nameType9 = request.POST['nameType9']
        nameType10 = request.POST['nameType10']

        quanType1 = request.POST['quanType1']
        quanType2 = request.POST['quanType2']
        quanType3 = request.POST['quanType3']
        quanType4 = request.POST['quanType4']
        quanType5 = request.POST['quanType5']
        quanType6 = request.POST['quanType6']
        quanType7 = request.POST['quanType7']
        quanType8 = request.POST['quanType8']
        quanType9 = request.POST['quanType9']
        quanType10 = request.POST['quanType10']

        unitType1 = request.POST['unitType1']
        unitType2 = request.POST['unitType2']
        unitType3 = request.POST['unitType3']
        unitType4 = request.POST['unitType4']
        unitType5 = request.POST['unitType5']
        unitType6 = request.POST['unitType6']
        unitType7 = request.POST['unitType7']
        unitType8 = request.POST['unitType8']
        unitType9 = request.POST['unitType9']
        unitType10 = request.POST['unitType10']

        slot1.name_unique = nameType1
        if quanType1 == "":
            slot1.quantity_unique = 0
        else:
            slot1.quantity_unique = quanType1
        slot1.unit_unique = unitType1
        slot1.save()

        slot2.name_unique = nameType2
        if quanType2 == "":
            slot2.quantity_unique = 0
        else:
            slot2.quantity_unique = quanType2
        slot2.unit_unique = unitType2
        slot2.save()

        slot3.name_unique = nameType3
        if quanType3 == "":
            slot3.quantity_unique = 0
        else:
            slot3.quantity_unique = quanType3
        slot3.unit_unique = unitType3
        slot3.save()

        slot4.name_unique = nameType4
        if quanType4 == "":
            slot4.quantity_unique = 0
        else:
            slot4.quantity_unique = quanType4
        slot4.unit_unique = unitType4
        slot4.save()

        slot5.name_unique = nameType5
        if quanType5 == "":
            slot5.quantity_unique = 0
        else:
            slot5.quantity_unique = quanType5
        slot5.unit_unique = unitType5
        slot5.save()

        slot6.name_unique = nameType6
        if quanType6 == "":
            slot6.quantity_unique = 0
        else:
            slot6.quantity_unique = quanType6
        slot6.unit_unique = unitType6
        slot6.save()

        slot7.name_unique = nameType7
        if quanType7 == "":
            slot7.quantity_unique = 0
        else:
            slot7.quantity_unique = quanType7
        slot7.unit_unique = unitType7
        slot7.save()

        slot8.name_unique = nameType8
        if quanType8 == "":
            slot8.quantity_unique = 0
        else:
            slot8.quantity_unique = quanType8
        slot8.unit_unique = unitType8
        slot8.save()

        slot9.name_unique = nameType9
        if quanType9 == "":
            slot9.quantity_unique = 0
        else:
            slot9.quantity_unique = quanType9
        slot9.unit_unique = unitType9
        slot9.save()

        slot10.name_unique = nameType10
        if quanType10 == "":
            slot10.quantity_unique = 0
        else:
            slot10.quantity_unique = quanType10
        slot10.unit_unique = unitType10
        slot10.save()

        return render(request, 'ownerpages/inventory_page.html', {'slots': slots, 'title': 'Inventory'})
    else:
        return render(request, 'ownerpages/inventory_page.html', {'slots': slots, 'title': 'Inventory'})


def ordersPage(request):
    global orders
    orders = list(Orders.objects.all().order_by('id'))
    orders = orders[0:5]
    for x in orders:
        print(str(x)+"\n")
    if request.method == 'POST':
        if 'save1' in request.POST:
            status1 = request.POST['statusValue1']
            if status1 == "":
                messages.info(request, 'Input an Order Status')
                return redirect('/owner/account/orders')
            else:
                orders[0].status = status1
                for x in orders:
                    x.save()
                return redirect('/owner/account/orders')
        if 'completed1' in request.POST:
            if Sales.objects.filter(today_date=date.today()).exists():
                new_sale = Sales.objects.get(today_date=date.today()).today_sale + orders[0].price
                Sales.objects.filter(today_date=date.today()).update(today_sale=new_sale)
                Sales.objects.get(today_date=date.today()).save()
                orders[0].delete()
                return redirect('/owner/account/orders')
            else:
                Sales.objects.create(today_date=date.today(), today_sale=orders[0].price)
                orders[0].delete()
                return redirect('/owner/account/orders')
        if 'save2' in request.POST:
            status2 = request.POST['statusValue2']
            if status2 == "":
                messages.info(request, 'Input an Order Status')
                return redirect('/owner/account/orders')
            else:
                orders[1].status = status2
                for x in orders:
                    x.save()
                return redirect('/owner/account/orders')
        if 'completed2' in request.POST:
            if Sales.objects.filter(today_date=date.today()).exists():
                new_sale = Sales.objects.get(today_date=date.today()).today_sale + orders[1].price
                Sales.objects.filter(today_date=date.today()).update(today_sale=new_sale)
                Sales.objects.get(today_date=date.today()).save()
                orders[1].delete()
                return redirect('/owner/account/orders')
            else:
                Sales.objects.create(today_date=date.today(), today_sale=orders[1].price)
                orders[1].delete()
                return redirect('/owner/account/orders')
        if 'save3' in request.POST:
            status3 = request.POST['statusValue3']
            if status3 == "":
                messages.info(request, 'Input an Order Status')
                return redirect('/owner/account/orders')
            else:
                orders[2].status = status3
                for x in orders:
                    x.save()
                return redirect('/owner/account/orders')
        if 'completed3' in request.POST:
            if Sales.objects.filter(today_date=date.today()).exists():
                new_sale = Sales.objects.get(today_date=date.today()).today_sale + orders[2].price
                Sales.objects.filter(today_date=date.today()).update(today_sale=new_sale)
                Sales.objects.get(today_date=date.today()).save()
                orders[2].delete()
                return redirect('/owner/account/orders')
            else:
                Sales.objects.create(today_date=date.today(), today_sale=orders[2].price)
                orders[2].delete()
                return redirect('/owner/account/orders')
        if 'save4' in request.POST:
            status4 = request.POST['statusValue4']
            if status4 == "":
                messages.info(request, 'Input an Order Status')
                return redirect('/owner/account/orders')
            else:
                orders[3].status = status4
                for x in orders:
                    x.save()
                return redirect('/owner/account/orders')
        if 'completed4' in request.POST:
            if Sales.objects.filter(today_date=date.today()).exists():
                new_sale = Sales.objects.get(today_date=date.today()).today_sale + orders[3].price
                Sales.objects.filter(today_date=date.today()).update(today_sale=new_sale)
                Sales.objects.get(today_date=date.today()).save()
                orders[3].delete()
                return redirect('/owner/account/orders')
            else:
                Sales.objects.create(today_date=date.today(), today_sale=orders[3].price)
                orders[3].delete()
                return redirect('/owner/account/orders')
        if 'save5' in request.POST:
            status5 = request.POST['statusValue5']
            if status5 == "":
                messages.info(request, 'Input an Order Status')
                return redirect('/owner/account/orders')
            else:
                orders[4].status = status5
                for x in orders:
                    x.save()
                return redirect('/owner/account/orders')
        if 'completed5' in request.POST:
            if Sales.objects.filter(today_date=date.today()).exists():
                new_sale = Sales.objects.get(today_date=date.today()).today_sale + orders[4].price
                Sales.objects.filter(today_date=date.today()).update(today_sale=new_sale)
                Sales.objects.get(today_date=date.today()).save()
                orders[4].delete()
                return redirect('/owner/account/orders')
            else:
                Sales.objects.create(today_date=date.today(), today_sale=orders[4].price)
                orders[4].delete()
                return redirect('/owner/account/orders')

    else:
        return render(request, 'ownerpages/checkorder_page.html', {'orders': orders, 'title': 'Orders'})


def salesPage(request):
    sales = Sales.objects.all()
    return render(request, 'ownerpages/sales_page.html', {'sales': sales, 'title': 'Daily Sales'})
