
from django.db import models
# from datetime import datetime
# from django.contrib.auth.models import User
# from news.models import Category

class Subscriber(models.Model):
    sub_user = models.CharField(verbose_name="Подписчик", max_length=100)
    sub_email = models.EmailField(verbose_name="Почта", unique=True, null=True)
    date = models.DateTimeField(verbose_name="Дата подписки", auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.sub_user} | {self.sub_email} | {self.date}'

    # sub_user = models.ForeignKey(User, on_delete = models.CASCADE)
    # sub_category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    # date = models.DateField(default=datetime.utcnow,)