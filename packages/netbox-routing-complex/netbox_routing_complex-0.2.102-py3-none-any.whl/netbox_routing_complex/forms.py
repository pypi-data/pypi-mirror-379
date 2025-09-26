from django import forms
from netbox.forms import NetBoxModelForm
from .models import AddressFamilyChoices, BFDConfig, BGPPeer, BGPPeerGroup, BGPSessionConfig
from utilities.forms.fields import CommentField

class BFDConfigForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = BFDConfig
        fields = ('hello_interval', 'multiplier', 'description', 'comments', 'tags')



class BGPSessionConfigForm(NetBoxModelForm):
    comments = CommentField()
    #address_families should be a dropdown in the GUI
    address_families = forms.MultipleChoiceField(
        choices=AddressFamilyChoices,
        required=False
    )

    class Meta:
        model = BGPSessionConfig
        fields = (
            'name', 'address_families', 'peer_asn', 'import_policy', 'export_policy',
            'next_hop_self', 'hardcoded_description', 'hello_interval', 'keepalive_interval',
            'ebgp_multihop', 'unencrypted_password', 'encrypted_password', 'source_interface',
            'source_ip', 'local_asn', 'bfd_config', 'comments', 'tags'
        )

class BGPPeerForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = BGPPeer
        fields = ('device', 'name', 'peer_ip', 'session_config', 'comments', 'tags')

class BGPPeerGroupForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = BGPPeerGroup
        fields = ('device', 'name', 'description', 'session_config', 'peers', 'comments', 'tags')