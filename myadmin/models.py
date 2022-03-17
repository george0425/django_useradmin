from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=100)
    password_salt = models.CharField(max_length=50)
    status = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username + ":"+ str(self.status)

    class Meta:
        db_table = 'user'

