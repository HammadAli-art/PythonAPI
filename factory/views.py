from django.shortcuts import render, redirect
from django.conf import settings

from rest_framework import viewsets

from .models import Machine
from .serializers import MachineSerializer


# ==================================================
# API VIEWSET
# ==================================================

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


# ==================================================
# COMMON DASHBOARD DATA
# ==================================================

def get_dashboard_context(machine_queryset):

    all_machines = Machine.objects.all()

    total_machines = all_machines.count()

    running_machines = all_machines.filter(
        status='Running'
    ).count()

    stopped_machines = all_machines.filter(
        status='Stopped'
    ).count()

    maintenance_machines = all_machines.filter(
        status='Maintenance'
    ).count()

    avg_health = 0

    if total_machines > 0:

        avg_health = round(
            sum(
                machine.machine_health
                for machine in all_machines
            ) / total_machines,
            2
        )

    context = {

        "machines": machine_queryset,

        "total_machines": total_machines,

        "running_machines": running_machines,

        "stopped_machines": stopped_machines,

        "maintenance_machines": maintenance_machines,

        "avg_health": avg_health,

        "machine_names": [
            machine.name
            for machine in all_machines
        ],

        "temperatures": [
            machine.temperature
            for machine in all_machines
        ],

        "health_values": [
            machine.machine_health
            for machine in all_machines
        ],

        "production_values": [
            machine.total_production()
            for machine in all_machines
        ]
    }

    return context


# ==================================================
# MAIN DASHBOARD
# ==================================================

def dashboard(request):

    context = get_dashboard_context(
        Machine.objects.none()
    )

    context["page_title"] = "Dashboard"

    return render(
        request,
        "factory/dashboard.html",
        context
    )


# ==================================================
# FILTERS
# ==================================================

def all_machines(request):

    context = get_dashboard_context(
        Machine.objects.all()
    )

    context["page_title"] = "All Machines"

    return render(
        request,
        "factory/all_machines.html",
        context
    )


def running_machines(request):

    context = get_dashboard_context(
        Machine.objects.filter(
            status='Running'
        )
    )

    context["page_title"] = "Running Machines"

    return render(
        request,
        "factory/all_machines.html",
        context
    )


def stopped_machines(request):

    context = get_dashboard_context(
        Machine.objects.filter(
            status='Stopped'
        )
    )

    context["page_title"] = "Stopped Machines"

    return render(
        request,
        "factory/all_machines.html",
        context
    )


def maintenance_machines(request):

    context = get_dashboard_context(
        Machine.objects.filter(
            status='Maintenance'
        )
    )

    context["page_title"] = "Maintenance Machines"

    return render(
        request,
        "factory/all_machines.html",
        context
    )


# ==================================================
# CHART PAGES
# ==================================================

def temperature_monitoring(request):

    context = get_dashboard_context(
        Machine.objects.all()
    )

    return render(
        request,
        "factory/temperature.html",
        context
    )


def machine_health(request):

    context = get_dashboard_context(
        Machine.objects.all()
    )

    return render(
        request,
        "factory/health.html",
        context
    )


def production_analysis(request):

    context = get_dashboard_context(
        Machine.objects.all()
    )

    return render(
        request,
        "factory/production.html",
        context
    )

def backend_portal(request):

    return render(
        request,
        "factory/backend_portal.html"
    )