# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Publisher, Film, Director
admin.site.register(Publisher)
admin.site.register(Film)
admin.site.register(Director)