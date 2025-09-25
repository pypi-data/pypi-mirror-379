from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from netbox.plugins import PluginTemplateExtension

from netbox_plugin_mclag.models import McDomain, McLag


class McLagInterfaceExtensions(PluginTemplateExtension):
    model = "dcim.interface" # NB = 4.2
    models = ("dcim.interface",) # NB >= 4.3

    def buttons(self):
        interface = self.context["object"]

        if interface.type != "lag":
            interface = interface.lag

        if interface is None:
            return ""

        try:
            mc_lag = interface.mc_lags.get()
            title = "Show MC-LAG"
            url = f"/plugins/mclag/mclags/{ mc_lag.id }/"
        except MultipleObjectsReturned:
            # Does it really make sense for an interface to be part of multiple MC-LAGs? Probably not... but let's handle the case anyway.
            title = "Show MC-LAGs"
            url = f"/plugins/mclag/mclags/?interface={ interface.id }"
        except ObjectDoesNotExist:
            return ""

        return self.render(
            "netbox_plugin_mclag/button.html",
            extra_context={"url": url, "title": title},
        )


class McLagDeviceExtensions(PluginTemplateExtension):
    model = "dcim.device" # NB = 4.2
    models = ("dcim.device",) # NB >= 4.3

    def buttons(self):
        device = self.context["object"]

        try:
            mc_domain = device.mc_domains.get()
            title = "Show MC Domain"
            url = f"/plugins/mclag/domains/{ mc_domain.id }/"
        except MultipleObjectsReturned:
            title = "Show MC Domains"
            url = f"/plugins/mclag/domains/?device={ device.id }/"
        except ObjectDoesNotExist:
            return ""

        return self.render(
            "netbox_plugin_mclag/button.html",
            extra_context={"url": url, "title": title},
        )


template_extensions = [McLagInterfaceExtensions, McLagDeviceExtensions]
