from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.fields import related
from django.contrib.auth.models import User


# Create your models here
class Profile(models.Model):
    prof_photo = CloudinaryField('image')
    bio = models.TextField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

class Images(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    caption = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    like_count = models.ManyToManyField(User,related_name='liked',default=0)
    comm_count = models.IntegerField(default=0)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image',null=True)
    def __str__(self):
        return self.name

    @property
    def saved_comments(self):
        return self.comments.all()

    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()

    @classmethod
    def get_images_by_user(cls, user):
        images = cls.objects.filter(user=user)
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images
    
LIKE_CHOICES={
    ('Like','Like'),
    ('Unlike','Unlike',)
}
class Likes(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def str(self):
        return self.value

class Comments(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(Images,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')

    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments
