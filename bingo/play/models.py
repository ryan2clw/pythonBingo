"""
The card and row tables will form the data for the bingo cards.
"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

class Card(models.Model):
    """ A bingo card with 5 rows. """
    created_on = models.DateField(auto_now_add=True)

class Row(models.Model):
    """ Each property is a column on a bingo card, should have 5 rows per card """
    b = models.CharField(max_length=3)
    i = models.CharField(max_length=3)
    n = models.CharField(max_length=3)
    g = models.CharField(max_length=3)
    o = models.CharField(max_length=3)
    card = models.ForeignKey(
    	'Card',
        on_delete=models.CASCADE
    )
    #card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card')

    def __str__(self):
        return self.b + "," + self.i + "," + self.n + "," + self.g + "," + self.o + ", card:"

class BingoBoard(models.Model):
    b = ArrayField(
	    models.CharField(max_length=3),
	    size=5
    )
    i = ArrayField(
	    models.CharField(max_length=3),
	    size=5
    )
    n = ArrayField(
	    models.CharField(max_length=3),
	    size=5
    )
    g = ArrayField(
	   models.CharField(max_length=3),
	   size=5
    )
    o = ArrayField(
	   models.CharField(max_length=3),
	   size=5
    )

