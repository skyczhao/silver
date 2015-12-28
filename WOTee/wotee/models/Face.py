# -*- coding: utf-8 -*-

__author__ = 'tobin'

import os

from django.db import models

class Face(models.Model):
    md5 = models.CharField(unique=True, blank=False, max_length=32)
    name = models.CharField(blank=False, max_length=64)
    extension = models.CharField(blank=False, max_length=16)
    path = models.CharField(blank=False, max_length=128)

    class Meta:
        app_label = 'wotee'

    # return complete location
    def location(self):
        return os.path.join(self.path, self.md5 + self.extension)