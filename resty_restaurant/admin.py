# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Venue, Schedule


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'cellphone', 'landline', 'stars')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
