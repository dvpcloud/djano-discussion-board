from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):       

    def __str__(self):
        return self.name

   # def get_absolute_url(self):
    #    return reverse("_detail", kwargs={"pk": self.pk})
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=100)

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateField(auto_now_add=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE, related_name = "topics")
    starter = models.ForeignKey(User,on_delete=models.CASCADE,related_name="topics")
    last_updated = models.DateTimeField( auto_now_add=True)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name = "posts")
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( null=True)
    created_by = models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True,on_delete=models.CASCADE, related_name="+")

    
