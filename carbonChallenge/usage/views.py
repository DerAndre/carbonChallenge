from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from usage.models import Usage, UsageType
from usage.serializers import UsageSerializer, UsageTypeSerializer
from carbonChallenge.permissions import IsOwner, FromAdminOrRead


class UsageViewSet(viewsets.ModelViewSet):
    """
    A simple ModelViewSet to provide basic CRUD functionality for usage model
    """

    filterset_fields = ['amount', 'usage_at', 'usage_type', 'user']
    permission_classes = [IsOwner | IsAdminUser]
    serializer_class = UsageSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            Usage.objects.all()
        return self.request.user.usage_set.all()

    def create(self, request):
        request.data['user'] = request.user.pk
        serializer = UsageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsageTypeViewSet(viewsets.ModelViewSet):
    """
    A simple ModelViewSet to provide basic CRUD functionality for usage type model
    """

    filterset_fields = ['name', 'unit', 'factor']
    serializer_class = UsageTypeSerializer
    permission_classes = [FromAdminOrRead]

    def get_queryset(self):
        return UsageType.objects.all()
