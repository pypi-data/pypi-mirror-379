from datetime import timedelta
from functools import reduce

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from huscy.projects.models import Project


class Experiment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='experiments',
                                verbose_name=_('Project'))

    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), blank=True, default='')

    order = models.PositiveSmallIntegerField(_('Order'))

    class Meta:
        ordering = 'order',
        verbose_name = _('Experiment')
        verbose_name_plural = _('Experiments')


class Session(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='sessions',
                                   verbose_name=_('Experiment'))

    title = models.CharField(_('Title'), max_length=255)
    contacts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='+')

    order = models.PositiveSmallIntegerField(_('Order'))

    class Meta:
        ordering = 'order',
        verbose_name = _('Session')
        verbose_name_plural = _('Sessions')

    @property
    def duration(self):
        return reduce(
            lambda total, data_acquisition_method: total + data_acquisition_method.duration,
            self.data_acquisition_methods.all(),
            timedelta(),
        )


class DataAcquisitionMethodType(models.Model):
    short_name = models.CharField(_('Short name'), max_length=32, primary_key=True, editable=False)
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Data acquisition method type')
        verbose_name_plural = _('Data acquisition method types')


class DataAcquisitionMethod(models.Model):
    class STIMULUS(models.TextChoices):
        auditive = ('auditive', _('Auditive'))
        gustatory = ('gustatory', _('Gustatory'))
        haptic = ('haptic', _('Haptic'))
        olfactory = ('olfactory', _('Olfactory'))
        visual = ('visual', _('Visual'))

    session = models.ForeignKey(Session, on_delete=models.CASCADE,
                                related_name='data_acquisition_methods', verbose_name=_('Session'))
    order = models.PositiveSmallIntegerField(_('Order'))

    type = models.ForeignKey(DataAcquisitionMethodType, on_delete=models.PROTECT,
                             verbose_name=_('Type'))

    setup_time = models.DurationField(_('Setup time'), default=timedelta())
    duration = models.DurationField(_('Duration'))
    teardown_time = models.DurationField(_('Teardown time'), default=timedelta())

    stimulus = models.CharField(_('Stimulus'), max_length=32, null=True, choices=STIMULUS.choices)

    location = models.CharField(_('Location'), max_length=126)

    class Meta:
        verbose_name = _('Data acquisition method')
        verbose_name_plural = _('Data acquisition methods')
