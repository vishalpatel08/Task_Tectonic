from django.shortcuts import get_object_or_404, render, redirect

from bnpl.models import Item, Orders, User

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        itemid = request.POST.get('itemid')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        new_Item = Item(name=name, itemid=itemid, quantity=quantity, price=price)
        new_Item.save()
        return redirect('/')
        pass
    else:
        items = Item.objects.all()
        return render(request, 'bnplhome.html', {'items':items})
    
def buy(request):
    if request.method == 'POST':
        itemid = request.POST.get('itemid')
        quantity = request.POST.get('quantity')
        payment = request.POST.get('payment')

        try:
            item1 = get_object_or_404(Item, itemid=itemid)
            if payment == "1":
                if(int(quantity)<item1.quantity):
                    item1.quantity -= int(quantity)
                    item1.save()
                else:
                    item1.quantity = 0
                    item1.save()
                    item1.delete()
                
                orderid = itemid+"11"
                userid = "user123"
                new_order = Orders(orderid=orderid, userid=userid, name=item1.name, itemid=itemid, quantity=quantity, price=item1.price)
                new_order.save()
                return redirect('/')
            else:
                user = get_object_or_404(User, userid="user123")
                if user.credits >= quantity*item1.price:
                    if(int(quantity)<item1.quantity):
                        item1.quantity -= int(quantity)
                        item1.save()
                    else:
                        item1.quantity = 0
                        item1.save()
                        item1.delete()
                    orderid = itemid+"11"
                    userid = "user123"
                    new_order = Orders(orderid=orderid, userid=userid, name=item1.name, itemid=itemid, quantity=quantity, price=item1.price)
                    new_order.save()
                    user.credits -= item1.price
                    user.save()
                    return redirect('/')
                else :
                    redirect("/")
        except:
            pass
            # return redirect("/admin")
    else:
        return render(request, 'bnplbuy.html')