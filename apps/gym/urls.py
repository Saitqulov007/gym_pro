from django.urls import path

from .views.main import AddNewGymEquipmentView, EquipmentView, UpdatePlanView, home, PlansView, AddSubscriptionView, \
    AddNewPlanView, ArchivePlanView, get_plan_days, cancel_subscription, remove_equipment
from .views.statistics import statistics

urlpatterns = [
    path('', home, name='dashboard'),
    path('add-subscription/', AddSubscriptionView.as_view(), name='add-subscription'),
    path('add-subscription/<int:pk>/', AddSubscriptionView.as_view(), name='add-subscription-registration'),
    path('subscriptions/<int:sub_id>/cancel/', cancel_subscription, name='cancel-subscription'),
    path('equipment/', EquipmentView.as_view(), name='equipment'),
    path('equipment/add', AddNewGymEquipmentView.as_view(), name='add-equipment'),
    path('equipment/<int:pk>/delete', remove_equipment, name='delete-equipment'),
    path('add-plan/', AddNewPlanView.as_view(), name='add-plan'),
    path('plans/', PlansView.as_view(), name='plans'),
    path('plans/<int:plan_id>/days/', get_plan_days, name='get-plan-days'),
    path('plans/<int:pk>/archive/', ArchivePlanView.as_view(), name='archive-plan'),
    path('plans/<int:pk>/update/', UpdatePlanView.as_view(), name='update-plan'),
    path('statistics/', statistics, name="statistics"),
]
