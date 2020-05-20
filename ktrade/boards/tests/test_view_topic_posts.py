from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve,reverse
from ..models import Board,Topic,Post
from ..views import topic_posts

class TopicPostTest(TestCase):
    def setUp(self):
        board = Board.objects.create(name="Django", description="Django Board")
        user = User.objects.create_user(username="john",email="john@test.com",password="123456")
        topic = Topic.objects.create(subject="hello,world",board=board,starter=user)
        Post.objects.create(message="test message for testing",topic=topic,created_by=user)
        url =reverse("topic_posts",kwargs={"pk":board.pk,"topic_pk":topic.pk})
        self.response = self.client.get(url)
    
    def test_status_code(self):
        self.assertEquals(self.response.status_code,200)
    def test_view_function(self):
        view = resolve("/boards/1/topics/1/")
        self.assertEquals(view.func,topic_posts)