from django.contrib import admin
from bnpl.models import Item, User, Orders
# Register your models here.

admin.site.register(Item)
admin.site.register(User)
admin.site.register(Orders)