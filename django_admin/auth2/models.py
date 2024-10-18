from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_days = models.JSONField(default=list)  # 存储工作日，例如 ['1', '2', '3', '4', '5']
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()
    pay_day = models.CharField(max_length=50)
    daily_income = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)  # 记录最后更新时间
