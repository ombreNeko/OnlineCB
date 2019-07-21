from django.db import models

# Create your models here.
# Course becomes a model, as we are inheriting Models class (in model module) to class Course.
class Course(models.Model):
    name = models.CharField(max_length =256)
    price = models.FloatField()
    description = models.TextField()
    instructor = models.ForeignKey('Instructor',on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    photo = models.URLField(null = True, blank = True)
    name = models.CharField(max_length = 256)
    email = models.EmailField() 