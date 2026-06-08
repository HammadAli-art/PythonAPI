from django.contrib import admin
from .models import Machine


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'status',
        'production_rate',
        'working_hours',
        'temperature',
        'machine_health',
        'target_production',
        'total_production',
        'efficiency',
    )

    search_fields = ('name',)

    list_filter = ('status',)