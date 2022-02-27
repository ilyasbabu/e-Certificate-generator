from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.IntegerField()


