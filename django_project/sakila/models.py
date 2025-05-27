from django.db import models

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        ordering = ['country']

    def str(self):
        return self.country
    
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='country_id')
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'city'
        managed = False  # car la table existe déjà
        ordering = ['city']

    def __str__(self):
        return self.city

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'actor'
        ordering = ['last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    actors = models.ManyToManyField('Actor', through='FilmActor')
    class Meta:
        db_table = 'film'
        managed = False
        ordering = ['title']

    def __str__(self):
        return self.title

class FilmActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, db_column='actor_id')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, db_column='film_id')
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_actor'
        managed = False
        unique_together = ('actor', 'film')

    def __str__(self):
        return f"{self.actor} in {self.film}"
