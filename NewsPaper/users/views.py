from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from news.models import Category, Post
from users.models import Subscriber
from .forms import SubscriberForm
from django.views.generic.edit import CreateView
# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import Group
from news.models import Author
from django.shortcuts import get_object_or_404
# from django.db import models

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL

class AccountsView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
        Author.objects.create(authorUser=user)
    return redirect('/')

class SubscriberView(LoginRequiredMixin, TemplateView):
    model = Subscriber
    template_name = 'users/subscribe.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sub_user = self.request.user
        print(sub_user)
        category_name = self.kwargs.get('category_name')
        category = Category.objects.filter(name=category_name)
        # category = Category.objects.get(name=category_name)
        # category = get_object_or_404(Category, name=category_name)
        print(category)
        # is_subscriber = Subscriber.objects.filter(user=sub_user, category=category).exists()
        # if not is_subscriber:
        #     Subscriber.objects.create(user=sub_user, category=category)
        #     category.subscribers.add(sub_user)
        # context['is_subscriber'] = is_subscriber
        context['category'] = category 
        return context

