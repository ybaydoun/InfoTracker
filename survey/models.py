import datetime
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField
from django.contrib.postgres.fields import ArrayField, JSONField


class Topic(TimeStampedModel):
    name = models.CharField(
        max_length=500,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Name'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Language(TimeStampedModel):
    name = models.CharField(
        max_length=500,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Name'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Channel(TimeStampedModel):
    name = models.CharField(
        max_length=500,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Name'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Audience(TimeStampedModel):
    name = models.CharField(
        max_length=500,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Name'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Audience"
        verbose_name_plural = "Audiences"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Sector(TimeStampedModel):
    name = models.CharField(
        max_length=500,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Name'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Source(TimeStampedModel):
    name = models.CharField(
        max_length=500,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Name'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Source"
        verbose_name_plural = "Sources"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Output(TimeStampedModel):
    name = models.CharField(
        max_length=500,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Name'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Output"
        verbose_name_plural = "Outputs"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Type(TimeStampedModel):
    name = models.CharField(
        max_length=500,
        blank=True,
        null=False,
        unique=True,
        verbose_name='Name'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Type"
        verbose_name_plural = "Type"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Message(TimeStampedModel):
    msg_number = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name='Message number'
    )
    topic = models.ForeignKey(
        Topic,
        blank=False, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Topic'
    )
    language = models.ForeignKey(
        Language,
        blank=False, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Language'
    )
    channel = models.ForeignKey(
        Channel,
        blank=False, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Channel'
    )
    audience = models.ForeignKey(
        Audience,
        blank=False, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Audience'
    )
    sector = models.ForeignKey(
        Sector,
        blank=False, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Sector'
    )
    adapted_by = models.ManyToManyField(
        Source,
        related_name='+',
        verbose_name='Adapted from Below Source'
    )
    adapted_by_2 = models.ManyToManyField(
        Source,
        related_name='+',
        verbose_name='Adapted from Below Source'
    )
    desired_output = models.ForeignKey(
        Output,
        blank=False, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Desired behavior / output'
    )
    message_type = models.ForeignKey(
        Type,
        blank=False, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Type of message / driver'
    )

    english_message = models.TextField(
        'English Messages',
        null=True,
        blank=True,
    )
    arabic_message = models.TextField(
        'Arabic Messages',
        null=True,
        blank=True,
    )

    relevant_link = models.URLField('Link to IEC materials', null=True, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Created by'
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True, null=True,
        related_name='+',
        on_delete=models.DO_NOTHING,
        verbose_name='Modified by'
    )

    @property
    def reported_organization(self):
        return self.reported_by.last_name

    def dissemination_method_list(self):
        if self.dissemination_method:
            return ", ".join(self.dissemination_method)
        return ''

    def save(self, **kwargs):
        if not self.msg_number:
            objects = list(Message.objects.all().order_by('created').values_list('id', flat=True))
            sequence = '{0:03d}'.format(objects.index(self.id) + 1 if self.id in objects else len(objects) + 1)
            self.msg_number = '{}-{}'.format(
                'MSG',
                sequence
            )

        super(Message, self).save(**kwargs)

    class Meta:
        ordering = ['msg_number']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __unicode__(self):
        return self.msg_number

    def __str__(self):
        return self.msg_number

