import json

from django.core.management.base import BaseCommand
from usage.serializers import UsageTypeSerializer


class Command(BaseCommand):
    """
    Management command to initially create usage types
    """

    def handle(self, *args, **options):
        with open('carbonChallenge/usage_types.json') as json_file:
            usage_types = json.load(json_file)
        i = 0
        for usage_type in usage_types:
            serializer = UsageTypeSerializer(data=usage_type)
            if serializer.is_valid():
                serializer.save()
                i = i + 1
        print(f'Created {i} usage types')
