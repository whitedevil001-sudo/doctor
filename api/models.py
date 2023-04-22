from django.db import models

class appointment(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    client_name = models.CharField(max_length=100)
    notes = models.TextField()





class doctors(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    type=models.CharField(max_length=50,choices=(('Surgeon','Surgeon'),('psychiatrist','psychiatrist'),('neurologist','neurologist'),('general practitioner','general practitioner')))
    active=models.BooleanField(default=True)
        