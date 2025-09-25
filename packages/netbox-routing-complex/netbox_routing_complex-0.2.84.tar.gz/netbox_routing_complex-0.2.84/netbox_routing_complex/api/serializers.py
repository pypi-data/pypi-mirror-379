from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, NestedPrefixSerializer, WritableNestedSerializer
#WritableNestedSerializer lets us write our own serializers for the brief versions of our classes

from ..models import BFDConfig
from ..constants import APP_LABEL

class BFDConfigSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name=f'plugins-api:{APP_LABEL}-api:bfdconfig-detail' #this is the name of a view that we have to write and link to in urls
    )

    class Meta:
        model = BFDConfig
        fields = (
            #the order of these fields is how the JSON/API representation of the object will be structured
            'id', 'hello_interval', 'multiplier', 'description', 'comments', 'tags', 'custom_fields', 'created', 'last_updated'
        )