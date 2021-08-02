from rest_framework import routers
from usage.views import UsageViewSet, UsageTypeViewSet

router = routers.SimpleRouter()
router.register(r'usage', UsageViewSet, basename='usage')
router.register(r'usage_type', UsageTypeViewSet, basename='usage_type')
urlpatterns = router.urls
