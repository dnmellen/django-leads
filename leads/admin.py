import csv
from django.core.mail import EmailMultiAlternatives, get_connection
from django.contrib import admin
from django.http import HttpResponse
from . import get_register_model, get_register_model_admin
from .models import Newsletter


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


class NewsletterAdmin(admin.ModelAdmin):
    fields = ['subject', 'from_name', 'from_address', 'html_file']
    readonly_fields = ('created_on', 'modified_on')
    list_display = ('created_on')
    list_filter = ['created_on']
    search_fields = ['subject']
    actions = ['send']

    def send(self, request, queryset):
        """
        Action to send the current newsletter to all registered users
        """
        connection = get_connection()
        body = self.html_file.read()
        msg = EmailMultiAlternatives(subject=self.subject,
                                     body='',
                                     from_email=u"{from_name} <{from_email}>".format(from_name=self.from_name,
                                                                                     from_email=self.from_address))
        msg.attach_alternative(body, "text/html")

        def get_emails():
            for obj in get_register_model().objects.all():
                msg.to = obj.email
                yield msg

        connection.send_messages(get_emails())

    send.short_description = "Send newsletter to all registered users"


admin.site.register(Newsletter, NewsletterAdmin)
