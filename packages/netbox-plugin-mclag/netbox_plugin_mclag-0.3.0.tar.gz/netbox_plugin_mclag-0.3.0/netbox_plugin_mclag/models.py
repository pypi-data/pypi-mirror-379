from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel

from netbox_plugin_mclag.choices import LagTypeChoices

class McDomain(NetBoxModel):
    name = models.CharField(max_length=100)
    domain_id = models.CharField(max_length=20, blank=True, null=True, verbose_name="Domain ID")
    description = models.TextField(max_length=200, blank=True, null=True)
    devices = models.ManyToManyField(
        to='dcim.Device',
        related_name="mc_domains"
    )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_plugin_mclag:mcdomain', args=[self.pk])
    class Meta:
        verbose_name="Multi-Chassis Domain"
        verbose_name_plural="Multi-Chassis Domains"

class McLag(NetBoxModel):
    name = models.CharField(max_length=100)
    lag_id = models.CharField(max_length=20, blank=True, null=True, verbose_name="Group ID")
    description = models.TextField(max_length=200, blank=True, null=True)
    type = models.CharField(
        max_length=20,
        choices=LagTypeChoices,
        default=LagTypeChoices.LAGTYPE_CHANNEL
    )
    mc_domain = models.ForeignKey(
        to=McDomain,
        on_delete=models.CASCADE,
        related_name="mc_lags",
        verbose_name="Multi-Chassis Domain"
    )
    interfaces = models.ManyToManyField(
        to='dcim.Interface',
        related_name="mc_lags"
    )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_plugin_mclag:mclag', args=[self.pk])
    def get_type_color(self):
        return LagTypeChoices.colors.get(self.type)
    class Meta:
        verbose_name="Multi-Chassis Link Aggregation Group"
        verbose_name_plural="Multi-Chassis Link Aggregation Groups"
