from typing import Any, Dict
from unicodedata import category
from django.shortcuts import render
# from django.core.mail import send_mail
# from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  #, HttpResponseRedirect
from django.conf import settings
# from django.views import View
from django.views.generic.edit import CreateView

from .models import Subscriber 
from news.models import Category, User
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string


# from django.shortcuts import render
from .forms import SubscriberForm
from .utils import function

class SubscriberView(CreateView):
    model = Subscriber
    form_class = SubscriberForm
    template_name = 'mail/subscribe.html'
    success_url = '/'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     contex = super().get_context_data(**kwargs)
    #     contex['subscribes'] = Category.objects.all()

@login_required  
def get(request, category_id):
    category = Category.objects.get(id=category_id)  
    print(category)
    category.subscribers.add(request.user)  
    # return HttpResponseRedirect('/news/')
    return render(request, 'subscribe.html')


# def subscribe(request):
#     if request.method == 'POST':
#         form = SubscriberForm(request.POST)
#         name = request.user
#         if form.is_valid():
#             name = request.user
#             form.save()
#             return render(request, 'success.html')
#     else:
#         form = SubscriberForm()
#     return render(request, 'subscribe.html', {'form': form})
    


@login_required
def subscribe(request, pk):
    # if request.method == 'POST':
    #     email = request.POST['email']
    user = request.user
    category = Category.objects.get(pk=pk)
    email = user.email
    if not category.subscribers.filter(id=user.id).exists():
        category.subscribers.add(user)
        # сохранение адреса электронной почты в базе данных
        context = {
            'category': category,
            'user': user,
            'email': email,
            }

        function(request, receiver=email, subject='Подписка на рассылку', context=context, template='subscribe.html')
        return render(request, 'subscribe.html')
    else:
        return render(request, 'subscribe.html')
    
# @login_required
# def unsubscribe(request):
#     if request.method == 'POST':

#         email = request.POST['email'].delete()
#         # Удаление адреса электронной почты из базы данных
#         # context = context.filter(email=email).delete()
#         # EmailModel.objects.filter(email=email).delete()
#         return HttpResponse('Вы успешно отписались от рассылки.')
#     else:
#         return render(request, 'unsubscribe.html')
    
# from django.conf import settings
# from django.core.mail import send_mail

# settings.configure(
#     EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
#     # другие настройки...

# )

# send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['lek.dfv@mail.ru'])

# send_mail(
#         'Test Subject', 
#         'Test message body', 
#         'skillfactory.course@yandex.ru', 
#         ['lek.dfv@mail.ru'], fail_silently=False,
#         )
    
    # def get_context_data(self, **kwargs):
    # context = super(ClassName, self).get_context_data(**kwargs)
    # return context
# def subscribe(request):
#     if request.method == 'POST':
#         form = SubscriberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'success.html')
#     else:
#         form = SubscriberForm()
#     return render(request, 'subscribe.html', {'form': form})

    

# class SubscribeCategoryView(View):  
# @login_required  
# def get(request, category_id):
#     category = get_object_or_404(Category, id=category_id)  
#     category.subscribers.add(request.user)  
#     return HttpResponseRedirect('/news/')  
 
# class SendNewsEmailView(View):  
# def post( request):  
#     user_id = request.POST.get('user_id')  
#     news_id = request.POST.get('news_id')  
#     user = get_object_or_404(User, id=user_id)  
#     article = get_object_or_404(Post, id=news_id)  
#     subject = news.title  
#     message = render_to_string('news/email_template.html', {  
#         'user': user,  
#         'news': news,  
#     })  
#     send_mail(subject, '', 'your_email@example.com', [user.email], html_message=message)  
#     return HttpResponseRedirect('/news/') 

    # def subscribe(request):
    #     if request.method == 'POST':
    #         form = SubscriberForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return render(request, 'success.html')
    #     else:
    #         form = SubscriberForm()
    #     return render(request, 'subscribe.html', {'form': form})


# @login_required
# def subscribe_category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     category.subscribers.add(request.user)
#     return HttpResponseRedirect('/news/')  # Перенаправление на стран




# class Meta:
        #     '''Meta definition for ModelName.'''
    
        #     verbose_name = 'ModelName'
        #     verbose_name_plural = 'ModelNames'

# class Mail(View):
# def mail(request):

# from django.contrib.auth.decorators import login_required
# from news.models import Category
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from django.shortcuts import redirect


# @login_required
# def subCategory(request, pk):
#     user = request.user
#     category_mail = Category.objects.get(id=pk)
    
#     if not category_mail.subscribers.filter(id=user.id).exists():
#         category_mail.subscribers.add(user.id)
#         email = user.email
#         # загруж шаблон и вызыв метод render
#         html_content = render_to_string (  'mail/newsmail.html',
#                                             {  'categories': category_mail,
#                                                 'user' : user,
#                                             },
#                                         )
#         msg = EmailMultiAlternatives(
#             subject=f'Подтверждение подписи на категорию - {category_mail.name}',
#             body='',
#             from_email='vet.nes@yandex.ru',
#             to=[email, 'vetaness@mail.ru'], # пишу свою почту для проверки
#         )
#         msg.attach_alternative(html_content, "text/html") # добавляем html
#         try:
#             msg.send() # отсылаем  
#         except Exception as e:
#             print(e)
#         return redirect('edit')
#     return redirect(request.Meta.get('HTTP_REFERER'))


# @login_required
# def unsubCategory(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     if category.subscribers.filter(id=user.id).exists():
#         category.subscribers.remove(user.id)
#     return redirect('edit')

