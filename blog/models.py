from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Actualixado el ')


    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'


    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='titulo')
    content = RichTextField(verbose_name= 'Contenido')
    image = models.ImageField(verbose_name='Imagen', default='null', upload_to="articles")
    public = models.BooleanField(verbose_name='¿Publicado?')
    user = models.ForeignKey(User, verbose_name='Usuario', editable=False, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')


    class Meta:
        verbose_name= 'Articulo'
        verbose_name_plural= 'Articulos'
        ordering = ['create_at']

    def __str__(self):
        return self.title