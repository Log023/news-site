import os
from django.db import models
from django.conf import settings
from PIL import Image
from ckeditor.fields import RichTextField


def default_image():
    return 'articles/default.jpg'


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    intro = models.CharField('Обзор', max_length=80)
    full_text = RichTextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='articles/', default=default_image)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)


class Comment(models.Model):
    article = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.article}'
