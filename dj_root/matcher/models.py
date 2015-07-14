from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User


class Playgroup(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Player(models.Model):
    playgroup = models.ForeignKey(Playgroup)
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class FootballMetric(models.Model):
    player = models.OneToOneField(Player, primary_key=True)
    defence = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    midfield = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    attack = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __unicode__(self):
        return unicode(
            {self.player: [self.defence, self.midfield, self.attack]}
        )


