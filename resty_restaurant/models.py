# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager


class Venue(models.Model):
    '''
    Model a common restaurant or place for eating.

    booking_endpoint: The URL used to make a reservation in this venue.


    TODO:
    price_range - list of different price dishes
    payment_options - paypal, cash, credit_card, bitcoins
    cuisine_type
    social_media_info (https://github.com/creafz/django-social-widgets)
    '''
    name = models.CharField(max_length=60, blank=False, null=False)
    # This may be improved by using some geolocalization service.
    address = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    stars = models.PositiveSmallIntegerField()
    # This phone numbers may be moved to a different model in a many-to-one relation.
    cellphone = models.CharField(max_length=30, blank=False, null=False)
    landline = models.CharField(max_length=30, blank=False, null=False)

    booking_endpoint = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    tags = TaggableManager()

    def __unicode__(self):
        return '{}'.format(self.name)


class Schedule(models.Model):
    ''' Used to keep track of the different opening hours for each venue. '''
    WEEKDAYS = [
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
        (7, _("Sunday")),
    ]
    venue = models.ForeignKey(Venue)
    from_weekday = models.IntegerField(choices=WEEKDAYS)
    to_weekday = models.IntegerField(choices=WEEKDAYS, null=True, blank=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        unique_together = (("venue", "from_weekday"), )

    def __unicode__(self):
        return '{0}{1}, {2} to {3}'.format(
            self.from_weekday_str,
            ' to {}'.format(self.to_weekday_str) if self.to_weekday else '',
            self.from_hour, self.to_hour)

    @property
    def from_weekday_str(self):
        return Schedule.WEEKDAYS[self.from_weekday - 1][1]

    @property
    def to_weekday_str(self):
        return Schedule.WEEKDAYS[self.to_weekday - 1][1]
