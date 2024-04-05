from django.db import models
from django.urls import reverse
from datetime import date

RATING = (
  ('E', 'Excellent'),
  ('G', 'Good'),
  ('F', 'Fair')
)
# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=100)
  superpower = models.CharField(max_length=30) 

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('characters_detail', kwargs={'pk': self.id})

class Comic(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  creator = models.CharField(max_length=100)
  first_appearance = models.CharField(max_length=100)
  publisher = models.CharField(max_length=100)
  characters = models.ManyToManyField(Character)

  def __str__(self):
    return f'{self.title} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'comic_id': self.id})
  
  def rating_for_today(self):
   return self.rating_set.filter(date=date.today()).count() >= len(RATING)


class Rating(models.Model):
  date = models.DateField('Rating Date')
  rating = models.CharField(
    max_length=1,
    choices=RATING,
    default=RATING[0][0]
  )
  # comic_id
  comic = models.ForeignKey(
    Comic, 
    on_delete=models.CASCADE
    )

  def __str__(self):
    return f'Rate on {self.comic.title}'
  
  class Meta:
   ordering = ['-date']
  
