from django.db import models


class Machine(models.Model):

    MACHINE_STATUS = [
        ('Running', 'Running'),
        ('Stopped', 'Stopped'),
        ('Maintenance', 'Maintenance'),
    ]

    name = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=MACHINE_STATUS,
        default='Running'
    )

    production_rate = models.IntegerField(
        help_text="Items produced per hour"
    )

    working_hours = models.IntegerField()

    temperature = models.FloatField(
        default=0.0,
        help_text="Current machine temperature in °C"
    )

    machine_health = models.FloatField(
        default=100.0,
        help_text="Machine health score from 0 to 100"
    )

    target_production = models.IntegerField(
        default=0,
        help_text="Target number of items to be produced"
    )

    def total_production(self):
        return self.production_rate * self.working_hours

    def efficiency(self):
        max_output = 1000
        return round((self.total_production() / max_output) * 100, 2)

    def __str__(self):
        return self.name