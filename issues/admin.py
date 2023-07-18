from django.contrib import admin

# Register your models here.

from .models import Issue, Status, Priority

admin.site.register(Issue)
# admin.site.register(Status)
# admin.site.register(Priority)