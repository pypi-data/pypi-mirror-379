from netbox.api.routers import NetBoxRouter

from . import views

from ..constants import APP_LABEL

app_name = APP_LABEL

#link the view to an api route
router = NetBoxRouter()
router.register('bfd-configs', views.BFDConfigViewSet)

urlpatterns = router.urls