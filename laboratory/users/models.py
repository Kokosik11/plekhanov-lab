from django.db import models
from django.contrib.auth.models import User
from mainpage.models import Services
from PIL import Image
import uuid

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default="default.jpg", upload_to="profile_images")
  phone = models.CharField("Телефон", max_length=50, blank=True)
  birthdate = models.DateField(blank = True, null = True)

  def __str__(self):
    return f'Профиль пользователя {self.user.username}'

  def save(self, *args, **kwards):
    super().save()
    
    image = Image.open(self.image.path)
    
    if image.height > 64 or image.width > 64:
      resize = (64, 64)
      image.thumbnail(resize)
      image.save(self.image.path)
      
  class Meta:
    verbose_name = "Профиль"
    verbose_name_plural = "Профили"
    User._meta.get_field('email')._unique = True


class Order(models.Model):

  CHOICESSTATUS = {
      ('Оформлен', 'Оформлен'),
      ('Принят', 'Принят'),
      ('Отменен', 'Отменен'),
      ('В процессе', 'В процессе'),
  }

  def generateUUID():
    return str(uuid.uuid4().hex[:4].upper())

  created = models.DateTimeField('Создано', auto_now_add=True)
  updated = models.DateTimeField('Обновлено', auto_now=True)
  number = models.CharField("Номер заказа", primary_key=True, default=generateUUID, max_length=50, editable=False)
  status = models.CharField('Статус', max_length=100, default="Оформлен", choices=CHOICESSTATUS)
  user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, related_name='orders', verbose_name="Заказы")
  commentary = models.TextField('Комментарий к заказу', max_length=500, blank=True)
  paid = models.BooleanField('Оплачено', default=False)

  def __str__(self):
    return f'{self.user.username} - {self.number}'

  class Meta:
    ordering = ('-created',)
    verbose_name = 'Заказ'
    verbose_name_plural = "Заказы"


class OrderItem(models.Model):
  order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
  service = models.ForeignKey(Services, verbose_name="Услуга", related_name='order_items', on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.id}'