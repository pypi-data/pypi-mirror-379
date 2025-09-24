from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from .constants import APP_LABEL

from utilities.choices import ChoiceSet

class ActionChoices(ChoiceSet):
    key = 'AccessListRule.action'

    CHOICES = [
        ('permit', 'Permit', 'green'),
        ('deny', 'Deny', 'red'),
        ('reject', 'Reject (Reset)', 'orange'),
    ]

class ProtocolChoices(ChoiceSet):

    CHOICES = [
        ('tcp', 'TCP', 'blue'),
        ('udp', 'UDP', 'orange'),
        ('icmp', 'ICMP', 'purple'),
    ]

class AccessList(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    default_action = models.CharField(
        max_length=30
    )
    comments = models.TextField(
        blank=True
    )

    default_action = models.CharField(
        max_length=30,
        choices=ActionChoices
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_default_action_color(self):
        return ActionChoices.colors.get(self.default_action)
    




class AccessListRule(NetBoxModel):
    access_list = models.ForeignKey(
        to=AccessList,
        on_delete=models.CASCADE,
        related_name='rules'
    )

    index = models.PositiveIntegerField()

    protocol = models.CharField(
        max_length=30,
        choices=ProtocolChoices,
        blank=True
    )

    source_prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    source_ports = ArrayField(
        base_field=models.PositiveIntegerField(),
        blank=True,
        null=True
    )

    destination_prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    destination_ports = ArrayField(
        base_field=models.PositiveIntegerField(),
        blank=True,
        null=True
    )

    action = models.CharField(
        max_length=30
    )

    description = models.CharField(
        max_length=500,
        blank=True
    )

    action = models.CharField(
        max_length=30,
        choices=ActionChoices
    )

    class Meta:
        ordering = ('access_list', 'index')
        unique_together = ('access_list', 'index')

    def __str__(self):
        return f'{self.access_list}: Rule {self.index}'
    
    def get_protocol_color(self):
        return ProtocolChoices.colors.get(self.protocol)

    def get_action_color(self):
        return ActionChoices.colors.get(self.action)
    


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
        ordering = ('hello_interval', 'multiplier')
        # Ensures that each combination of interval and multiplier is unique
        unique_together = ('hello_interval', 'multiplier')

    def __str__(self):
        """
        Returns a human-readable string representation of the BFD configuration.
        """
        return f'Hello: {self.hello_interval}, Multiplier: {self.multiplier}, Desc: {self.description}'
    
    def get_absolute_url(self):
        '''Get the absolute URL to this object'''
        return reverse(f'plugins:{APP_LABEL}:bfdconfig', args=[self.pk])