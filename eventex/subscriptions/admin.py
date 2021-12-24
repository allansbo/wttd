from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'phone', 'cpf', 'created_at')

    list_display = fields
    date_hierarchy = 'created_at'
    search_fields = fields
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
