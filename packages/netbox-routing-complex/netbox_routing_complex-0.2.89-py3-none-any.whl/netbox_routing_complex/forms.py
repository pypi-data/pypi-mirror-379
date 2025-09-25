from netbox.forms import NetBoxModelForm
from .models import BFDConfig, BGPSessionConfig
from utilities.forms.fields import CommentField

class BFDConfigForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = BFDConfig
        fields = ('hello_interval', 'multiplier', 'description', 'comments', 'tags')



class BGPSessionConfigForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = BGPSessionConfig
        fields = (
            'name', 'address_families', 'peer_asn', 'import_policy', 'export_policy',
            'next_hop_self', 'hardcoded_description', 'hello_interval', 'keepalive_interval',
            'ebgp_multihop', 'unencrypted_password', 'encrypted_password', 'source_interface',
            'source_ip', 'local_asn', 'bfd_config', 'comments', 'tags'
        )