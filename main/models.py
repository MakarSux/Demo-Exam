from django.db import models

from django.contrib.auth.models import User

STATUSES = (
    ('Новый', 'Новый'),
    ('В обработке', 'В обработке'),
    ('Выполнен', 'Выполнен'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100, default="")
    
class Statement(models.Model):
    adress = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Статус', max_length=200, choices=STATUSES, default='Новый')
    
    def save(self, *args, **kwargs):
        # Проверка, является ли пользователь администратором
        user = kwargs.pop('user', None)
        if user and (user.is_staff or user.is_superuser):
            # Администратор может выбирать любой статус
            pass
        else:
            # Обычный пользователь получает статус "Новый"
            self.status = 'Новый'
        
        super().save(*args, **kwargs)
    
