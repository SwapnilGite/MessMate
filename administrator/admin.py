from django.contrib import admin
from .models import Mess
from .models import Feedback
from .models import Transaction
# Register your models here.
admin.site.register(Mess)
admin.site.register(Feedback)
admin.site.register(Transaction)


