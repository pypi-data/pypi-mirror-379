import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import BFDConfig, BGPSessionConfig

class BFDConfigTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = BFDConfig
        fields = ('pk', 'id', 'hello_interval', 'multiplier', 'description')
        default_columns = ('hello_interval', 'multiplier', 'description')

class BGPSessionConfigTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = BGPSessionConfig
        fields = (
            'pk', 'id', 'name', 'address_families', 'peer_asn', 'import_policy', 'export_policy',
            'next_hop_self', 'hardcoded_description', 'hello_interval', 'keepalive_interval',
            'ebgp_multihop', 'source_interface', 'source_ip', 'local_asn', 'bfd_config'
        )
        default_columns = ('name', 'peer_asn', 'address_families', 'bfd_config', 'hardcoded_description')