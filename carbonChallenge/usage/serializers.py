from rest_framework.serializers import ModelSerializer
from usage.models import Usage, UsageType


class UsageSerializer(ModelSerializer):
    """
    Model serializer for usage model
    """

    class Meta:
        model = Usage
        fields = '__all__'

    def create(self, validated_data):
        return Usage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.usage_type_id = validated_data.get(
            'usage_type', instance.usage_type_id)
        instance.usage_at = validated_data.get('usage_at', instance.usage_at)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance


class UsageTypeSerializer(ModelSerializer):
    """
    Model serializer for usage type model
    """

    class Meta:
        model = UsageType
        fields = '__all__'

    def create(self, validated_data):
        return UsageType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
