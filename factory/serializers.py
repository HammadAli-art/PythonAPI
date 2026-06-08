from rest_framework import serializers
from .models import Machine


class MachineSerializer(serializers.ModelSerializer):

    total_production = serializers.SerializerMethodField()
    efficiency = serializers.SerializerMethodField()

    class Meta:
        model = Machine
        fields = [
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
        ]

    def get_total_production(self, obj):
        return obj.total_production()

    def get_efficiency(self, obj):
        return obj.efficiency()