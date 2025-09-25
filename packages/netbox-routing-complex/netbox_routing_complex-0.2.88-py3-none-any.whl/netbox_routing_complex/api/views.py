from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import BFDConfigSerializer

class BFDConfigViewSet(NetBoxModelViewSet):
    queryset = models.BFDConfig.objects.prefetch_related('tags')
    serializer_class = BFDConfigSerializer