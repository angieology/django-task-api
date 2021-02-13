from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

class TaskMeta(models.Model):
  task = models.OneToOneField(Task, on_delete=models.CASCADE, blank=True, null=True)
  completed = models.DateField(auto_now=True)
      
  def __str__(self):
    return self.task.title

def create_task_meta_on_post_save_signal(sender, instance, created, **kwargs):
  if created:
    TaskMeta.objects.create(task=instance)
    print('task meta created!')
post_save.connect(create_task_meta_on_post_save_signal, sender=Task)

def update_task_meta_on_post_save_signal(sender, instance, created, **kwargs):
  if created == False:
    instance.taskMeta.save()
    print('profile updated!')
post_save.connect(update_task_meta_on_post_save_signal, sender=Task)