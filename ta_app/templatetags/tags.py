from django import template
from ta_app.models import Task
from django.contrib.auth.models import User
from django.db.models import Sum

register = template.Library()

@register.simple_tag
def total_reward(user):
    total = user.task_set.all().aggregate(Sum('reward'))
    if total['reward__sum'] == None:
        total['reward__sum'] = 0
    return total['reward__sum']