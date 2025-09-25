import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import BFDConfig

class BFDConfigTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = BFDConfig
        fields = ('pk', 'id', 'hello_interval', 'multiplier', 'description')
        default_columns = ('hello_interval', 'multiplier', 'description')