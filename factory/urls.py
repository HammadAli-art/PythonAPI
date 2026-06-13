from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (

    MachineViewSet,

    dashboard,

    all_machines,
    running_machines,
    stopped_machines,
    maintenance_machines,

    temperature_monitoring,
    machine_health,
    production_analysis,

    backend_portal
)

router = DefaultRouter()

router.register(
    r'machines',
    MachineViewSet
)

urlpatterns = [

    # BACKEND PORTAL

    path(
        '',
        backend_portal,
        name='backend_portal'
    ),

    # FRONTEND DASHBOARD

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    # FILTERS

    path(
        'all/',
        all_machines,
        name='all_machines'
    ),

    path(
        'running/',
        running_machines,
        name='running_machines'
    ),

    path(
        'stopped/',
        stopped_machines,
        name='stopped_machines'
    ),

    path(
        'maintenance/',
        maintenance_machines,
        name='maintenance_machines'
    ),

    # CHARTS

    path(
        'temperature/',
        temperature_monitoring,
        name='temperature_monitoring'
    ),

    path(
        'health/',
        machine_health,
        name='machine_health'
    ),

    path(
        'production/',
        production_analysis,
        name='production_analysis'
    ),

    # API

    path(
        'api/',
        include(router.urls)
    ),
]