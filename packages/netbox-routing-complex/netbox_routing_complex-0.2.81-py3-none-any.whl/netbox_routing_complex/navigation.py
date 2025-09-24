from extras.plugins import PluginMenuItem, PluginMenuButton
from utilities.choices import ButtonColorChoices

#each model / navigation menu item can have buttons attached to it with additional links
bfdconfig_buttons = [
    PluginMenuButton(
        link='plugins:netbox_routing_complex:bfdconfig_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    #simply add a new plugin menu item to this file per endpoint that you want to be accessible via the left panel
    PluginMenuItem(
        link = 'plugins:netbox_routing_complex:bfdconfig_list',
        link_text = 'BFD Configs',
        buttons = bfdconfig_buttons #optionally add the buttons defined above to this menu item
    )
)

