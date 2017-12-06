from django.db import models
from django.utils import timezone

#name of model is Post, models.Model indicates that it is a django model
class Post(models.Model):
    #this is a link to another model
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #title, using CharField, will be a text field with a limited number of characters
    title = models.CharField(max_length=200)
    #text is for the body of the post, and TextField means there's no character limit
    text = models.TextField()
    #date and time, makes sense
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #make a method called publish
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #this method returns a string with the post title
    def __str__(self):
        return self.title
# Create your models here.
