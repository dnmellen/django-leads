import csv
from django.contrib import admin
from django.http import HttpResponse
from . import get_register_model, get_register_model_admin


class RegisterAdmin(admin.ModelAdmin):
    fields = ['email', 'name', 'created_on', 'modified_on']
    readonly_fields = ('created_on', 'modified_on')
    list_display = ('email', 'created_on')
    list_filter = ['created_on']
    search_fields = ['name', 'email']
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        """
        Action to export leads to CSV
        """

        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=leads.csv'
        writer = csv.writer(response)
        field_names = [field for field in self.fields]
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field, '') for field in field_names])
        return response

    export_to_csv.short_description = "Export selected objects as csv file"


admin.site.register(get_register_model(), get_register_model_admin())
