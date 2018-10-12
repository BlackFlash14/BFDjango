from django.contrib import admin
from .models import Task, Owner, User
# Register your models here.
admin.site.register(Task)
admin.site.register(Owner)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')