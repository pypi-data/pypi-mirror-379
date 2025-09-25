from netbox.choices import ButtonColorChoices
from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton
#^this doesn't match the tutorial because the latest api has rearranged things into the netbox namespace per below
#https://netboxlabs.com/docs/netbox/plugins/development/navigation/

#simply add a new plugin menu item to this file per endpoint that you want to be accessible via the left panel; these use the view names from urls.py for their link
bfdconfig_menu_with_add_button = PluginMenuItem(
    link = 'plugins:netbox_routing_complex:bfdconfig_list',
    link_text = 'BFD Configs',
    buttons = (
            PluginMenuButton(
                link='plugins:netbox_routing_complex:bfdconfig_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
                ),
            )
)

menu = PluginMenu(
    label='Complex Routing',
    groups = (
        ('Misc', (bfdconfig_menu_with_add_button,)), #Misc is the subcategory name in the left panel, note that each subpanel is a tuple where the second value is also a tuple of PluginMenuItem instances
    ),
    icon_class='mdi mdi-router'
)