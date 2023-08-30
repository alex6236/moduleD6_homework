from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
# from django.shortcuts import render


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return self.authorUser.username

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum('rating')) or 0
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.all(
        ).aggregate(commentRating=Sum('rating')) or 0
        cRat = 0
        cRat += commentRat.get('commentRating')
        self.ratingAuthor = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.name
    
# class Subscription(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
#     subscribed_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.category.name}"
    
    
# class Subscriber(models.Model):
#     sub_user = models.CharField(verbose_name="Подписчик", max_length=100)
#     sub_email = models.EmailField(verbose_name="Почта", unique=True, null=True)
#     date = models.DateTimeField(verbose_name="Дата подписки", auto_now_add=True)

#     def __str__(self):
#         return f'{self.sub_user} | {self.sub_email} | {self.date}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dataCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=124)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:123] + '...'
    
    def __str__(self):
        categories = ', '.join([str(category) for category in self.postCategory.all()])
        return f"Заголовок: {self.title} |Дата: {self.dataCreation} |Автор: {self.author.authorUser.username} |Категория: {categories}"
 


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.categoryThrough    


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dataCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.text

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

