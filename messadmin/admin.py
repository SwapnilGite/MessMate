from django.contrib import admin
from .models import MessAdmin,Menu,MealRecord,Bill
# Register your models here.
admin.site.register(MessAdmin)
admin.site.register(Menu)
admin.site.register(MealRecord)
admin.site.register(Bill)