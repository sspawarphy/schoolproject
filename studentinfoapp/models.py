from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    rollNo=models.IntegerField()
    name=models.CharField(max_length=40)
    mobile=models.IntegerField()
    addr=models.CharField(max_length=100)
    def __str__(self):
        return 'StudentInfo Object with rollNo:+str(self.rollNo)'
