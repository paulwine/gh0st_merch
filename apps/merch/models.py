# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    admin_level = models.IntegerField(default = 0)
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Size(models.Model):
    size = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    price = models.FloatField()

class Print(models.Model):
    image_url = models.CharField(max_length = 255)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



class Song(models.Model):
    song_url = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    duration = models.IntegerField()
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Video(models.Model):
    video_url = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    duration = models.IntegerField()
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# Create your models here.
