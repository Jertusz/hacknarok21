from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(ActivityLog)
admin.site.register(SessionLog)
admin.site.register(Log)
admin.site.register(CustomQuestion)
admin.site.register(CustomQuestionLog)
