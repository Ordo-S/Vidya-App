from django.db import models
from django.utils import timezone
from django.urls import reverse
class Genre(models.Model):
    
    name = models.CharField(max_length=200, help_text="Enter a game genre (e.g. RPG, Action, Shooter, ect..)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

 #Used to generate URLs by reversing the URL patterns

class Game(models.Model):
    
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=1000, null=True, help_text="Eneter the game website")
    img = models.CharField(max_length=1000, null=True, help_text="Put the link for the game box image")
    review = models.TextField( help_text="Enter a review")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    release_date = models.DateTimeField(blank=True, null=True, help_text='Enter the date the game is released')
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        
        return reverse('game-detail', args=[str(self.id)])

class Publisher(models.Model):
    
    name = models.CharField(max_length=100)
    
    
    def get_absolute_url(self):
       
        return reverse('publisher-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return "{0}" .format(self.name)

class Comments(models.Model):
    post = models.ForeignKey('game', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



# Create your models here.
