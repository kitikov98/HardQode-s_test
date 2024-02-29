from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Product, Group, Lesson


@receiver(post_save, sender=Product)
def distribute_users(sender, instance, created, **kwargs):
    if created:
        groups = Group.objects.filter(product=instance).order_by('users__count')
        users = User.objects.filter(groups=None)
        user_count = users.count()

        for group in groups:
            group_users = users[:group.max_users - group.min_users + 1]
            group.users.add(*group_users)
            users = users[group.max_users - group.min_users + 1:]
            user_count = user_count - group.max_users

@receiver(post_save, sender=Lesson)
def update_lesson_count(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.lesson_count = Lesson.objects.filter(product=product).count()
        product.save()

