from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

# image
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=True,null=True, blank=True)
    comments = models.IntegerField(blank=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class meta:
        ordering =['posted_on']
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
        
    def __str__(self):
        return self.name
    
        
    
    
