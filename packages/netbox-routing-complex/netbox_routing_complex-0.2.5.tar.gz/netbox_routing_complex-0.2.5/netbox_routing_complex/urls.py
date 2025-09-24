from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from .constants import APP_LABEL
from . import models, views

print("Attempting import of url patterns")
urlpatterns = [
    path('bfd-configs/',                 views.BFDConfigListView.as_view(),   name='bfdconfig_list'),
    path('bfd-configs/add/',             views.BFDConfigEditView.as_view(),   name='bfdconfig_add'),
    path('bfd-configs/<int:pk>/',        views.BFDConfigView.as_view(),       name='bfdconfig'),
    path('bfd-configs/<int:pk>/edit/',   views.BFDConfigEditView.as_view(),   name='bfdconfig_edit'),
    path('bfd-configs/<int:pk>/delete/', views.BFDConfigDeleteView.as_view(), name='bfdconfig_delete'),

    #changelog endpoint
    path('bfd-configs/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='bfdconfig_changelog', kwargs={
        'model': models.BFDConfig
    }),
]
print(urlpatterns)

#this is where we link views to URLs
#<int:pk> is a path converter which allows the user to enter an integer to get a specific object from the database by its id



