from django.db import models

# Create your models here.
class Teacher(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class TimeTable(models.Model):
    Day = models.CharField(max_length=100, choices=[('Monday','Monday'), ('Tuesday','Tuesday'), ('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday')])
    Teacher_id = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    Lecture = models.CharField(max_length=100, choices=[('CSE310','CSE310'), ('INT404','INT404'), ('MTH302','MTH302')] )
    Time = models.CharField(max_length=100, choices=[('9-10', '9-10'), ('10-11', '10-11'),('11-12', '11-12'),('12-01', '12-01'),('02-03', '02-03'),('03-04', '03-04'),('04-05', '04-05')])

    def __repr__(self):
        return '{Day:'+self.Day+' , Teacher_id:'+str(self.Teacher_id)+', Lecture:'+self.Lecture+', Time:'+self.Time+'}'
