from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default="default.jpg", upload_to="profile_images")
  phone = models.CharField("Телефон", max_length=50, blank=True)
  birthdate = models.DateField(blank = True, null = True)
  
  def save(self, *args, **kwards):
    super().save()
    
    image = Image.open(self.image.path)
    
    if image.height > 64 or image.width > 64:
      resize = (64, 64)
      image.thumbnail(resize)
      image.save(self.image.path)

  def __str__(self):
    return f'Профиль пользователя {self.user.username}'