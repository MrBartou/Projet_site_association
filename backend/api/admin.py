from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import *

admin.site.register(Event)
admin.site.register(PartnershipType)
admin.site.register(Partnership)
admin.site.register(Subscription)
