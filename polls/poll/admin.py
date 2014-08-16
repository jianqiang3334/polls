from django.contrib import admin

# Register your models here.
from poll.models import Poll,Choice,Upload

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Upload)

