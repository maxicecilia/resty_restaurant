# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Venue, Schedule


class ScheduleAdmin(admin.TabularInline):
    model = Schedule


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'cellphone', 'landline', 'stars')
    inlines = [ScheduleAdmin, ]
