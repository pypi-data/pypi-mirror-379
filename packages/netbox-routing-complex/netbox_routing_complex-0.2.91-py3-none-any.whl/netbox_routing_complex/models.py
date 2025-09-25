from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

from .constants import APP_LABEL

class AddressFamilyChoices(ChoiceSet):
    CHOICES = [
        ('ipv4_unicast', 'IPv4 Unicast', 'blue'),
        ('ipv6_unicast', 'IPv6 Unicast', 'purple'),
    ]

class BFDConfig(NetBoxModel):
    """
    Configuration model for BFD (Bidirectional Forwarding Detection) profiles.
    """
    hello_interval = models.PositiveIntegerField(
        verbose_name='Hello Interval',
        help_text='The minimum interval for sending BFD control packets.'
    )

    multiplier = models.PositiveIntegerField(
        verbose_name='Dead Multiplier',
        help_text='Number of hello packets missed before the session is declared down.'
    )

    description = models.CharField(
        max_length=256,
        blank=True
    )

    class Meta:
        ordering = ('hello_interval', 'multiplier', 'description')
        ## Ensures that each combination of interval and multiplier is unique
        # unique_together = ('hello_interval', 'multiplier')

    def __str__(self):
        """
        Returns a human-readable string representation of the BFD configuration.
        """
        return f'Hello: {self.hello_interval}, Multiplier: {self.multiplier}, Desc: {self.description}'
    
    def get_absolute_url(self):
        '''Get the absolute URL to this object'''
        return reverse(f'plugins:{APP_LABEL}:bfdconfig', args=[self.pk])
    



class BGPSessionConfig(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    address_families = ArrayField(
        base_field=models.CharField(max_length=30, choices=AddressFamilyChoices),
        blank=True,
        null=True
    )

    peer_asn = models.BigIntegerField(
        blank=True,
        null=True
    )

    import_policy = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    export_policy = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    next_hop_self = models.BooleanField(
        default=False
    )

    hardcoded_description = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    hello_interval = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    keepalive_interval = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    ebgp_multihop = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    unencrypted_password = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    encrypted_password = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    source_interface = models.ForeignKey(
        to='dcim.Interface',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    source_ip = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    local_asn = models.BigIntegerField(
        blank=True,
        null=True
    )
    
    bfd_config = models.ForeignKey(
        to=BFDConfig,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(f'plugins:{APP_LABEL}:bgpsessionconfig', args=[self.pk])
    

class BGPPeer(NetBoxModel):
    peer_ip = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='bgp_peer'
    )

    session_config = models.ForeignKey(
        to=BGPSessionConfig,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    name = models.CharField(
        max_length=100,
        blank=True
    )

    class Meta:
        ordering = ('name', 'peer_ip',)
        verbose_name = 'BGP Peer'
        verbose_name_plural = 'BGP Peers'

    def __str__(self):
        return str(self.peer_ip)

    def get_absolute_url(self):
        return reverse(f'plugins:{APP_LABEL}:bgppeer', args=[self.pk])