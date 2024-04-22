# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Directors(models.Model):
    movie = models.ForeignKey('Movies', models.DO_NOTHING)
    person = models.ForeignKey('People', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'directors'


class Movies(models.Model):
    title = models.TextField()
    year = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'movies'


class People(models.Model):
    name = models.TextField()
    birth = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'people'


class Ratings(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    rating = models.FloatField()
    votes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ratings'


class Stars(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    person = models.ForeignKey(People, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stars'
