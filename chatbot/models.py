from django.db import models

# Create your models here.
class Subway(models.Model):
    line_name=models.CharField(max_length=20)
    station_name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.station_name
        
class Schedule(models.Model):
    time=models.DateTimeField()
    subway=models.ForeignKey(Subway)
    weather=models.CharField(max_length=20)
    interval=models.IntegerField()
    
    def __str__(self):
        return str(self.time)

class User(models.Model):
    user_key=models.CharField(max_length=250)
    stacked_data=models.IntegerField()
    
    def __str__(self):
        return self.user_key
    
class Data(models.Model):
    schedule=models.ForeignKey(Schedule)
    user=models.ForeignKey(User)
    time=models.DateTimeField()
    
    SIT_IN_DATA_CHOICES = (
        (1, '입석'),
        (2, '착석')
    )
    DETAIL_IN_DATA_CHOICES=(
        (1,'콩나물 시루다'),
        (2,'자리는 없다'),
        (3,'자리가 남아 있다')
        )
    sit=models.IntegerField(choices=SIT_IN_DATA_CHOICES)
    detail=models.IntegerField(choices=DETAIL_IN_DATA_CHOICES)
    
    def __str__(self):
        return str(self.time)+' '+str(self.schedule.subway.station_name)

    