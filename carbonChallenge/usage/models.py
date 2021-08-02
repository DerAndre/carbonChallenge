from django.db import models
from django.contrib.auth.models import User


class Usage(models.Model):
    """
    The usage model describes a users personal carbon usage
    """
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usage_type = models.ForeignKey('UsageType', on_delete=models.CASCADE)
    usage_at = models.DateTimeField(auto_now=False, null=True)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.id} - {self.usage_type.name}'

    class Meta:
        verbose_name = 'Usage'
        verbose_name_plural = 'Usages'


class UsageType(models.Model):
    """
    The usage type model describes the type a usage object can have
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    unit = models.CharField(max_length=5, null=False)
    factor = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        verbose_name = 'UsageType'
        verbose_name_plural = 'UsageTypes'
