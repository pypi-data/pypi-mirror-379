import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import BFDConfig, BGPPeer, BGPPeerGroup, BGPSessionConfig

class BFDConfigTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = BFDConfig
        fields = ('pk', 'id', 'hello_interval', 'multiplier', 'description')
        default_columns = ('hello_interval', 'multiplier', 'description')

class BGPSessionConfigTable(NetBoxTable):
    bfd_config = tables.LinkColumn()
    class Meta(NetBoxTable.Meta):
        model = BGPSessionConfig
        fields = (
            'pk', 'id', 'name', 'address_families', 'peer_asn', 'import_policy', 'export_policy',
            'next_hop_self', 'hardcoded_description', 'hello_interval', 'keepalive_interval',
            'ebgp_multihop', 'source_interface', 'source_ip', 'local_asn', 'bfd_config'
        )
        default_columns = ('name', 'peer_asn', 'address_families', 'bfd_config', 'hardcoded_description')

class BGPPeerTable(NetBoxTable):
    device = tables.LinkColumn()
    session_config = tables.LinkColumn()
    peer_ip = tables.LinkColumn()
    class Meta(NetBoxTable.Meta):
        model = BGPPeer
        fields = ('pk', 'id', 'device', 'name', 'peer_ip', 'session_config')
        default_columns = ('device', 'name', 'peer_ip', 'session_config')

class BGPPeerGroupTable(NetBoxTable):
    device = tables.LinkColumn()
    session_config = tables.LinkColumn()
    peers = tables.ManyToManyColumn(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = BGPPeerGroup
        fields = ('pk', 'id', 'device', 'name', 'description', 'session_config', 'peers')
        default_columns = ('device', 'name', 'description', 'session_config', 'peers')