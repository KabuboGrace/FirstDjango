from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    age= models.IntegerField(null=True)
    phone_numbers= models.IntegerField(null=True)

    class Meta:
        db_table= "Student"

    def __str__(self):
        return self.firstname + ' ' + self.lastname