from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from ..models import BFDConfig, BGPSessionConfig
from ..constants import APP_LABEL

class BFDConfigSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name=f'plugins-api:{APP_LABEL}-api:bfdconfig-detail' #this is the name of an api view that we have to write and link to in urls
    )

    class Meta:
        model = BFDConfig
        fields = (
            #the order of these fields is how the JSON/API representation of the object will be structured
            'id', 'hello_interval', 'multiplier', 'description', 'tags', 'custom_fields', 'created', 'last_updated'
        )
        brief_fields = ('id', 'hello_interval', 'multiplier', 'description') #the shorthand serializer




class BGPSessionConfigSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name=f'plugins-api:{APP_LABEL}-api:bgpsessionconfig-detail'
    )

    class Meta:
        model = BGPSessionConfig
        fields = (
            'id', 'name', 'address_families', 'peer_asn', 'import_policy', 'export_policy',
            'next_hop_self', 'hardcoded_description', 'hello_interval', 'keepalive_interval',
            'ebgp_multihop', 'unencrypted_password', 'encrypted_password', 'source_interface',
            'source_ip', 'local_asn', 'bfd_config', 'tags', 'custom_fields', 'created', 'last_updated'
        )
        brief_fields = ('id', 'name', 'description')