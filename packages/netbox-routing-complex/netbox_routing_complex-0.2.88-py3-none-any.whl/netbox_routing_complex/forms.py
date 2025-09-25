from netbox.forms import NetBoxModelForm
from .models import BFDConfig
from utilities.forms.fields import CommentField

class BFDConfigForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = BFDConfig
        fields = ('hello_interval', 'multiplier', 'description', 'comments', 'tags')