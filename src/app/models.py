from django.db import models

# Create your models here.

class Post(models.Model):
    """docstring for Post"""
    YOUTUBE = "YT"
    FACEBOOK = "FB"
    BLOG = "BL"

    TYPE_POST_CHOICES = {
        (YOUTUBE, "Youtube"),
        (FACEBOOK, "Facebook"),
        (BLOG, "Blog"),
    }

    title = models.CharField(max_length=120)
    desc = models.TextField()
    url = models.URLField()
    shorter_url = models.URLField(null=True, blank=True)
    type_post = models.CharField(
        max_length=2,
        choices=TYPE_POST_CHOICES,
        default=YOUTUBE,
    )
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)


class Config(models.Model):

    """Docstring for Config. """
    posts = models.ManyToManyField(Post, through="PostConfig")
    name = models.CharField(max_length=120)
    publish_at = models.CharField(max_length=512)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)


class PostConfig(models.Model):

    """Docstring for PostConfig. """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    config = models.ForeignKey(Config, on_delete=models.CASCADE)
    published_date = models.DateTimeField()


class Source(models.Model):
    name = models.CharField(max_length=120)
    domain = models.CharField(max_length=120)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sources"


class ShortenerUrl(models.Model):
    medium = models.CharField(max_length=120)
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.CharField(max_length=120, null=True, blank=True)
    link = models.URLField()
    shortcut = models.SlugField(null=True, blank=True, max_length=120)
    source = models.ForeignKey(Source, related_name="source", on_delete=models.CASCADE)
    dest = models.ForeignKey(Source, related_name="dest", on_delete=models.CASCADE)
    count = models.IntegerField(null=False, default=0)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return self.link
