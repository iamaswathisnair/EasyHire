from django.contrib import admin
from .models import reg
from .models import Jobposting 
from .models import workerreg1,Complaints,Gallery,Feedback,Workerbooking
# Register your models here.

admin.site.register(reg)
admin.site.register(Jobposting)
admin.site.register(workerreg1)
admin.site.register(Complaints)
admin.site.register(Feedback)
admin.site.register(Workerbooking)
admin.site.register(Gallery)


