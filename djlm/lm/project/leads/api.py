from models import leads
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#lead viewset, create crud without creating speific routes
class LeadViewset(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer