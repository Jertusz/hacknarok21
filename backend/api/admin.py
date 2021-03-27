from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(ActivityLog)
admin.site.register(SessionLog)
