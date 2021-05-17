from django.db import models
from shortuuidfield import ShortUUIDField

STATUS = (
  (0, "Draft"),
  (1, "Publish")
)

class Post(models.Model):
  title = models.CharField("Название", max_length=200)
  slug = models.SlugField("Ссылка", max_length=130, unique=True, help_text="Ссылка на пост")
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField() # Need to connect tinymice
  created_on = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(choices=STATUS, default=0)
  is_head = models.BooleanField(default=False)
  image = models.ImageField("Фото", upload_to='post_images', blank=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-created_on']
    verbose_name = "Пост"
    verbose_name_plural = "Посты"


class Project(models.Model):
  name = models.CharField("Название проекта", max_length=200)
  slug = models.SlugField("Ссылка", max_length=130, unique=True, help_text="Ссылка на проект")
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(choices=STATUS, default=0)
  year = models.PositiveSmallIntegerField("Год", default=2021)
  image = models.ImageField("Фото", upload_to='project_images', blank=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['-created_on']
    verbose_name = "Проект"
    verbose_name_plural = "Проекты"

class Feedback(models.Model):
  name = models.CharField("Имя", max_length=200)
  email = models.EmailField()
  phone = models.CharField("Телефон", max_length=150)
  uuid = ShortUUIDField()

  def __str__(self):
    return self.email

  class Meta:
    verbose_name = "Отклик"
    verbose_name_plural = "Отклики"

class Services(models.Model):
  created = models.DateTimeField('Создано', auto_now_add=True)
  updated = models.DateTimeField('Обновлено', auto_now=True)
  name = models.CharField("Название услуги", max_length=200)
  price = models.DecimalField("Стоимость", max_digits=5, decimal_places=1, blank=True)
  
  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Услуга"
    verbose_name_plural = "Услуги"