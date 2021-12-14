from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        """creation of profile for testing
        """
        user = User.objects.create(
            username = 'ayubu',
            first_name = 'ayub',
            last_name = '254')
        
        Profile.objects.create(
            bio = 'hey',
            profile_photo = 'static/image/travel.webp',
            user_id = user.id
        )

    
    def test_bio(self):
        """tests the profiles bio
        """
        profile=Profile.objects.get(bio="hey")
        self.assertEqual(profile.bio, "hey")
        

class ImageTestCase(TestCase):
    def setUp(self):
        """image creation
        """
        user = User.objects.create(
            username = 'ayubu',
            first_name = 'ayub',
            last_name = '254')
        
        Image.objects.create(
            name="init",
            caption="ooops",
            profile_id=user.id,
            user_id=user.id
        )
    def test_image_name(self):
        """tests image name
        """
        image=Image.objects.get(name="init")
        self.assertEqual(image.name, "init")
        
class LikeTestCase(TestCase):
    def setUp(self):
         user = User.objects.create(
            username = 'ayubu',
            first_name = 'ayub',
            last_name = '254')
         
         Profile.objects.create(
            bio = 'hey',
            profile_photo = 'static/image/travel.webp',
            user_id = user.id
        )
        
         Image.objects.create(
            name="init",
            caption="ooops",
            profile_id=user.id,
            user_id=user.id
        )
         
         Like.objects.create(
             user_id = user.id,
             image_id = image.id
         )
         
    def test_image_id(self):
         user = User.objects.create(
            username = 'yub',
            first_name = 'yubus',
            last_name = '_254')
         
         Image.objects.create(
            name="init",
            caption="ooops",
            profile_id=user.id,
            user_id=user.id
        )
    