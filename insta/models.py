from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
# Create your models here.

# image
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,related_name='user_images')
    image = CloudinaryField('image')
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    comment = models.IntegerField(blank=True,null=True,default=True)
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
    
    @property
    def saved_comments(self):
        return self.comments.all()
    
    @property
    def saved_likes(self):
      return self.postslikes.count()
    
    def __str__(self):
        return self.name
    
liking={('Like','Like'),('Unlike','Unlike')}
    
class Profile(models.Model):
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
        return self.user.username
    
    
class Comment(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')
    
    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments
    
class Like(models.Model):
    val = models.CharField(choices=liking,default='like',max_length=50)
    image = models.ForeignKey(Image,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.val
    
    
    
