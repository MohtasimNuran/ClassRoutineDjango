from django.db import models

RoomType = (
    ('Normal', 'Normal'),
    ('Computer lab', 'Computer lab'),
    ('Electronics lab', 'Electronics lab'),
)


# Create your models here.

class Holiday(models.Model):
    holiday_Id = models.AutoField(primary_key=True)
    holidayStart_date = models.CharField(max_length=500, blank=True)
    holidayEnd_date = models.CharField(max_length=500)
    holiday_description = models.CharField(max_length=1000, blank=True)
    holidayInDays = models.CharField(max_length=500)

    def __str__(self):
        return self.holiday_description


class ClassRoom(models.Model):
    room_Id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=500, choices=RoomType)
    room_number = models.CharField(max_length=500)

    def __str__(self):
        return self.room_number


class ClassTime(models.Model):
    time_Id = models.AutoField(primary_key=True)
    time_period = models.CharField(max_length=500)

    def __str__(self):
        return self.time_period
