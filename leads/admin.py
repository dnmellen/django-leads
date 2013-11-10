from django.contrib import admin
from . import get_register_model, get_register_model_admin


class RegisterAdmin(admin.ModelAdmin):
    fields = ['email', 'name', 'created_on', 'modified_on']
    readonly_fields = ('created_on', 'modified_on')
    list_display = ('email', 'created_on')
    list_filter = ['created_on']
    search_fields = ['name', 'email']

admin.site.register(get_register_model(), get_register_model_admin())
