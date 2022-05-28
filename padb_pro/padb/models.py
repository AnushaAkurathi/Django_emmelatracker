from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


"""class announcements(models.Model):
    info = models.CharField(max_length=500, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    # timestamp = models.DateTimeField(default = now, blank=True)
    

    class Meta:
        # ordering = ['-created_on']
        db_table = 'announcements'

    def __str__(self):
        return self.info"""



"""class attendance(models.Model):
    id_choices = (('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('None', 'None'))
    ids = models.CharField(max_length = 20, choices = id_choices, default = 'None')
    
    reason = models.CharField(max_length=200, default = 'None')
    details = models.CharField(max_length=200, default = 'None')
    leave_for = models.FloatField(default = 'None')
    
    type_choices = (('Present', 'Present'), ('WFH','WFH'), ('Leave', 'Leave'), ('Break', 'Break'), ('None', 'None'))
    typ_e = models.CharField(max_length = 20, choices = type_choices, default = 'None')
    
    date =  models.DateField(default=now)
    created_at = models.DateTimeField(default = now, blank=True)
    
    b_choices = (('1 Hrs', '1 Hrs'), ('2 Hrs', '2 Hrs'), ('None', 'None'))
    brea_k = models.CharField(max_length = 20, choices = b_choices, default = 'None')




    class Meta:
        # ordering = ['-created_on']
        db_table = 'attendance'
        unique_together = ('ids','date')


    def __str__(self):
        return self.ids"""

