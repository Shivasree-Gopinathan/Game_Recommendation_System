from django.contrib import admin
from .models import UserProfile
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'date_joined']
#     search_fields = ['username', 'email']
#     readonly_fields = ['date_joined']
#
# admin.site.register(User, UserAdmin)

admin.site.register(UserProfile)
