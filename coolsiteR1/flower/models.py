from django.db import models
from django.urls import reverse


class Flower(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,verbose_name="URL", null=True)
    description = models.TextField(blank=True,  verbose_name='описание')
    photo = models.ImageField(upload_to='photo/%Y%m%d', verbose_name='фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время добавления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='время изменения')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('read_flower', kwargs={'flo_slug': self.slug})

    class Meta:
        verbose_name ='Разновидности растений'
        verbose_name_plural = 'Разновидности растений'
        ordering = ['-time_update']

class Category(models.Model):
    n_cat = models.CharField(max_length=150, db_index=True, verbose_name='категории')
    slug = models.SlugField(max_length=150,unique=True, db_index=True,verbose_name="URL",null=True )

    def __str__(self):
        return self.n_cat

    def get_absolute_url(self):
        return reverse('category', kwargs={'categ_slug': self.slug})

    class Meta:
        verbose_name = 'Категории растений'
        verbose_name_plural = 'Категории растений'
        ordering = ['id']