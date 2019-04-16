from rest_framework import routers
from api import LeadViewSet


routers = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
