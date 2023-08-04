from django.db import models
from datetime import datetime

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # date = models.DateField(default=datetime.utcnow,)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.email}'


# Данный код можно поместить в любой файл приложения Django, который будет обрабатывать отправку электронной почты. Например, можно создать отдельный модуль "utils.py" внутри приложения и поместить этот код внутрь него. Затем можно импортировать функцию "function" из этого модуля и использовать ее в других частях приложения, где необходимо отправлять электронные письма.


# from django.conf import settings
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from django.utils.html import strip_tags

# def function(request,**kwargs):
#    sender = settings.EMAIL_HOST_USER
#    receiver = kwargs['receiver']
#    subject = kwargs['subject']
#    context = kwargs['context']
#    html_content = render_to_string(kwargs['template'], context) # рендеринг с динамическим значением
#    text_content = strip_tags(html_content) # удаление хтмл тегов
#    email = EmailMultiAlternatives(subject, text_content, sender, receiver)
#    email.attach_alternative(html_content, "text/html")
#    email.send(fail_silently=True)
#    return True