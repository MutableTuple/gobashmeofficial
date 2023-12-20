import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True,null=True)
    profile_image  = models.ImageField(null=True,blank=True,default="profiles/default-user.png",upload_to="profiles/",max_length=20000)
    username = models.CharField(max_length=200,blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True, editable=False)
    def __str__(self):
        return str(f'{self.user.profiles.name} ({self.user.username})')
    
class Message(models.Model):
    sender = models.ForeignKey(Profiles, related_name='sent_messages', on_delete=models.CASCADE,null=True,blank=True)
    recipient = models.ForeignKey(Profiles, related_name='received_messages', on_delete=models.CASCADE,null=True,blank=True)
    subject = models.CharField(null=True, blank=True,max_length=500)
    message = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True, editable=False)
    created=models.DateTimeField(auto_now_add=True )
    def __str__(self):
            return str(f'{self.sender} ===> ({self.recipient})')