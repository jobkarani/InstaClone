from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

# image
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,related_name='user_images')
    image = CloudinaryField('image')
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=True,null=True, blank=True)
    comments = models.IntegerField(blank=True,null=True,default=True)
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
        
    @classmethod
    def search_by_name(cls,search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts
        
    def __str__(self):
        return self.name
    
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=650,blank=True,null=True)
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.save()
        
    def update(self):
        self.save()
        
    def __str__(self):
        return self.name
    
    
        
    
    
