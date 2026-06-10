from django.shortcuts import render

from rest_framework import viewsets

from .models import Machine
from .serializers import MachineSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


def dashboard(request):

    machines = Machine.objects.all()

    total_machines = machines.count()

    running_machines = machines.filter(
        status='Running'
    ).count()

    stopped_machines = machines.filter(
        status='Stopped'
    ).count()

    avg_health = 0

    if total_machines > 0:

        avg_health = round(
            sum(
                machine.machine_health
                for machine in machines
            ) / total_machines,
            2
        )

    machine_names = [
        machine.name
        for machine in machines
    ]

    temperatures = [
        machine.temperature
        for machine in machines
    ]

    health_values = [
        machine.machine_health
        for machine in machines
    ]

    production_values = [
        machine.total_production()
        for machine in machines
    ]

    context = {

        'machines': machines,

        'total_machines': total_machines,

        'running_machines': running_machines,

        'stopped_machines': stopped_machines,

        'avg_health': avg_health,

        'machine_names': machine_names,

        'temperatures': temperatures,

        'health_values': health_values,

        'production_values': production_values,

    }

    return render(
        request,
        'factory/dashboard.html',
        context
    )