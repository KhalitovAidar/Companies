from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(OwnerCompany)
admin.site.register(Company)
admin.site.register(Stock)
admin.site.register(Reviews)