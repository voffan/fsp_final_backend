from django.urls import path
from .views import NotificationView

urlpatterns = [
    path('', NotificationView.as_view({'get': 'list'})),
    path('<int:notification_id>/', NotificationView.as_view({'delete': 'delete'})),
]