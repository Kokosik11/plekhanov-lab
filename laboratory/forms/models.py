from django.db import models

class Feedback(models.Model):
  first_name = models.CharField("Имя", max_length=150)
  email = models.EmailField()
  phone = models.CharField("Телефон", max_length=150)
  timestamp = models.DateTimeField("Дата", auto_now_add=True)

  def __str__(self):
    return self.email

  class Meta:
    verbose_name = "Заявка"
    verbose_name_plural = "Заявки"