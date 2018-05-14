from django.db import models
from utils.string_utils import encode_id
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    # auto now is for every update, auto_now_add is for insert
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    deleted = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.title

    def url(self):
        return encode_id(self.id)

    def delete(self, using=None, keep_parents=False):
        self.deleted = 1



