from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    MachineViewSet,
    dashboard
)

router = DefaultRouter()
router.register(r'machines', MachineViewSet)

urlpatterns = [

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        '',
        include(router.urls)
    ),
]