from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
# from django.http import request

def function(request,**kwargs):
   sender = settings.EMAIL_HOST_USER
   receiver = kwargs['receiver']
   subject = kwargs['subject']
   context = kwargs['context']
   html_content = render_to_string(kwargs['template'], context) # рендеринг с динамическим значением
   text_content = strip_tags(html_content) # удаление хтмл тегов
   email = EmailMultiAlternatives(subject, text_content, sender, receiver)
   email.attach_alternative(html_content, "text/html")
   # email.send()
   email.send(fail_silently=True)
   return True

# from django.conf import settings
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from django.utils.html import strip_tags

# def function(request, **kwargs):
#    sender = settings.EMAIL_HOST_USER
#    receiver = kwargs['receiver']
#    subject = kwargs['subject']
#    context = kwargs['context']
#    html_content = render_to_string(kwargs['template'], context) # рендеринг с динамическим значением
#    text_content = strip_tags(html_content) # удаление хтмл тегов
#    email = EmailMultiAlternatives(subject, text_content, sender, [receiver])
#    email.attach_alternative(html_content, "text/html")
#    email.send(fail_silently=True)
#    return True

# from django.conf import settings
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from django.utils.html import strip_tags

# def function(request, **kwargs):
#    sender = settings.EMAIL_HOST_USER
#    receiver = kwargs.get('receiver')
#    subject = kwargs.get('subject')
#    context = kwargs.get('context')
#    template = kwargs.get('template')
#    if receiver and subject and context and template:
#        html_content = render_to_string(template, context) # рендеринг с динамическим значением
#        text_content = strip_tags(html_content) # удаление хтмл тегов
#        email = EmailMultiAlternatives(subject, text_content, sender, [receiver])
#        email.attach_alternative(html_content, "text/html")
#        email.send(fail_silently=True)
#        return True
#    return False