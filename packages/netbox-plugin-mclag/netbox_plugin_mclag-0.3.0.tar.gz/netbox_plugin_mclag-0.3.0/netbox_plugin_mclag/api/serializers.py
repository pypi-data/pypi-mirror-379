from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from dcim.api.serializers import DeviceSerializer, InterfaceSerializer
from dcim.models import Interface

from netbox_plugin_mclag.models import McLag, McDomain
from netbox_plugin_mclag.util import get_interface_label

#
# Nested serializers
#

class NestedMcDomainSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_plugin_mclag-api:mcdomain-detail'
    )
    devices = DeviceSerializer(nested=True, many=True)
    display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = McDomain
        fields = ('id', 'url', 'name', 'display', 'domain_id', 'devices')


class NestedMcLagSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_plugin_mclag-api:mclag-detail'
    )
    interfaces = InterfaceSerializer(nested=True, many=True)
    display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = McLag
        fields = ('id', 'name', 'display', 'url', 'name', 'lag_id', 'type', 'interfaces')

#
# Regular serializers
#

class McDomainSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_plugin_mclag-api:mcdomain-detail'
    )
    mc_lags = NestedMcLagSerializer(many=True)
    devices = DeviceSerializer(nested=True, many=True)
    display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = McDomain
        fields = (
            'id', 'url', 'name', 'display', 'domain_id', 'devices', 'description', 'mc_lags', 'tags', 'custom_fields',
            'created', 'last_updated',
        )


class McLagSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_plugin_mclag-api:mclag-detail'
    )
    mc_domain = NestedMcDomainSerializer()
    interfaces = InterfaceSerializer(nested=True, many=True)
    display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = McLag
        fields = (
            'id', 'url', 'name', 'display', 'lag_id', 'type', 'description', 'mc_domain', 'interfaces', 'tags', 'custom_fields',
            'created', 'last_updated',
        )

class McInterfaceSerializer(NetBoxModelSerializer):
    def get_display(self, interface):
        return get_interface_label(interface)
    class Meta:
        model = Interface
        fields = ['id', 'display']
