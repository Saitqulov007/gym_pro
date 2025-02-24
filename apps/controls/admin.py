from django.contrib import admin
from .models import Gym, GymPlan, GymSubscription, GymNotification

admin.site.register(Gym)
admin.site.register(GymPlan)
admin.site.register(GymSubscription)


@admin.register(GymNotification)
class GymNotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'gym', 'send_at']
