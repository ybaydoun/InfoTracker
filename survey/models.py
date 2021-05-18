import datetime
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField
from django.contrib.postgres.fields import ArrayField, JSONField


# class Topic(TimeStampedModel):
#     name = models.CharField(
#         max_length=500,
#         blank=True,
#         null=False,
#         unique=True,
#         verbose_name='Name'
#     )
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "Topic"
#         verbose_name_plural = "Topics"
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
# class Language(TimeStampedModel):
#     name = models.CharField(
#         max_length=500,
#         blank=True,
#         null=False,
#         unique=True,
#         verbose_name='Name'
#     )
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "Language"
#         verbose_name_plural = "Languages"
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
# class Channel(TimeStampedModel):
#     name = models.CharField(
#         max_length=500,
#         blank=True,
#         null=False,
#         unique=True,
#         verbose_name='Name'
#     )
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "Channel"
#         verbose_name_plural = "Channels"
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
#
# class Audience(TimeStampedModel):
#     name = models.CharField(
#         max_length=500,
#         blank=True,
#         null=False,
#         unique=True,
#         verbose_name='Name'
#     )
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "Audience"
#         verbose_name_plural = "Audiences"
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
# class Sector(TimeStampedModel):
#     name = models.CharField(
#         max_length=500,
#         blank=True,
#         null=False,
#         unique=True,
#         verbose_name='Name'
#     )
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "Sector"
#         verbose_name_plural = "Sectors"
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
#
# class Source(TimeStampedModel):
#     name = models.CharField(
#         max_length=500,
#         blank=True,
#         null=False,
#         unique=True,
#         verbose_name='Name'
#     )
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "Source"
#         verbose_name_plural = "Sources"
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
#
# class Output(TimeStampedModel):
#     name = models.CharField(
#         max_length=500,
#         blank=True,
#         null=False,
#         unique=True,
#         verbose_name='Name'
#     )
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "Output"
#         verbose_name_plural = "Outputs"
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
#
# class Type(TimeStampedModel):
#     name = models.CharField(
#         max_length=500,
#         blank=True,
#         null=False,
#         unique=True,
#         verbose_name='Name'
#     )
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "Type"
#         verbose_name_plural = "Type"
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name

