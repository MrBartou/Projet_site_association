from django.contrib import admin
from .models import Administrators, Events, Partnership, Subsciption

admin.site.register(Events)
admin.site.register(Partnership)
admin.site.register(Subsciption)
admin.site.register(Administrators)