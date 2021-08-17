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
        def _time_range_filter(request):
            return request.query_params.get(
                'time_range_from') is not None and\
                request.query_params.get('time_range_to') is not None

        if self.request.user.is_staff:
            queryset = Usage.objects.all()
        else:
            queryset = self.request.user.usage_set.all()
        if _time_range_filter(self.request):
            range_from = self.request.query_params.get('time_range_from')
            range_to = self.request.query_params.get('time_range_to')
            queryset = queryset.filter(
                usage_at__gte=range_from, usage_at__lte=range_to)
        if self.request.query_params.get('sorting'):
            sorting = self.request.query_params.get('sorting')
            queryset = queryset.order_by(sorting)
        return queryset

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
