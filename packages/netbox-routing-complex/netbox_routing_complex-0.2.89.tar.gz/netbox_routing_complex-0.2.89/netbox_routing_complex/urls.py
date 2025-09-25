from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from .constants import APP_LABEL
from . import models, views

urlpatterns = [
    # BFD Config URLs
    path('bfd-configs/',                 views.BFDConfigListView.as_view(),   name='bfdconfig_list'),
    path('bfd-configs/add/',             views.BFDConfigEditView.as_view(),   name='bfdconfig_add'),
    path('bfd-configs/<int:pk>/',        views.BFDConfigView.as_view(),       name='bfdconfig'),
    path('bfd-configs/<int:pk>/edit/',   views.BFDConfigEditView.as_view(),   name='bfdconfig_edit'),
    path('bfd-configs/<int:pk>/delete/', views.BFDConfigDeleteView.as_view(), name='bfdconfig_delete'),
    path('bfd-configs/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='bfdconfig_changelog', kwargs={
        'model': models.BFDConfig
    }),

    # BGP Session Config URLs
    path('bgp-session-configs/',                 views.BGPSessionConfigListView.as_view(),   name='bgpsessionconfig_list'),
    path('bgp-session-configs/add/',             views.BGPSessionConfigEditView.as_view(),   name='bgpsessionconfig_add'),
    path('bgp-session-configs/<int:pk>/',        views.BGPSessionConfigView.as_view(),       name='bgpsessionconfig'),
    path('bgp-session-configs/<int:pk>/edit/',   views.BGPSessionConfigEditView.as_view(),   name='bgpsessionconfig_edit'),
    path('bgp-session-configs/<int:pk>/delete/', views.BGPSessionConfigDeleteView.as_view(), name='bgpsessionconfig_delete'),
    path('bgp-session-configs/<int:pk>/changelog/', ObjectChangeLogView.as_view(),           name='bgpsessionconfig_changelog', kwargs={
        'model': models.BGPSessionConfig
    }),
]

#this is where we link views to URLs
#<int:pk> is a path converter which allows the user to enter an integer to get a specific object from the database by its id



