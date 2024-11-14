from django.contrib import admin
from .models import GoogleOAuthKeys

class GoogleOAuthKeyAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(GoogleOAuthKeys, GoogleOAuthKeyAdmin)
