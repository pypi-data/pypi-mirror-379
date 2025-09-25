from netbox.views import generic
from . import forms, models, tables

#Create four view for each object
#1. Detail view for a single object
#2. List view for all existing instances of the model
#3. Edit view for adding/modifying objects
#4. Delete view for deleting objects

#detail view
class BFDConfigView(generic.ObjectView):
    queryset = models.BFDConfig.objects.all()

#list view
class BFDConfigListView(generic.ObjectListView):
    queryset = models.BFDConfig.objects.all()
    table = tables.BFDConfigTable

#edit/modification view
class BFDConfigEditView(generic.ObjectEditView):
    queryset = models.BFDConfig.objects.all()
    form = forms.BFDConfigForm

#delete view
class BFDConfigDeleteView(generic.ObjectDeleteView):
    queryset = models.BFDConfig.objects.all()



# BGP Session Config Views
class BGPSessionConfigView(generic.ObjectView):
    queryset = models.BGPSessionConfig.objects.all()

class BGPSessionConfigListView(generic.ObjectListView):
    queryset = models.BGPSessionConfig.objects.all()
    table = tables.BGPSessionConfigTable

class BGPSessionConfigEditView(generic.ObjectEditView):
    queryset = models.BGPSessionConfig.objects.all()
    form = forms.BGPSessionConfigForm

class BGPSessionConfigDeleteView(generic.ObjectDeleteView):
    queryset = models.BGPSessionConfig.objects.all()